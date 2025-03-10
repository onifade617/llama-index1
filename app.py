from llama_index.core import Document

#text = "The quick brown fox jumps over the lazy dog."

#doc = Document(
    #text=text,
    #metadata= {'author': 'John Doe','category': 'others'},
    #id_ = '1'
#)
#print(doc)

'''
from llama_index.readers.wikipedia import WikipediaReader

loader = WikipediaReader()

documents = loader.load_data(
 pages=['Pythagorean theorem','General relativity', 'Lagos']
)

print(f"loaded {len(documents)} documents")

'''


'''
from llama_index.core import Document
from llama_index.core.schema import TextNode

doc = Document(text="This is a sample document text")
n1 = TextNode(text=doc.text[0:16], doc_id=doc.id_)
n2 = TextNode(text=doc.text[17:30], doc_id=doc.id_)

print(n1)
print(n2)
'''

from llama_index.core import Document
from llama_index.core.node_parser import TokenTextSplitter
doc = Document(
 text=(
 "This is sentence 1. This is sentence 2. "
 "Sentence 3 here."
 ),
 metadata={"author": "John Smith"}
)
splitter = TokenTextSplitter(
 chunk_size=12,
 chunk_overlap=0,
 separator=" "
)
nodes = splitter.get_nodes_from_documents([doc])
for node in nodes:
 print(node.text)
 print(node.metadata)