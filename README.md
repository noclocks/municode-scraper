# Municode Library Web Scraper Bot <img src="docs/assets/logo_municode.png" height="35%" width="35%" align="right">

<!-- BADGES:START -->
[![Automate Changelog](https://github.com/noclocks/municode-scraper/actions/workflows/changelog.yml/badge.svg)](https://github.com/noclocks/municode-scraper/actions/workflows/changelog.yml)
<!-- BADGES:END -->

> [!NOTE]
> The purpose of this repository is to explore and analyze the [Municode Digital Library]() through automation tools using Python and a Selenium Web Driver to extract data associated with zoning ordinances.

## Contents

- [Overview](#overview)
  - [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
  - [Data](#data)
  - [Text Mining](#text-mining)
- [Contributing](#contributing)

## Overview

This repository serves a "bot" and provides a development sandbox to collect, gather, and analyze data extracted from the [Municode Digital Library]() related to property zoning ordinances and their corresponding codes, descriptions, and permitted usages.
Further, once some data has been scraped, one can then progress into performing Natural Language Processing (NLP) analysis and other machine-learning based analytics.

Additionally, the repository aims to make the scraped building codes and additional data publicly accessible as a data product that can be prepared for a machine-based analysis.

The bot's primary task is designed to scrape the Municode Library website for all of the available ordinances and resolutions for a given city, county, or municipality and in turn download the scraped data documents and save them to a local directory.

### Background

All cities in the United States are governed by rules called ordinances and regulations which have been proposed and then adopted by City Council and codified into local laws and ordinances.

The Municode library makes these laws, or municipal codes publicly accessible on its website. As a result, the Municode library is vast and full of data that can tell us more about the past and present as it is consistently updated when new local laws are passed, and the older editions are archived.

The Municode library is a rich source of data that can be used to understand the history and current state of local laws and ordinances. The library is a collection of documents that contain a wealth of information about the laws and regulations that govern cities and counties across the United States.

## Installation

```bash
# No installation instructions yet...
# pip install ...
# docker pull ...
# make ...
```

Dependencies:

See [requirements.txt](requirements.txt):

<details><summary>View Requirements</summary>summary><p>

```python
adal==1.2.7
asttokens==2.4.1
attrs==23.2.0
azure-cognitiveservices-search-websearch==2.0.0
azure-common==1.1.28
azure-core==1.30.0
beautifulsoup4==4.12.3
certifi==2024.2.2
cffi==1.16.0
charset-normalizer==3.3.2
cryptography==42.0.2
decorator==5.1.1
exceptiongroup==1.2.0
executing==2.0.1
h11==0.14.0
idna==3.6
ipython==8.21.0
isodate==0.6.1
jedi==0.19.1
lxml==5.1.0
matplotlib-inline==0.1.6
msrest==0.7.1
msrestazure==0.6.4
numpy==1.26.4
oauthlib==3.2.2
outcome==1.3.0.post0
packaging==23.2
pandas==2.2.0
parso==0.8.3
pexpect==4.9.0
prompt-toolkit==3.0.43
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.21
Pygments==2.17.2
PyJWT==2.8.0
PySocks==1.7.1
python-dateutil==2.8.2
python-dotenv==1.0.1
pytz==2024.1
requests==2.31.0
requests-oauthlib==1.3.1
selenium==4.17.2
six==1.16.0
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.5
stack-data==0.6.3
traitlets==5.14.1
trio==0.24.0
trio-websocket==0.11.1
typing_extensions==4.9.0
tzdata==2024.1
urllib3==2.2.0
wcwidth==0.2.13
webdriver-manager==4.0.1
wsproto==1.2.0
```

</p></summary></details>

## Usage

### Data

The Municode API is a RESTful API that provides access to the Municode database. The Municode database contains a collection of municipal codes from various cities and counties across the United States. The Municode API provides access to the Municode database through a collection of endpoints that allow users to search for and retrieve municipal codes and related information.

### Text Mining

This repository attempts to perform text mining on the Municode library to extract information from the documents and shed light on the state-level and city-level building codes and zoning ordinances. With the extensive data the
Municode library provides, we can use text mining techniques to extract information from the documents and in turn pass that data off to NLP tools such as [NLP Suite]() to determine the sentiment of the documents, etc.

## Code Modifications

The codes can be modified to an extent to scrape data for other municipals and states in the United States. Because the scraping code was written specifically to scrape for the state of Georgia and its municipals, only Municode municipal pages with the same UI and format as the Georgia municipals will be able to be scraped. The majority of municipals in many different states follow the scraping-safe format; however, there exists codes uploaded in pdf format and municipal codes that redirect users to a different site hosting current building codes that cannot be scraped with the current script.

## Contributing



