#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/markchiang/ChatGPT/blob/main/ChatGPT_API.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[17]:


#get_ipython().system('pip install -q openai')


# In[18]:


import json
import openai
import os


# In[19]:


# Link to the API Key - https://beta.openai.com/docs/quickstart/add-your-api-key
# Replace the api key to your own api key.
openai.api_key = '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'


# In[22]:


messages = [
    # system message first, it helps set the behavior of the assistant
    {"role": "system", "content": "You are a research assistant."},
]


# In[23]:


while True:
    message = input("👨‍⚕️: ")
    if message:
        if message == "q": break
        messages.append(
            {"role": "user", "content": message},
        )
        chatCompletion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chatCompletion.choices[0].message.content
    print(f"🧙: {reply}")
    messages.append({"role": "assistant", "content": reply})

