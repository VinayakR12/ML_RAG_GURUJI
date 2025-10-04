import os
import uuid
import json
import pandas as pd
import docx
import fitz  # PyMuPDF
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# ==== CONFIG ====
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")
DATA_FOLDER=os.getenv("DATA_FOLDER", "Data")  # Root folder containing files

# ---- Initialize Pinecone ----
pc = Pinecone(api_key=PINECONE_API_KEY)

existing_indexes = [i["name"] for i in pc.list_indexes()]
if INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print("Created new index:", INDEX_NAME)
else:
    print("Index already exists:", INDEX_NAME)

index = pc.Index(INDEX_NAME)

# ---- Initialize embeddings & text splitter ----
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=GOOGLE_API_KEY)
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

# ---- Helper function to extract text from different file types ----
def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
        elif ext == ".csv":
            df = pd.read_csv(file_path)
            return df.to_string()
        elif ext == ".json":
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return json.dumps(data, indent=2)
        elif ext == ".docx":
            doc = docx.Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs])
        elif ext == ".pdf":
            text = ""
            with fitz.open(file_path) as pdf:
                for page in pdf:
                    text += page.get_text()
            return text
        else:
            print(f"Unsupported file type: {ext}")
            return ""
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

# ---- Recursively gather all files in folder ----
def get_all_files(folder):
    files = []
    for root, _, filenames in os.walk(folder):
        for f in filenames:
            files.append(os.path.join(root, f))
    return files

# ---- Process files ----
all_files = get_all_files(DATA_FOLDER)
all_text = ""
processed_files = 0

for file_path in all_files:
    text = extract_text_from_file(file_path)
    if text.strip():
        all_text += text + "\n"
        processed_files += 1
    else:
        print(f" No text extracted from {file_path}")

if not all_text.strip():
    print("No text found to upload.")
    exit()

# ---- Split into chunks & create embeddings ----
chunks = splitter.split_text(all_text)
vectors = []

print(f" Generating embeddings for {len(chunks)} chunks from {processed_files} file(s)...")

for chunk in chunks:
    emb = embeddings.embed_query(chunk)
    vectors.append({
        "id": str(uuid.uuid4()),
        "values": emb,
        "metadata": {"text": chunk}
    })

# ---- Upload to Pinecone ----
index.upsert(vectors=vectors)
print(f"Successfully uploaded {len(vectors)} chunks to Pinecone.")
