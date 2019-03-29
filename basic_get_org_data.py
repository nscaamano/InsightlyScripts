import requests,json


def get_json_data(offset):
    url = "https://api.insightly.com/v3.0/Organisations"

    querystring = {"brief":"false","skip": str(offset),"top":"500","count_total":"true"}

    payload = ""
    headers = {
        'Authorization': "Basic [API_KEY]",
        'cache-control': "no-cache",
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return json.loads(response.text)

#append any dictionary item you want. Usi API to see KeyNames
def get_object_data(obj):
    data = []
    data.append(obj['ORGANISATION_ID'])
    data.append(obj['ORGANISATION_NAME'])
    data.append(obj['CUSTOMFIELDS'])
    return data

def main(): 
    json_data = get_json_data(0)
    offset = 500
    insightly_count = len(json_data)
    while json_data != []:
        for obj in json_data:
            data = get_object_data(obj)
            #do stuff with data here
        json_data = get_json_data(offset)
        offset += 500
        insightly_count += len(json_data)
    
            
   
if __name__ == "__main__":
    main()
