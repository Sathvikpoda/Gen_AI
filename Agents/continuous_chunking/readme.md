📄 Continuous Document Chunking and Embedding Storage

🔍 Overview
This script monitors a folder for new PDF and TXT files, extracts text, splits it into smaller parts (chunks), generates embeddings, and stores them in Chroma DB for efficient retrieval.

⚡ How It Works
Watches a folder for new files.
Extracts text from PDF or TXT files.
Splits text into smaller chunks for better processing.
Generates AI-powered embeddings for each chunk.
Stores embeddings in Chroma DB for fast searching.
Repeats the process every minute to check for new files.
📂 Folder to Monitor
The script monitors this folder:
C:\Users\sathv\Gen-AI\python\Python\Chunking\continuous_cunking

💡 You can change this path in the script if needed.

🔧 Dependencies
Install required libraries before running the script:

pip install pymupdf langchain langchain-community chromadb openai

🚀 How to Run
Simply execute the script in Python, and it will keep running, checking for new files every minute:

python script_name.py
📌 Features
✅ Works with PDF and TXT files
✅ Extracts text accurately
✅ Splits text into meaningful chunks
✅ Uses AI-powered embeddings (OpenAI)
✅ Stores data in Chroma DB for retrieval
✅ Runs continuously to detect new files
💡 Example Output
If a new document is added, the script will process it and output the first two chunks like this:

Processing file: sample.pdf

Chunk 1:
"The quick brown fox jumps over the lazy dog. AI is transforming the world..."

Chunk 2:
"Machine learning models use embeddings to represent text in a meaningful way..."
Then, it stores these embeddings in Chroma DB.

🛑 Stopping the Script
To stop the script, press:

CTRL + C
📌 Notes
If a file is empty or unsupported, it will be skipped.
The script waits 1 minute before checking again for new files.
Chroma DB is used to store vector embeddings for future AI-powered search.