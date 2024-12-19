# ChromaDB

## Description

In a world where data is growing exponentially, traditional databases struggle to handle complex, high-dimensional data like images and text. Vector databases like ChromaDB are designed specifically to store and search data represented as vectors—mathematical entities that capture the essential features of rich data types.

With ChromaDB, you can:

Search for a sunset by showing another sunset image.

Find related product descriptions using keywords.

Enable recommendation engines and content retrieval systems powered by AI-driven insights.

## Learning Outcomes

Understand the principles and applications of vector databases, particularly ChromaDB.

Set up and configure ChromaDB on your local machine.

Generate vector embeddings using pre-trained models like CLIP and SentenceTransformer.

Implement vector search functionality for similarity queries on text and images.

Build an interactive Gradio-based interface for real-world use cases.

## Campaign Structure

### Quest 1: Foundations of Vector Databases

Objective: Learn the basics of vector databases and ChromaDB setup.

### Quest 2: Practical Applications of Vector Search

Objective: Implement advanced vector search functionalities.

### Quest 3: Implementing Text-to-Image Vector Search

Objective: Build a user-friendly text-to-image search system using Gradio.

Develop a complete text-to-image search application.

## Quest Steps

#### Clone the project repository:

git clone https://github.com/thebadsektor/chromadb-text-to-image.git

#### Navigate into the project directory:

cd chromadb-text-to-image

#### Create and activate a Python virtual environment:

python3 -m venv .venv

source .venv/bin/activate  # macOS/Linux

.venv\Scripts\activate   # Windows

#### Install dependencies:

pip install -r requirements.txt

### Step 2: Navigating Inside the Main Script

### Step 3: Running the Application

#### Run the script:

python3 text-to-image.py

Open the generated local URL to access the Gradio interface.

### Step 4: Testing the Application

Use predefined queries like:

Search Query: "A famous landmark in Paris"Expected Result: Image of the Eiffel Tower.

Search Query: "An Italian delicacy"Expected Result: Image of a pizza.

Open text-to-image.py, which contains core logic for vector search.

## Directory Structure

chromadb-text-to-image/

├── img/                # Sample images for comparison.

├── requirements.txt    # Project dependencies.

├── text-to-image.py    # Core script for vector search.

## Troubleshooting

### Windows Users: Avoid the uvloop library error by using Linux-based cloud environments like Gitpod or GitHub Codespaces.

#### Ensure transformers and sentence-transformers libraries are installed:

pip install git+https://github.com/huggingface/transformers
pip install sentence-transformers

## Extend Your Learning

Add new images to the /img folder.

Restart the application and test with new queries.

## Conclusion

Congratulations on completing this campaign! You’ve:

Set up ChromaDB and integrated the CLIP model.

Built and tested a Gradio-based text-to-image search application.

This campaign equips you with practical skills to design intuitive, ML-powered applications. Start exploring more with ChromaDB and push the boundaries of what’s possible with vector databases!

![image](https://github.com/user-attachments/assets/f694d486-9e2b-4f31-b048-20d85fa2ef39)

![image](https://github.com/user-attachments/assets/4a808a7e-e792-4cce-89bf-c98dda17a268)

![image](https://github.com/user-attachments/assets/8fa4880a-120a-4c0b-a140-4316db513ca1)

![image](https://github.com/user-attachments/assets/452e7a8c-8bd5-4615-bb81-e1d723270998)


@StackUp
