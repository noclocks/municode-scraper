import json
import os
from pprint import pprint
import requests
from IPython.display import HTML

from dotenv import load_dotenv

load_dotenv()

subscription_key = "d6167fd070204b4aaeec869538b3279d"
assert subscription_key

search_url = "https://api.bing.microsoft.com/v7.0/search"

search_term = "municode atlanta zoning"

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
# print(json.dumps(search_results, indent=4))

rows = "\n".join(["""<tr>
                       <td><a href=\"{0}\">{1}</a></td>
                       <td>{2}</td>
                     </tr>""".format(v["url"], v["name"], v["snippet"])
                  for v in search_results["webPages"]["value"]])
out = HTML("<table>{0}</table>".format(rows))

# launch in browser
out

# subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
# endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/bing/v7.0/search"

# query = "Municode Atlanta Zoning"

# mkt = 'en-US'
# params = { 'q': query, 'mkt': mkt }
# headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

# # Call the API
# try:
#     response = requests.get(endpoint, headers=headers, params=params)
#     response.raise_for_status()

#     print("\nHeaders:\n")
#     print(response.headers)

#     print("\nJSON Response:\n")
#     pprint(response.json())
# except Exception as ex:
#     raise ex
