import requests
import json

file_url = 'https://ef8b-84-54-83-43.ngrok-free.app/api/generate-visit-card/'


data = {
    'name': 'Sherzod',
    'phone': '+9989388991859',
    'email': 'sherzod@example.com',
    'pochta': 'sher@example.com',
    'manzil': 'Yashnabod',
    'name_company': 'sherzodIt',
}

try:

    img_response = requests.post(file_url, json=data)


    if img_response.status_code == 200:

        with open('media/1.jpg', 'wb') as img_file:
            img_file.write(img_response.content)
        print("Image downloaded successfully!")
    else:
        print(f"Failed to retrieve the image. Status code: {img_response.status_code}")
        print(f"Response Content: {img_response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
