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



## Install the library
```
pip install newsi 
```



## Supported-language-and-countries

To get the country and its supported language



```python
from newsi import Supported_language_and_countries
supported_language_and_countries = Supported_language_and_countries()
print(supported_language_and_countries)
```
Response example :
```JSON
  [{
    "United States": [
      {
        "Country code": "us",
        "Language code": "en",
        "Language name": "English"
      }
    ]
  }]
```
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
from newsi import Local
local_news = Local("en","us","top",1,20)
print(local_news)
```
Response example :
```JSON
  [{
    "_id": "93223cd39597de2f77da56f1e6774d53b70bfdc1ef8f13b3377b030f1a47b350",
    "body": "✕ Close Donald Trump indictment - latest news\n\nSign up for the daily Inside Washington email for exclusive US coverage and analysis sent to your inbox Get our free Inside Washington email Please enter a valid email address Please enter a valid email address SIGN UP I would like to be emailed about offers, events and updates from The Independent. Read our privacy notice Thanks for signing up to the\n\nInside Washington email {{ #verifyErrors }} {{ message }} {{ /verifyErrors }} {{ ^verifyErrors }} Something went wrong. Please try again later {{ /verifyErrors }}\n\nDonald Trump has promised to share an “irrefutable” report on his baseless claims of election fraud in Georgia.\n\n“A Large, Complex, Detailed but Irrefutable REPORT on the Presidential Election Fraud which took place in Georgia is almost complete & will be presented by me at a major News Conference at 11.00am on Monday of next week,” Mr Trump said.\n\nThe former president and 18 of his allies have been indicted on a range of criminal charges relating to the former president’s attempts to alter Georgia‘s 2020 election results.\n\nHe described the extensive charge sheet produced by a grand jury in Fulton County as an attempt to stop him from running in next year’s election, saying that the “the witch hunt continues”.\n\nMr Trump has been charged with 13 counts including racketeering, filing false documents, and attempting to coerce public officers to violate their oaths, according to court documents.\n\nIt marks the fourth major indictment against Mr Trump in nearly as many months, and the second related directly to his actions during the 2020 election.\n\nMr Trump has been issued with an arrest warrant and ordered to surrender by 25 August.",
    "hasBody": true,
    "image": "https://lh6.googleusercontent.com/proxy/aO7jtu3L2CrM-dkYuyB1iGTMC0jUXCXfzuPIaWeKCyG0DVwTOpZn42CVkblpl3XqzcYu3ZRbDaiw55plsjYam2tXbvaZI7Lvws9MQIQGZYBmKbLC2X4PKtFLm5MvrQP33zlnyN1ZpoJv8NjW7SnsUksR167lLHwQIKs=s1200",
    "link": "https://www.independent.co.uk/news/world/americas/us-politics/trump-indictment-arrest-warrant-georgia-latest-b2393765.html",
    "publishedAt": "2023-08-16T08:31:32Z",
    "publishedTimestamp": 1692174692,
    "shortLink": "independent.co.uk",
    "sourceName": "The Independent",
    "title": "Trump claims mystery press conference report clears him of Georgia election charges"
  }]
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
from newsi import Category
category_news = Category("world","en","us","top",1,20)
print(category_news)
```
Response example :
```JSON
  [{
    "_id": "6150b1ddc317ba0aab441226b688823ad74226dc5ab3ca1e0918bf1cf9361ce0",
    "body": "Afghanistan's Taliban rulers took over the capital Kabul on August 15, 2021. A Taliban spokesperson denied the group was anti-woman in comments to DW, while the UN has accused it of gender apartheid.\n\nAfghanistan's Taliban rulers on Tuesday celebrated the second anniversary of their return to power.\n\nThe group took over the Afghan capital Kabul on August 15, 2021. The US-backed government collapsed and much of its leadership, including former President Ashraf Ghani, went into exile.\n\nSo far, no country has recognized the Taliban's government in Afghanistan.\n\nTaliban mark 'Independence Day'\n\nTaliban authorities held official events across the country, celebrating what they called \"Afghanistan's Independence day from the US occupation.\"\n\nTaliban celebrate 2nd Anniversary of Afghan takeover To view this video please enable JavaScript, and consider upgrading to a web browser that supports HTML5 video\n\nUS-led forces overthrew the Taliban-led Islamic Emirate of Afghanistan in 2001 and withdrew 20 years later.\n\n\"On the second anniversary of the conquest of Kabul, we would like to congratulate the mujahid (holy warrior) nation of Afghanistan and ask them to thank Almighty Allah for this great victory,\" Taliban spokesman Zabihullah Mujahid said.\n\n\"The conquest of Kabul proved once again that no one can control the proud nation of Afghanistan and guarantee their stay in this country,\" the Taliban government said in a statement.\n\nTaliban spokesperson to DW: 'How can we be against women?'\n\nTaliban spokesperson Suhail Shaheen denied that the de facto rulers of Afghanistan were anti-woman in comments to DW News Asia.\n\n\"How can we be against women?\" he said. \"They are our mothers, wives, daughters, sisters.\"\n\nTaliban authorities have imposed a number of restrictions on women, including enforcing a strict dress code in public, barring them from gyms and parks, and keeping women out of secondary and tertiary education.\n\nShaheen insisted that the Taliban have not denied women the right to education.\n\nHe said that the Taliban would reopen schools and universities to girls and women, but did not provide a timeline for this. \"There is a committee set up to create an Islamic environment for that,\" he said.\n\nShaheen argued that the Islamist group is supporting women's progress by allowing them to study nursing and specialize as doctors.\n\nAfghanistan's Taliban rulers have allowed for the continued existence female medical professionals so that women do not have to be treated by male staff.\n\nThe UN has accused the Taliban of practicing gender apartheid. UN Deputy Secretary-General Amina Mohammed said on Tuesday that Taliban rule has \"upturned\" the lives of Afghan women.\n\n\"It's been two years since the Taliban took over in Afghanistan. Two years that upturned the lives of Afghan women and girls, their rights and futures,\" she said in a statement.\n\nBlinken: No normalization of ties without women's rights\n\nUS Secretary of State Antony Blinken reiterated that continued engagement between Washington and the Taliban was conditional on the group supporting the rights of women.\n\n\"We continue to work to hold the Taliban accountable for the many commitments that it's made and not fulfilled, particularly when it comes to the rights of women and girls,\" Blinken told reporters.\n\nHow are Afghan women coping with Taliban rule? To view this video please enable JavaScript, and consider upgrading to a web browser that supports HTML5 video\n\n\"We've been very clear with the Taliban — and dozens of countries around the world have been very clear — that the path to any more normal relationship between the Taliban and other countries will be blocked unless and until the rights of women and girls among other things are actually supported,\" Blinken said.\n\nBlinken defended Washington's decision to withdraw from Afghanistan, which preceded the Taliban's return to power.\n\n\"The decision to withdraw from Afghanistan was an incredibly difficult one, but also the right one,\" Blinken said. \"We ended America's longest war. For the first time in 20 years, we don't have another generation of young Americans going to fight and die.\"\n\nGerman NGO: Humanitarian situation 'dramatic'\n\nDespite a decrease in fighting, Afghanistan has been grappling with a major humanitarian crisis since the withdrawal of US-led forces and a number of international aid organizations.\n\nThe Asia Regional Director of the German humanitarian NGO Welthungerhilfe, Elke Gottschalk, has described the situation in Afghanistan as \"dramatic.\"\n\nShe said that 17 million people in the country are threatened by hunger and 29 million people are dependent on humanitarian aid. \"You can see this on every street corner,\" she said in remarks to German public broadcaster ARD.\n\nAfghanistan has a total population of around 42 million.\n\nThe country's Taliban rulers imposed a ban on women working in NGOs in 2022, which Gottschalk said brought about additional complications.\n\nShe said that while 20% of Welthungerhilfe employees are women, each of these positions had to be negotiated separately and approved by the Taliban.\n\nThe head of the Kabul office of Caritas International, Stefan Recker, told Deutschlandfunk radio that two women were still working for the organization but were not allowed to work in the office.\n\nRecker said that the situation in the country was desperate and many people wanted to flee. However, he said he was hopeful because of the improved security situation and the decrease in street crime.\n\nsdi/wd (AFP, dpa, AP, Reuters)",
    "hasBody": true,
    "image": "https://lh5.googleusercontent.com/proxy/BQKtDN_LHmMiKqoX_H5IiI72B2Ib43BIMycnPyFdHGJs_X7j-5FW2OI-q-kSOtU-cWbtHLjTIv1pjqUPqlPE-WcaWgHsa54=s1200",
    "link": "https://www.dw.com/en/afghanistan-taliban-celebrate-2-years-since-return-to-power/a-66542834",
    "publishedAt": "2023-08-16T07:57:08Z",
    "publishedTimestamp": 1692172628,
    "shortLink": "dw.com",
    "sourceName": "DW (English)",
    "title": "Afghanistan: Taliban celebrate 2 years since return to power"
  }]
```
---