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
The core improvement to the Wikipedia Game involves leveraging semantic similarity measures to enhance the efficiency and educational value of the game's pathfinding mechanism. Instead of the traditional BFS algorithm, which treats all links equally and explores them in a linear, unranked order, the proposed method integrates word embeddings to assess and prioritize links based on their semantic closeness to the target article.

### Key Components:

- **Semantic Similarity Measurement**: Utilizes pre-trained word embeddings models (e.g., Word2Vec, GloVe) to calculate the semantic similarity between the text of links in the current Wikipedia article and the target article. This approach identifies which links are  closer to the target, aiming to reduce the path length by making more informed path choices.

- **Priority Queue in BFS**: Modifies the traditional BFS algorithm to incorporate a priority mechanism, where links are enqueued based on their semantic similarity score. Links with higher relevance to the target article are explored first, potentially leading to a quicker discovery of the shortest path.

### Expected Benefits:

- **Efficiency**: By prioritizing links that are semantically related to the target article, the algorithm can find shorter paths more quickly than standard BFS, reducing the number of clicks needed to reach the target.
  
- **Educational Value**: This method encourages exploration of content that is more relevant to the target topic, enhancing the learning experience by exposing players to thematically connected articles.

### Implementation Considerations:

- **Word Embeddings Preprocessing**: The effectiveness of this improvement relies on the quality and relevance of the pre-trained word embeddings used to calculate semantic similarity.
  
- **Computational Resources**: Calculating semantic similarity for multiple links can be resource-intensive. This means there may be a higher priority to necessitate efficient implementation and possibly the use of caching strategies to store similarity scores for frequently encountered articles.


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


```
## Special Libraries Required
- Wikipedia API: For fetching article links.
- Gensim: For loading and utilizing pre-trained Word2Vec or GloVe models.

## Challenges and Limitations
- Computational Overhead: Calculating semantic similarity for every link may increase computational overhead.
- Relevance Accuracy: The accuracy of semantic similarity measures can vary, potentially affecting pathfinding efficiency.
- Model Limitations: Pre-trained models may not perfectly capture the semantic relationship for all topics.

