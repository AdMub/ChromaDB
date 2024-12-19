### Step 2:Environment Setup
## python3 -m venv .venv          Create a Python virtual environment
## activate the virtual environment:
# source .venv/bin/activate      On macOS/ Linux
## pip install chromadb        install the required packages
## pip install git+https://github.com/huggingface/transformers     install the transformers library, which will be used for generating embeddings with pre-trained models
## pip install sentence-transformers     install the sentence-transformers library, which provides additional functionality for working with text embeddings:


### Step 2:Setting Up ChromaDB
##  import the necessary libraries
from sentence_transformers import SentenceTransformer
import chromadb

## Initialize ChromaDB and create a new collection
client = chromadb.Client()
collection = client.create_collection("text_collection")

### Step 3:Loading the Pre-Trained Embedding Model and Ingesting Text 
## Generate embeddings for text data,  the pre-trained model all-MiniLM-L6-v2, which is a compact model that provides high-quality sentence embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

## add multiple text entries that represent different types of content, ranging from iconic landmarks to scientific discoveries and everyday scenes.
texts = [
    "The Eiffel Tower in Paris is an iconic landmark.",
    "A delicious homemade pizza fresh from the oven.",
    "A scientist studying the effects of climate change on polar bears.",
    "A group of friends hiking through the mountains during autumn.",
    "The discovery of water on Mars could mean the possibility of life.",
    "The rise of artificial intelligence is reshaping industries.",
    "A peaceful garden filled with blooming flowers and chirping birds.",
    "A musician playing the violin in a crowded subway station.",
    "A historical novel set during World War II.",
    "An astronaut floating weightlessly in space.",
     "The space shuttle launched into orbit, marking a new era in space exploration.",
    "An advanced AI system is helping doctors diagnose rare diseases.",
    "A cozy cafe in the city center where people gather to relax and chat."
]


## Generate embeddings for each text entry and insert those embeddings into your ChromaDB collection
embeddings = model.encode(texts)

collection.add(
    embeddings=embeddings,
    metadatas=[{"text": text} for text in texts],
    ids=[str(i) for i in range(len(texts))]
)

### Step 4: Making Queries and Displaying the Results
## create a few queries that represent different concepts.
queries = [
    "A musician performing in public",
    "A peaceful place with flowers and birds",
    "Medical professionals using machine learning to find rare illnesses", 
    "Astronaughts traveling to outside of earth",
    "Relaxing at a shop with friends",
]


## iterate through the defined queries and perform vector searches to find the top 3 most similar entries in your collection.
for query in queries:
    print(f"\nQuery: {query}")
    
    # Generate an embedding for the query text
    query_embedding = model.encode(query)

    # Perform a vector search in the collection
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3  # Retrieve top 3 similar entries
    ) 


## Display the results from the search by retrieving the text metadata associated with each result.
    for i, result in enumerate(results['metadatas'][0]):
         print(f"Result {i + 1}: {result['text']}")


## python3 text-to-text.py   run the script on your terminal