import pymupdf4llm

# loader = MarkItDown()
# text_loader = loader.convert("CV-AD-N.pdf")
# print(text_loader.text_content)
text_loader = pymupdf4llm.to_markdown("CV-AD-N.pdf")
print(text_loader)
