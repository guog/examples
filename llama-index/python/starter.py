from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# from llama_index.readers.file import (
#   DocxReader,
#   HWPReader,
#   PDFReader,
#   EpubReader,
#   FlatReader,
#   HTMLTagReader,
#   ImageCaptionReader,
#   ImageReader,
#   ImageVisionLLMReader,
#   IPYNBReader,
#   MarkdownReader,
#   MboxReader,
#   PptxReader,
#   PandasCSVReader,
#   VideoAudioReader,
#   UnstructuredReader,
#   PyMuPDFReader,
#   ImageTabularChartReader,
#   XMLReader,
#   PagedCSVReader,
#   CSVReader,
#   RTFReader,
# )


# parser = OfficeReader()
# file_extractor = {".xls": parser}
documents = SimpleDirectoryReader("./data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3.2", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
    show_progress=True
)

query_engine = index.as_query_engine()
response = query_engine.query("北京市2022年度商品房销售面积是多少?")
print(response)
