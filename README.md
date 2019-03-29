# Basic Insightly API Scripts

These are a set of files which perform task for the Insighly CRM. So far it includes a basic get organisation data script. But I may add more as time goes. 

## Getting Started

Insert your API Key within the headers of the get_json_data function. To find your API key follow instructions<a href = "https://support.insight.ly/hc/en-us/articles/204864594-Finding-or-resetting-your-API-key">here</a><br /><br />
Regarding basic_get_org_data.py: <br />
'''
<pre><code>     querystring = {"brief":"false","skip": str(offset),"top":"500","count_total":"true"}</code></pre><br />
'''
Here depending on the size of your company, you could change the top and offset values. In the programs initial state it will request 500 records and then skip 500 for the next request you've cycled through all organisations. <br /><br /> 
    Append any KeyNames you would like. To see the json of a basic get organisation list request, navigate to the Insightly API, insert your API key up top, scroll down to Gets a list of Organisations, and click try: https://api.insightly.com/v3.0/Help

### Prerequisites

Python 3.7 




