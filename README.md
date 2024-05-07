# Wikipedia Game Improvement Proposal (WGIP)

## Project Description
The Wikipedia Game challenges players to navigate from one Wikipedia article to another using the least number of clicks. The project enhances this game by integrating a transformer-based model to measure semantic similarity, improving the pathfinding algorithm. By utilizing Breadth-First Search (BFS) augmented with a transformer model, the game prioritizes links that are semantically closer to the target article, potentially reducing the number of hops needed to reach the goal. This method makes the search more efficient and enhances the game's educational value by guiding players through more relevant content.

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
