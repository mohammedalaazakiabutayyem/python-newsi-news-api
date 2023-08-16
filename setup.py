from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'Newsi is Free News API is able to fetch local news and category news in real time.'
LONG_DESCRIPTION = 'Best free news api that provide news in all categories from different sources like google news api, yahoo news api, bing news api, bbc news api , business news api, breaking news api, newsapi python website news: https://newsi-app.com'

# Setting up
setup(
    name="newsi",
    version=VERSION,
    author="Mohammed Alaa Zaki",
    author_email="<mohammedalaazakitayyem@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'news api', 'free news api', 'newsi', 'python free news api', 'rapidapi','news feed api',"google news api","best news api","python news api","python news library","python news package","breaking news api","google news api free","news api for python","news library for python"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
