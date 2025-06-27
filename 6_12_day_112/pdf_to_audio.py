import requests
import PyPDF2


text=''
try:
    reader=PyPDF2.PdfReader('The-Alchemist-Paulo-Coelho.pdf')
    # for page in reader.pages:
    #     text += page.extract_text()
    from_page=reader.pages[13]
    text+= from_page.extract_text()
except Exception as e:
    print(e)

# print(text)

try:
    from murf import Murf

    client = Murf(
        api_key="ap2_b1716d58-3df7-42a7-811e-41e03cb19ccb",
    )
    response=client.text_to_speech.generate(
        text=text,
        voice_id="en-US-natalie",
    )
    # print("Response Object:", response)

    if hasattr(response, 'audio_file'):
        audio_file = response.audio_file
        print(f"Audio generated successfully: {audio_file}")
    else:
        print("Failed to generate audio. Response:", response)

except Exception as e:
    print(e)