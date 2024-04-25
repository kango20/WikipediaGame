# Wikipedia Game Improvement Proposal (WGIP)

## Authors
- Author: Karen Ngo

## Introduction
The Wikipedia Game is a challenge that involves navigating from one specified Wikipedia article to another using the least number of clicks. The user enters the Wikipedia link of the starting page and the final page, and the program's searching algorithm will attempt to find a path of links from the source to final.

A fundamental algorithm for finding the shortest path in such a networked environment is the Breadth-First Search (BFS) algorithm. BFS systematically explores a graph's edges to discover every vertex reachable from the source vertex, making it an ideal choice for finding the shortest path in the Wikipedia Game.

## Proposed Improvement: Transformer-Based Semantic Pathfinding

### Overview
This improvement integrates a transformer-based model for semantic similarity measurement into the BFS algorithm. By leveraging the advanced natural language understanding capabilities of transformers, the algorithm can better prioritize links that are semantically closer to the target article's topic, potentially reducing the number of hops needed to reach the target.

### Rationale
Traditional BFS treats all links equally, potentially leading to longer and less relevant paths. Integrating transformer-based semantic similarity allows the search to be guided towards more relevant articles, making the search more efficient and educational.

### Description
The core improvement involves utilizing transformer-based models to enhance the Wikipedia Game's pathfinding mechanism. Unlike traditional BFS, which treats all links equally, this method uses transformers to assess and prioritize links based on their semantic closeness to the target article.

### Key Components:

- **Priority Queue in BFS**: Incorporates a priority mechanism into the BFS algorithm, where links are queued based on their semantic similarity score. Links with higher relevance to the target article are explored first, leading to potentially quicker discovery of the shortest path.

- **Transformer-Based Semantic Similarity Measurement**: Uses pre-trained transformer models, such as BERT or GPT, to calculate the semantic similarity between the text of the current Wikipedia article and the target article. This identifies which links are closer to the target, aiming to reduce the path length through more informed path choices.
  
### Expected Benefits:

- **Efficiency**: Prioritizing semantically related links can quickly find shorter paths, reducing the number of clicks needed to reach the target.

### Implementation Considerations:

- **Transformer Model Selection and Preprocessing**: The choice of transformer model and its preprocessing steps are crucial for the effectiveness of this improvement. Different models and configurations may offer varying degrees of semantic understanding.
  
- **Computational Resources**: Transformer models are resource-intensive. Efficient implementation and caching strategies for similarity scores are important considerations.

### Pseudo-Code

```python
import wikipedia
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from queue import PriorityQueue

def get_transformer_similarity_score(source_text, target_text, model, tokenizer):
    # Tokenize the input texts
    inputs = tokenizer(source_text, target_text, return_tensors='pt', padding=True, truncation=True)
    # Calculate the embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the model's output to determine similarity (example uses cosine similarity)
    similarity_score = outputs.logits.softmax(dim=1).numpy()[0, 1]
    return similarity_score

def transformer_semantic_bfs(start_article, target_article, model, tokenizer):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_article, [start_article]))

    while not queue.empty():
        _, current_article, path = queue.get()
        if current_article == target_article:
            return path

        visited.add(current_article)
        links = wikipedia.page(current_article).links
        for link in links:
            if link not in visited:
                similarity_score = get_transformer_similarity_score(wikipedia.page(link).summary, wikipedia.page(target_article).summary, model, tokenizer)
                new_path = list(path)
                new_path.append(link)
                queue.put((-similarity_score, link, new_path))  # Note: negative score because PriorityQueue is min-first
```
## Special Libraries Required
- Wikipedia API: For fetching article links.
- Transformers: For utilizing pre-trained transformer models for natural language processing tasks.
- 
## Challenges and Limitations
- Computational Overhead: Calculating semantic similarity for every link may increase computational overhead.
- Relevance Accuracy: The accuracy of semantic similarity measures can vary, potentially affecting pathfinding efficiency.
- Model Limitations: Pre-trained models may not perfectly capture the semantic relationship for all topics.

## Milestones
### Milestone 1: Project Setup and Preliminary Research
- **Objective**: Set up the development environment and complete preliminary research on transformer models suitable for the project.
- **Deliverables**:
  - A development environment setup, including necessary software, tools, and libraries (Python, PyTorch, Transformers library, Wikipedia API).
  - Summarize the transformer models evaluated, with a focus on BERT and GPT, and the chosen model.
- **Deadline**: April 4, 2024

### Milestone 2: Development
- **Objective**: Develop a basic prototype that integrates the transformer model with the BFS algorithm for semantic pathfinding.
- **Deliverables**:
  - A working prototype script that can perform semantic BFS on a small subset of Wikipedia articles.
  - Documentation of the prototype, including a description of the algorithm and instructions for running the prototype.
- **Deadline**: April 18, 2024

### Milestone 3: Efficiency and Optimization
- **Objective**: Optimize the prototype for efficiency and scalability, focusing on reducing computational overhead.
- **Deliverables**:
  - An optimized version of the prototype that includes efficiency improvements such as caching similarity scores and optimizing transformer model usage.
- **Deadline**: April 25, 2024

### Milestone 4: Testing and Feedback
- **Objective**: Conduct comprehensive testing of the system and collect user feedback.
- **Deliverables**:
  - A test plan and report outlining the testing methodology, test cases, and results.
  - A collection of user feedback on the usability and educational value of the game.
- **Deadline**: May 2, 2024
