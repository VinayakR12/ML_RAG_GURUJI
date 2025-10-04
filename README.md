# 🌟 GURUJI - AI-Powered ML Teacher
---
<div class="my-3 text-center">
    <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge" alt="Python Badge">
    <img src="https://img.shields.io/badge/Flask-v2.3-lightgrey?style=for-the-badge" alt="Flask Badge">
    <img src="https://img.shields.io/badge/LangChain-v1.0-purple?style=for-the-badge" alt="LangChain Badge">
    <img src="https://img.shields.io/badge/Pinecone-VectorDB-green?style=for-the-badge" alt="Pinecone Badge">
    <img src="https://img.shields.io/badge/RAG-Retrieval_+_Generation-orange?style=for-the-badge" alt="RAG Badge">
    <img src="https://img.shields.io/badge/Embeddings-GoogleAI-lightblue?style=for-the-badge" alt="Embeddings Badge">
    <!-- HTML5 Badge -->
<img src="https://img.shields.io/badge/HTML5-v5.0-orange?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge">

<!-- CSS3 Badge -->
<img src="https://img.shields.io/badge/CSS3-v3.0-blue?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3 Badge">

<!-- Bootstrap Badge -->
<img src="https://img.shields.io/badge/Bootstrap-v5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap Badge">

<!-- JavaScript Badge -->
<img src="https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript Badge">
</div>

---

## 🚀 Project Overview

**GURUJI** is an **intelligent AI chatbot** that helps learners master **Machine Learning (ML) concepts, algorithms, and applications**.  

It combines the power of **RAG (Retrieval-Augmented Generation)**, **LLMs (Large Language Models)**, and **LangChain pipelines** to provide **accurate, context-aware, and interactive answers** from uploaded documents.  

> "Learn ML the smart way — ask Guruji and get precise, reliable guidance instantly!"  

---
## 🖼️ Result

Here’s an example of GURUJI in action:

<p align="center">
  <img src="/Output/result.png" alt="GURUJI Chatbot Output" width="600"/>
</p>

> **Figure:** GURUJI providing context-aware ML guidance using RAG + LangChain + LLM.

---


## 📌 Core Concepts

### 1️⃣ **RAG - Retrieval-Augmented Generation**

**RAG** is a cutting-edge technique that **retrieves relevant information** and **augments LLM generation** for precise responses:

- Retrieves relevant text chunks from a **knowledge base** or documents.  
- Feeds the retrieved context into an **LLM** for intelligent answer generation.  
- Produces **highly accurate, grounded responses** rather than generic answers.  

**✨ Benefits of RAG:**

- Reduces hallucinations by grounding answers in real content.  
- Works seamlessly with **PDFs, CSVs, DOCX, JSON**, and other formats.  
- Efficient for **large-scale knowledge bases**.

---

### 2️⃣ **LangChain - Orchestrating Intelligence**

**LangChain** is a Python framework for building **LLM-powered applications** with smooth pipelines:

- Automates **document splitting, embedding, retrieval, and prompt management**.  
- Connects the **RAG workflow** from vector search to LLM generation.  
- Simplifies building **AI chatbots, question-answering systems, and virtual assistants**.  

**In GURUJI:**

- LangChain retrieves **contextual chunks** from the **Pinecone vector database**.  
- Feeds this context to the **LLM** for generating accurate responses.  
- Ensures a **seamless and intelligent conversation experience**.

---

### 3️⃣ **LLM - Large Language Models**

**LLMs** are AI models trained on massive datasets to **understand and generate human-like language**:

- Interpret retrieved context and **produce clear, conversational answers**.  
- Examples include **GPT, Google Gemini**, and other generative AI models.  

**Why LLMs are crucial for GURUJI:**

- Summarize, explain, and teach ML concepts effectively.  
- Adapt responses to **question complexity and context**.  
- Provide **interactive, natural language feedback**.

---

## 🛠️ Technologies Used

| Component               | Technology / Tool |
|-------------------------|-----------------|
| **Vector Database**      | Pinecone (Serverless, fast semantic search) |
| **Embeddings**           | Google Generative AI Embeddings (text-embedding-004) |
| **Document Processing**  | PyMuPDF (PDFs), python-docx (Word), pandas (CSV/JSON) |
| **Frontend UI**          | Tailwind CSS + Bootstrap (modern, responsive chat interface) |
| **Backend & Orchestration** | Python, LangChain, FastAPI/Flask |

---

## 🏗️ How GURUJI Works

1. Users **upload documents** to the `data/` folder.  
2. A Python script **extracts text**, splits it into **chunks**, and generates **embeddings**.  
3. Chunks are stored in **Pinecone vector database**.  
4. When a user asks a question, **LangChain retrieves relevant chunks**.  
5. **LLM generates context-aware answers** using retrieved content.  
6. Answers are displayed in a **modern, interactive chatbot UI**.

---

## ⚡ Key Features

- Supports **multi-format document ingestion** (`.txt`, `.csv`, `.json`, `.docx`, `.pdf`).  
- Automatic **chunking** for efficient embeddings.  
- **Semantic search** powered by Pinecone.  
- **RAG + LLM** ensures **accurate, context-rich answers**.  
- Modern, responsive UI with **typing animations**, **gradient chat bubbles**, and **interactive design**.

---
## 🛣️ Roadmap / Future Enhancements

- Multi-turn **conversation memory** with LangChain.  
- Real-time **document updates** and embeddings refresh.  
- **Voice input/output** integration for interactive learning.  
- Advanced **analytics dashboard** for usage metrics.  
- Public **web deployment** for interactive online access.
---
<p align="center">
<strong> Empowering AI-driven learning, one question at a time!</strong>
</p>
