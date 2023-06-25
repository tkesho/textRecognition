from google.cloud import vision
import io

def extract_text(image_path):
    client = vision.ImageAnnotatorClient.from_service_account_json(r'C:\Users\dtkes\Downloads\CNN_AlphabetRecognition-master\grab text\secret-lambda-390612-5d20899e8bad.json')

    
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if texts:
        extracted_text = texts[0].description
        return extracted_text
    else:
        return None



image_path = r'C:\Users\dtkes\Desktop\grab text\testIMG.jpg'
extracted_text = extract_text(image_path)
print(extracted_text)