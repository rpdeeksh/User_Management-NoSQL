import os
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://deekshithrpbtech22:<your cluster password>@cluster0.ur8n9.mongodb.net/?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true&appName=Cluster0")  
    db = client["Databade Name"]  # Database name
    return db["Collection Name"]  # Collection name
