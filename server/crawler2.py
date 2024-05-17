import time
import requests
from bs4 import BeautifulSoup
import re
from transformers import AutoTokenizer, TFAutoModel
import tensorflow as tf

# Constants
TIMEOUT = 500  # time limit in seconds for the search

# Load transformer model and tokenizer for TensorFlow
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = TFAutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

global_logs = []

def log_message(message):
    global global_logs
    print(message)  # Log to terminal
    global_logs.append(message)  # Add message to global logs

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='tf', truncation=True, max_length=512)
    outputs = model(inputs)
    return outputs.pooler_output[0]

def semantic_similarity(embedding1, embedding2):
    log_message(f"Calculating similarity between embeddings.")
    return tf.keras.losses.cosine_similarity(embedding1, embedding2).numpy().item()

def get_links(page_url):
    log_message(f"Fetching page: {page_url}")
    response = requests.get(page_url)
    log_message(f"Finished fetching page: {page_url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]
    log_message(f"Found {len(links)} links on page: {page_url}")
    return links

def find_path(start_page, finish_page):
    global logs
    logs = []

    # Start tracking time
    start_time = time.time()

    # Fetch and process the finish page
    finish_page_text = requests.get(finish_page).text
    finish_page_embedding = get_embedding(finish_page_text)

    # Initialize the queue with the start page
    queue = [(start_page, [start_page], get_embedding(requests.get(start_page).text))]
    discovered = set()

    while queue:
        elapsed_time = time.time() - start_time
        if elapsed_time > TIMEOUT:
            log_message(f"Search took {elapsed_time} seconds.")
            log_message(f"Discovered pages: {len(discovered)}")
            raise TimeoutErrorWithLogs("Search exceeded time limit.", logs, elapsed_time, len(discovered))

        # Sort the queue based on semantic similarity with the finish page embedding
        queue.sort(key=lambda x: -semantic_similarity(x[2], finish_page_embedding))
        vertex, path, embedding = queue.pop(0)
        
        # Fetch and process links from the current vertex
        for next in set(get_links(vertex)) - discovered:
            next_text = requests.get(next).text
            next_embedding = get_embedding(next_text)
            
            # Check if the next page is the finish page
            if next == finish_page:
                log_message(f"Found finish page: {next}")
                elapsed_time = time.time() - start_time
                log_message(f"Search took {elapsed_time} seconds.")
                log_message(f"Discovered pages: {len(discovered)}")
                return path + [next], logs, elapsed_time, len(discovered)  # Return the successful path
            
            log_message(f"Adding link to queue: {next}")
            discovered.add(next)
            queue.append((next, path + [next], next_embedding))

        # Update the elapsed time at the end of each iteration
        elapsed_time = time.time() - start_time

    log_message(f"Search took {elapsed_time} seconds.")
    log_message(f"Discovered pages: {len(discovered)}")
    raise TimeoutErrorWithLogs("Search exceeded time limit.", logs, elapsed_time, len(discovered))


class TimeoutErrorWithLogs(Exception):
    def __init__(self, message, logs, time, discovered):
        super().__init__(message)
        self.logs = logs
        self.time = time
        self.discovered = discovered
