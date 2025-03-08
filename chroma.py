# Add to your notebook
from chromadb import PersistentClient

client = PersistentClient(path="./chroma_db")

# List collections
print(client.list_collections())

# Inspect a collection
collection = client.get_collection("your_collection_name")
print(f"Count: {collection.count()}")
print("First 5 items:", collection.peek(5))
