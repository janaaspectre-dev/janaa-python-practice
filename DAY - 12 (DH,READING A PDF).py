from pypdf import PdfReader

a = PdfReader("path of pdf","r")
print(len(a.pages))
print(a.pages[0].extract_text())
