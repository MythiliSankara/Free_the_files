Mythili Sankara -ns3305- Investigative Techniques- Assignment 2

# Free the Files API 

According to a Propublica report dated December 2012 and titled 'What we learned from the free files', Free the Files campaign in Spring 2011 as an appplication to that provides access to a database on spending by various groups on political ads across four major television channels- ABC, CBS, NBC and FOX. 

The documents provide detailed information on each ad marked by a unique contract id, the gross amount per individual order, the group that bought the ad the targeted swing markets. 

# Authentication and access:

Unlike Propublica’s Campaign Finance API, Free the Files does not require any API key or completion of any form of authentication.

# The API and datasets

The API only allows GET requests. The base url is  https://projects.propublica.org/free-the-files. No form of authentication or key is required. The data is made available in json format and is segregated based on markets, television stations, and committee name. 

# Complete URL Search:

The base url must include two variables, as shown below:

>https://projects.propublica.org/free-the-files/{Object1}.json'

The above URL must include the base URL followed by atleast one of the four objects  (Market, Station, Committee and, Filing) and their respective variables. 

# Understanding the Variables

Everything begins with a committee and the candidate it supported during the 2011 campaign. A quick look at the main page shows the different committees and the gross amount each invested. The object "committee" in the above URL retrieves a list of 1203 committees. The slug is the unique identifier of a committee, which can be used to look for further details. 

Below is the query to retrieve committee names:

> data_type="committees"
> committee_url=f'https://projects.propublica.org/free-the-files/{data_type}.json'
> data = requests.get(committee_url).json()
> for dat in data:
>	 slugs.append(dat['committee']['slug'])
> print(slugs)

The output:

>['planned-parenthood-issue', 'obama-for-america', 'romney-for-president', >'american-crossroads--2', 'restore-our-future', 'crossroads-gps', >'democratic-congressional-campaign-committee', 'democratic-senatorial-campaign-committee', >'national-republican-congressional-committee', 'americans-for-prosperity', >'priorities-usa-action', 'tom-smith-for-senate', 'americans-for-job-security', >'national-republican-senatorial-committee', 'us-chamber-of-commerce', >'warren-for-senate-2012', 'house-majority-pac', 'independence-usa-pac', >'berkley-for-senate', 'american-future-fund', 'republican-national-committee', >'bob-casey-for-senate', 'linda-mcmahon-for-senate-2012', 'nelson-for-senate', >'live-free-pac', 'heller-for-senate', 'republican-jewish-coalition', 'majority-pac', >'menendez-for-senate', 'afscme', 'rnc', 'rnc-romney', 'patriot-majority', >'american-action-network', 'senate-majority-pac', 'congressional-leadership-fund', >'rpof-3-pac', 'citizens-for-josh-mandel', 'wilson-for-nm-senate', 'nh-democratic-party', >'brown-r-senate', 'warren-d-senate', 'sobhani-for-senate', 'mi-energy-mi-jobs', >'freedom-pac', 'protecting-michigan-taxpayers', 'dga-nh-freedom-fund', >'patriot-majority-usa', 'kaine-for-senate-2012', 'flake-for-senate', >'republican-party-of-florida', 'fitzpatrick-for-congress', 'horsford-for-congress', >'linda-mcmahon', 'coffman-for-congress', 'grayson-for-congress', 'friends-of-joe-heck', >'brown-for-senate...

Using any of the above committee name, which are called slugs here, we can query for further details as below:

>slug="kalil-for-judge"
>committee_url=f'https://projects.propublica.org/free-the-files/{data_type}/{slug}.json'
>data = requests.get(committee_url).json()
>print("The gross amount is ",data["committee"]["freed_files"])
>file_dict=data["committee"]["freed_files"][1]
>file_details=file_dict.values()

The most important variable here is ‘freed_files’, which provides the contract number, the filing type and the advertising agency of the committee. There are a few observations to note.
a) The name or the slug gives the name of the committee that has purchased the ads.
b) The advertising agency, which appears as a value in the ‘freed_files’ dictionary is not be confused with the advertiser itself, who is infact the individual/committee that bought the ad.
c) Some filings can have multiple contracts, which is meant to classify the kind of advertisement and agreement the user has signed up for. 

The output:

>dict_values([{'callsign': 'WJXX', 'contract_number': '704418', 'dc_slug': >'432190-collect-files- 11893-political-file-2012-local', 'filing_type': 'Local', >'gross_amount': 100.0, 'id': 12229, 'market_id': 50, 'thumbnail_url': 'https://s3.amazonaws.com/s3.documentcloud.org/documents/432190/pages/collect-files- 11893-political-file-2012-local-p1-thumbnail.gif', 'transcriptions_count': 3, 'upload_date': '2012- 08-09T00:00:00Z', 'url': '/collect/files/11893/Political File/2012/Local/Florida/6262553 AUG 5 AUG 12704418 (13445319161006)_.pdf', 'committee': {'id': 4418, 'name': 'KALIL FOR JUDGE', 'slug': 'kalil-for-judge'}, 'agency': {'name': 'DAIGLE IDEA DEVELOPMENT/POL'}}])

Finally, you can use the 'Market' slug as below to retrieve the number the number of scraped and freed files on ads in each of the 33 swing markets

>slug='new-york'
>url = f'https://projects.propublica.org/free-the-files/{data_type}/{slug}.json'
>data = requests.get(url).json()
>print("The number of files scraped="+str(data["market"]["filings_ct"])+'\n'+"The Market name="+str(data["market"]["name"])+'\n'+"The number of files freed="+str(data["market"]["freed_ct"])+'\n'+"The titleized_name="+str(data["market"]["titleized_name"]))

The output:
>The number of files scraped=475
>The Market name=NEW YORK
>The number of files freed=127
>The titleized_name=New York

# Caveats:
According to a Propublica article, dated October 2012, titled 'Free the Files Frequently Asked Questions', the FCC does not have access to files outside the top 50 television markets. Additionally, the data is cached which may result in errors when one initially runs the given python code.





























   