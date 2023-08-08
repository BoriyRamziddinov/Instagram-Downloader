import requests
import json

def insta_downloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "404a638f2dmshe97f76ebb87f624p110c9ajsna0ce964ea409",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    dict = {}
    if 'error' in rest:
        return 'Пока что эта ссылка не работает'
    else:
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Пока что эта ссылка не работает'

print(insta_downloader('https://www.instagram.com/p/BwKhp8TlyCC/'))


