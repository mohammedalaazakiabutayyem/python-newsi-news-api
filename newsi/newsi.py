import requests

def Category(category,language,country,sort="top",page=1,limit=20):

    url = "https://newsi-app.com/api/category"

    querystring = {"category": category, "language": language, "country": country, "sort": sort, "page": page, "limit": limit}


    response = requests.get(url, params=querystring)

    return response.json()

def Local(language,country,sort="top",page=1,limit=20):

    url = "https://newsi-app.com/api/local"

    querystring = {"language": language, "country": country, "sort": sort, "page": page, "limit": limit}


    response = requests.get(url, params=querystring)

    return response.json()

def Supported_language_and_countries():
    url = "https://newsi-app.com/api/Supported-language-and-countries"
    response = requests.get(url)
    return response.json()

