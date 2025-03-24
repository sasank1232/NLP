# !pip install langchain
# !pip install -U langchain-community
# !pip install pypdf
from langchain.document_loaders import PyPDFLoader

file_path = '../Data_files/budget_speech.pdf'
loader = PyPDFLoader(file_path)
    
# Load the PDF documents
documents = loader.load()
print(len(documents))
for doc in documents:
    print(f"Page {doc.metadata['page']} Text: {doc.page_content}")
