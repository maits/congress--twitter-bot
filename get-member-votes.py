# coding: utf-8

# In[1]:

import requests
import json


# ## set api header

# In[2]:

headers = {
    'X-API-Key': 'xQmZXjwTFWC6v0xk9SJB4ZqIKVyvy7bsSoqNcGQA',
}


# ## make api call to get delegation (with requests)

# In[3]:

senate_resp = requests.get('https://api.propublica.org/congress/v1/members/senate/WV/current.json', headers=headers)
house_resp = requests.get('https://api.propublica.org/congress/v1/members/house/WV/current.json', headers=headers)


# ## set list of all members w all data

# In[4]:

all_members_list = json.loads(senate_resp.text)["results"] + json.loads(house_resp.text)["results"]


# ## function to extract data we want

# In[5]:

member_data = []

def get_member_data(member_list):
    for member in member_list:
        d = {}
        d["twitter_id"] = member["twitter_id"]
        d["party"] = member["party"]
        d["id"] = member["id"]
        d["role"] = member["role"]
        d["name"] = member["name"]
        member_data.append(d)
        
get_member_data(all_members_list)


# In[6]:

member_data


# In[ ]:



