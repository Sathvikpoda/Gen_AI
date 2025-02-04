🔍 Overview
This script monitors a folder for new PDF, TXT, and DOCX files, extracts text, splits it into smaller parts (chunks), generates AI-powered embeddings, and stores them in Chroma DB for efficient searching.

⚡ How It Works
Watches a folder for new or updated files.
Extracts text from PDF, TXT, and Word (DOCX) files.
Splits text into smaller chunks to make it easier to process.
Generates AI-powered embeddings using OpenAI.
Stores embeddings in Chroma DB for easy searching.
Repeats the process every minute to check for new or modified files.

📂 Folder to Monitor
The script monitors this folder:
C:\Users\sathv\Gen-AI\python\Python\Chunking\continuous_cunking

💡 You can change this folder path in the script if needed.

🔧 Requirements
Before running the script, you need to install the required Python libraries.

Run this command:
pip install pymupdf langchain langchain-community chromadb openai python-dotenv python-docx

🚀 How to Run
Make sure you have Python installed on your system.
Set your OpenAI API Key inside a .env file like this:
OPENAI_API_KEY=your_api_key_here

Open a terminal or command prompt and run the script:
python script_name.py

The script will keep running and checking for new files automatically.
📌 Features
✅ Works with PDF, TXT, and Word files
✅ Extracts text from documents automatically
✅ Splits text into smaller parts for better processing
✅ Uses OpenAI embeddings for AI-powered search
✅ Stores data in Chroma DB for fast retrieval
✅ Continuously runs to detect new or modified files


📌 Example Output
When a new document is added, the script will process it and display the first two chunks:
Processing file: sample.pdf

Chunk 1:
"The quick brown fox jumps over the lazy dog. AI is transforming the world..."

Chunk 2:
"Machine learning models use embeddings to represent text in a meaningful way..."
Then, it stores these embeddings in Chroma DB.

🛑 How to Stop the Script
If you want to stop the script, press:
CTRL + C


📌 Notes
If a file is empty or unsupported, it will be skipped.
The script waits 1 minute before checking for new files again.
Chroma DB is used to store vector embeddings for fast retrieval.
The script only processes files that are new or modified.
