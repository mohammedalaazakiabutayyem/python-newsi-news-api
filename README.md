# python-newsi-news-api

## Overview


Free News library for python is able to fetch local news and category news in real time.

Please email mohammedalaazakitayyem@gmail.com if you find any bugs.
This api works by : [Newsi](https://newsi-app.com)

## The News api

This news API supports local news and category news.

1. Top Headlines news
2. Local news
3. World news
4. business news
5. sports news
6. world news
7. politics news
8. technology news
9. entertainment news
10. science news



## Supported-language-and-countries
```
pip install newsi 
```



## Supported-language-and-countries

To get the country and its supported language

```python

```
newsi.
---



## Local news

Make a get request specifying the local of news you want

Field | Description
------|------------
language | The 2-letter ISO-639-1 code of the language you want to get headlines for. example: ```ar``` ```en``` ```es``` ```fr``` ```he``` .....
country | Find sources that display news in a specific country. Possible options: .```eg``` ```us``` ```es``` ```fr``` ```in``` .....
sort | The order to sort the articles in :<br/>```top``` = Fetch the top news.<br/>```last``` = Fetch the latest news.
page | Use this to page through the results.
limit | Use this to customize the number of stories per page <br/>```default``` = 20<br/> ```Max``` = 100

```python

```

---




## Category news

Make a get request specifying the Category of news you want

Field | Description
------|------------
category | The category you want to get new for. Possible options:```sport``` ```world``` ```business``` ```science_and_technology``` ```education``` ```entertainment``` ```health``` ```travel```.
language | The 2-letter ISO-639-1 code of the language you want to get headlines for. example: ```ar``` ```en``` ```es``` ```fr``` ```he``` .....
country | Find sources that display news in a specific country. Possible options: .```eg``` ```us``` ```es``` ```fr``` ```in``` .....
sort | The order to sort the articles in :<br/>```top``` = Fetch the top news.<br/>```last``` = Fetch the latest news.
page | Use this to page through the results.


```python

```

---