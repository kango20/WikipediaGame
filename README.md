# Wikipedia Game Improvement Proposal (WGIP)

## Project Description
The Wikipedia Game challenges players to navigate from one Wikipedia article to another using the least number of clicks. The project enhances this game by integrating a transformer-based model to measure semantic similarity, improving the pathfinding algorithm. By utilizing Breadth-First Search (BFS) augmented with a transformer model, the game prioritizes links that are semantically closer to the target article, potentially reducing the number of hops needed to reach the goal. This method makes the search more efficient and enhances the game's educational value by guiding players through more relevant content.

### Key Features

- **Semantic Analysis:** Utilizes the transformer model "sentence-transformers/all-MiniLM-L6-v2" to generate semantic embeddings of Wikipedia articles. This allows the system to prioritize links that are more relevant to the target article's content.

- **Pathfinding Algorithm:** Combines traditional BFS with a modern approach to semantic similarity, sorting possible paths by their relevance to the target article, ensuring more efficient navigation.

- **Link Extraction:** Employs BeautifulSoup for web scraping, extracting and filtering valid Wikipedia links from articles, focusing on those that contribute to a more relevant path toward the target article.

- **Efficiency and Timeout Management:** Implements a timeout mechanism to prevent excessive computation times, ensuring the game remains responsive even under constraints.

## Educational Value

By guiding players through content that is semantically related to the target article, the game not only makes the search process more efficient but also enhances the learning experience, making it a powerful educational tool.



## Installation Instructions
To run and test the WGIP, you need to install several libraries and set up a suitable Python environment. Follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kango/WGIP.git](https://github.com/kango20/WikipediaGame.git
2. **Install Python:**
Download and install it from [python.org](https://www.python.org/downloads/)
3. **(Optional) Set Up a Virtual Environment:**
Use a virtual environment to manage the Python packages for this project:
```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS and Linux:
source myenv/bin/activate
```
4. **Install Required Packages:**
```bash
pip install requests beautifulsoup4 tensorflow transformers
```

## Testing
Run the code using this script:
```bash
python3 server.py
```
Click on the HTTP link provided and enter the link of the start Wikipedia page and the final Wikipedia page. Click search and the program will begin running the algorithm while printing the ongoing status in the terminal and log.


## Limitations and Future Works

### Limitations

1. **Timeout Handling**:
   - Although the timeout mechanism ensures the search does not run indefinitely, it may interrupt the process before a path is found. This can be particularly problematic for searches involving distant or loosely connected Wikipedia pages.

2. **Dependency on External Services**:
   - The algorithm relies on external requests to fetch Wikipedia pages. Any downtime or latency from Wikipedia servers can affect the performance and reliability of the crawler.

3. **Semantic Similarity Limitations**:
   - The semantic similarity model, while effective, may not always capture the full context or relevance of Wikipedia pages. This can result in suboptimal paths or missed connections.

4. **Scalability**:
   - The current implementation processes pages sequentially and maintains all discovered pages in memory. This may not scale well for extensive searches or large datasets.

5. **Real-Time Logging**:
   - While real-time logging provides valuable insights into the crawling process, it may introduce additional overhead and latency, especially for high-frequency logging.
  
6. **Computationally Expensive**:
   - While calculating the semantic similarity score may be effective, it is computationally expensive and takes a long time to compute. Therefore, this slows down the time it may take to find a path exponentially. 


### Future Works

1. **Enhanced Pathfinding Algorithms**:
   - Explore alternative pathfinding algorithms that can more efficiently handle large datasets and provide more accurate results. Techniques like bidirectional search or heuristic-based methods could be used.

2. **Improved Semantic Models**:
   - Experiment with more advanced semantic models or fine-tune existing models on Wikipedia-specific data to improve the accuracy and relevance of the semantic similarity calculations.

3. **Parallel Processing**:
   - Implement parallel processing or distributed computing techniques to handle multiple pages concurrently, improving the scalability and efficiency of the crawler.

4. **Caching Mechanism**:
   - Develop a caching mechanism to store and reuse previously fetched Wikipedia pages and their embeddings. This can reduce the number of external requests and speed up the search process.

5. **Error Handling and Robustness**:
   - Enhance error handling to gracefully manage unexpected issues, such as network failures or invalid inputs. Implementing retries and fallback mechanisms can improve the overall robustness.

6. **Extended Functions**:
   - Add support for additional features, such as filtering links based on categories or topics, prioritizing certain types of links, or providing user-configurable search parameters.

By addressing these limitations and exploring future work opportunities, the project can be significantly improved in terms of efficiency, scalability, and usability.

