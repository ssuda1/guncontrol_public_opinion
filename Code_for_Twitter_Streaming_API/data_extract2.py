import re
import json
import pandas as pd

#create the list of dictinary formatted strings by extracting data item
#from twitter API scrape
list = []
with open('twtgun3.24.1.txt') as fhand:
    for item in fhand:
        dic = {}
        x = re.findall("^{'created_at': \'(.*?)\'", item)
        if len(x) > 0:
            dic["created_at"] = str(x[0])
        else:
            dic["created_at"] = None
        y = re.findall("{'full_text': \'(.*?)\'", item)
        if len(y) > 0:
            dic["full_text"] = str(y[0])
        else:
            dic["full_text"] = None
        z = re.findall(" 'text': \'(.*?)\'", item)
        if len(z) > 0:
            dic["text"] = str(z[0])
        else:
            dic["text"] = None
        a = re.findall("\'location\': \'(.*?)\'", item)
        if len(a) > 0:
            dic["location"] = str(a[0])
        else:
            dic["location"] = None
        b = re.findall("\'time_zone\': \'(.*?)\'", item)
        if len(b) > 0:
            dic["time_zone"] = str(b[0])
        else:
            dic["time_zone"] = None
        list.append(dic)

fhand.close()

#convert the list (json formattd) into json object

with open('data.json', 'w') as fp:
    json.dump(list, fp)

# convert json file into pandas DataFrame

df = pd.read_json('data.json')

df.to_csv('data.csv', index = False)
