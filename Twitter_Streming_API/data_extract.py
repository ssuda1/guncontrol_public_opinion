import re
import json
from ast import literal_eval
import pandas as pd

list = []
with open('twtgun3.24.2.txt') as fhand:
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

#for item in list:
    #print(item['text'])   #debug the diblications of values in dictionary

#convert the list into json format

list2 =[]
for item in list:
    x = json.dumps(item)  #replace single quote by double quote
    x = literal_eval(item)   #convert string to dictionary
    list2.append(x)

#print(type(list2[0])) #list2 is 'list' of 'dictionary'
#print(list2[:4])

df = pd.DataFrame(list2, columns=['created_at','location','time_zone','text','full_text']) #convert dictionary to dataframe
print(df.loc[:5,])
