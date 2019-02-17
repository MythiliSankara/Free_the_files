""""
This script executes API queries to Propublica's Free The Files API

"""
import requests

slugs=[]
data_type="committees"
committee_url=f'https://projects.propublica.org/free-the-files/{data_type}.json'
data = requests.get(committee_url).json()
for dat in data:
	slugs.append(dat['committee']['slug'])
#print(slugs)

"""""
Choose one of the committee slugs and query freed_files which provides details on the contracts, gross amounts and the advertising agency involved.
"""""

slug="kalil-for-judge"
committee_url=f'https://projects.propublica.org/free-the-files/{data_type}/{slug}.json'
data = requests.get(committee_url).json()
#print("The gross amount is ",data["committee"]["freed_files"])
file_dict=data["committee"]["freed_files"][1]
file_details=file_dict.values()
#print(file_dict.values)
#print(data["committee"]["pactrack"],data["committee"]["slug"])


data_type = 'markets'
slug='new-york'
list_markets=[]

url = f'https://projects.propublica.org/free-the-files/{data_type}.json'
data = requests.get(url).json()

""""
From data, choose the slug for related to a particular city
"""

slug='new-york'
url = f'https://projects.propublica.org/free-the-files/{data_type}/{slug}.json'
data = requests.get(url).json()
print("The number of files scraped="+str(data["market"]["filings_ct"])+'\n'+"The Market name="+str(data["market"]["name"])+'\n'+"The number of files freed="+str(data["market"]["freed_ct"])+'\n'+"The titleized_name="+str(data["market"]["titleized_name"]))

