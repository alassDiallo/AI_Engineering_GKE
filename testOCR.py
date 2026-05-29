from easyocr import Reader

reader = Reader(["fr", "en"], gpu=False)
result = reader.readtext("textOCR.png")
full_text = ""

for bblock, text, prob in result:
    print("Confidence: {:.2f}%".format(prob * 100))
    print("Text: {}".format(text))
    full_text += text + " \n"


print(full_text)
