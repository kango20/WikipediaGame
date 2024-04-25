import time
import requests
from bs4 import BeautifulSoup
import re
from transformers import AutoTokenizer, TFAutoModel
import tensorflow as tf

# Constants
TIMEOUT = 300  # time limit in seconds for the search

# Load transformer model and tokenizer for TensorFlow
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = TFAutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='tf', truncation=True, max_length=512)
    outputs = model(inputs)
    return outputs.pooler_output[0]

def semantic_similarity(embedding1, embedding2):
    return tf.keras.losses.cosine_similarity(embedding1, embedding2).numpy().item()

def get_links(page_url):
    print(f"Fetching page: {page_url}")
    response = requests.get(page_url)
    print(f"Finished fetching page: {page_url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]
    print(f"Found {len(links)} links on page: {page_url}")
    return links

def find_path(start_page, finish_page):
    finish_page_text = requests.get(finish_page).text
    finish_page_embedding = get_embedding(finish_page_text)

    queue = [(start_page, [start_page], 0, get_embedding(requests.get(start_page).text))]
    discovered = set()

    start_time = time.time()
    while queue:
        queue.sort(key=lambda x: -semantic_similarity(x[3], finish_page_embedding))  # prioritize by similarity
        (vertex, path, depth, embedding) = queue.pop(0)
        if time.time() - start_time > TIMEOUT:
            raise TimeoutError("Search exceeded time limit.")
        
        for next in set(get_links(vertex)) - discovered:
            next_text = requests.get(next).text
            next_embedding = get_embedding(next_text)
            
            if next == finish_page:
                print(f"Found finish page: {next}")
                return path + [next]
            else:
                discovered.add(next)
                queue.append((next, path + [next], depth + 1, next_embedding))
    return []


