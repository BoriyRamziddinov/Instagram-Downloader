def tiktok_downloader(link):
    import requests
    import json
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "404a638f2dmshe97f76ebb87f624p110c9ajsna0ce964ea409",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    return {"video": rest['video'][0],"music": rest['music'][0]}

