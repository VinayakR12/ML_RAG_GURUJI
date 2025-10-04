import os
import uuid
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
import markdown2 

# ---- Load env variables ----
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")

# ---- Flask app ----
app = Flask(__name__)

# ---- Pinecone setup ----
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
if INDEX_NAME not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=INDEX_NAME,
        dimension=768,
        metric="cosine",
        spec=pinecone.ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(INDEX_NAME)

# ---- LangChain models ----
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=GOOGLE_API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

# ---- Memory buffer ----
conversation_memory = []

# ---- Helper functions ----
def retrieve_docs(query, top_k=3):
    query_emb = embeddings.embed_query(query)
    results = index.query(vector=query_emb, top_k=top_k, include_metadata=True)
    return [m["metadata"]["text"] for m in results["matches"]]

def ml_teacher_chat(query):
    # Add student question to memory
    conversation_memory.append({"role": "student", "content": query})
    
    # Retrieve context from Pinecone
    context_chunks = retrieve_docs(query)
    context_text = "\n\n".join(context_chunks)

    # Prepare prompt
    system_prompt = (
        "You are Guruji, a friendly and wise Machine Learning teacher. "
        "Only answer questions related to Machine Learning, AI, Deep Learning, or Data Science. "
        "Explain concepts clearly, step by step, as if teaching a student. response in the simple and understandble lanuage. "
        "Use bullets, bold, and no emojis where appropriate. "
        "Do not output raw markdown."
    )

    memory_text = "\n".join([f"{m['role']}: {m['content']}" for m in conversation_memory])
    user_prompt = f"Context:\n{context_text}\n\nConversation:\n{memory_text}\n\nStudent Question:\n{query}"
    final_prompt = f"{system_prompt}\n\n{user_prompt}\n\nAnswer as a teacher to a student."

    # Get response from LLM
    response = llm.invoke(final_prompt)
    answer = response.content.strip()

    # Add Guruji response to memory
    conversation_memory.append({"role": "guruji", "content": answer})

    html_text = markdown2.markdown(answer)
    

    return html_text



# ---- Routes ----
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = ml_teacher_chat(question)
    return jsonify({"answer": answer})

# ---- Run app ----
if __name__ == "__main__":
    app.run(debug=True)

