import requests
import PyPDF2
import pyttsx3
text=''
try:

    reader=PyPDF2.PdfReader('The-Alchemist-Paulo-Coelho.pdf')
    for page in reader.pages:
        text += page.extract_text()
    # from_page=reader.pages[13]
    # text+= from_page.extract_text()

except Exception as e:
    print(e)

print(text)

speak=pyttsx3.init()
# speak.save_to_file(text,'alchemist_all.mp4')
speak.say(text)

speak.runAndWait()