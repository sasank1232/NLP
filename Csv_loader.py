#pip install langchain
#pip install langchain-community

#=================== CSV Loader ===========================================
from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path='../Data_files/winequality_red.csv')
data = loader.load()
#print(data)
# print(type(data))  # list
#print(data[0])    # page meta  row
print(data[0].page_content)
# print(data[0].metadata)
# print(len(data))
#print(data[25479])
