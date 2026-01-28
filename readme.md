# AI Customer Support Agent

## 📌 Project Overview
This project is an AI-based Customer Support Agent that automatically
analyzes customer tickets and suggests appropriate responses.
The system learns from previous tickets using Natural Language Processing (NLP).

This project is developed as an academic AI mini-project.

---

## 🎯 Objectives
- Classify customer support tickets
- Suggest responses based on past interactions
- Demonstrate real AI logic (not hard-coded responses)
- Provide a simple interface for testing

---

## ⚙️ Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Streamlit (for UI)

---

## 🧠 How the AI Works
1. Past tickets are stored in a CSV file
2. Text is converted into numerical vectors using TF-IDF
3. Cosine similarity is used to find the most similar past ticket
4. The system predicts the category and response based on similarity

This allows the system to improve as more data is added.

---

## 📁 Project Structure
