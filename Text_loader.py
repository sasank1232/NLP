# !pip install langchain
# !pip install -U langchain-community
#################### Text Loader ##########################################
from langchain.document_loaders import TextLoader
file_path='../Data_files/GenAi.txt'
loader = TextLoader(file_path)
print(loader)
# Load the documents
documents = loader.load()
print(documents)
print("=======================================")
print(documents[0])
print("..................................")
print(documents[0].page_content)
print(documents[0].metadata['source'])
# for doc in documents:
#     print(f"Document Text: {doc.page_content}")