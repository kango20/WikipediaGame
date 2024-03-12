# Wikipedia Game Improvement Proposal (WGIP)

## Authors
- Author: Karen Ngo

## Introduction
The Wikipedia Game is a challenge that involves navigating from one specified Wikipedia article to another using the least number of clicks. The user enters the Wikipedia link of the starting page and the final page, and the program's searching algorithm will attempt to find a path of links from the source to final.

A fundamental algorithm for finding the shortest path in such a networked environment is the Breadth-First Search (BFS) algorithm. BFS systematically explores a graph's edges to discover every vertex reachable from the source vertex, making it an ideal choice for finding the shortest path in the Wikipedia Game.

## Proposed Improvement: Semantic Similarity Pathfinding

### Overview
The proposed improvement to the Wikipedia Game is by integrating a semantic similarity measure into the BFS algorithm. This approach utilizes word embeddings to prioritize links semantically closer to the target article's topic, potentially reducing the number of hops needed to reach the target.

### Rationale
Traditional BFS treats all links equally, potentially leading to longer paths that are not related to the target article. By using semantic similarity, we can guide the search towards more relevant articles, making the game more educational and efficient.

### Description
The improvement involves calculating semantic similarity scores between the text of the links in the current article and the target article using pre-trained word embedding models like Word2Vec or GloVe. The algorithm then prioritizes nodes with higher semantic similarity to the target for exploration.

### Pseudo-Code

```python
import wikipedia
from gensim.models import Word2Vec
from queue import Queue

def get_semantic_similarity_score(source_text, target_text, model):
    # Placeholder function for semantic similarity calculation
    pass

def semantic_bfs(start_article, target_article, word_embedding_model):
    visited = set()
    queue = Queue()
    queue.put((start_article, [start_article]))

    while not queue.empty():
        current_article, path = queue.get()
        if current_article == target_article:
            return path

        visited.add(current_article)
        links = wikipedia.page(current_article).links
        links_with_similarity = [(link, get_semantic_similarity_score(link, target_article, word_embedding_model)) for link in links if link not in visited]
        sorted_links = sorted(links_with_similarity, key=lambda x: x[1], reverse=True)

        for link, _ in sorted_links:
            if link not in visited:
                new_path = list(path)
                new_path.append(link)
                queue.put((link, new_path))

