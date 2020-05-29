#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:38:48 2020

@author: a975193
"""

import requests

url = "https://drive.google.com/uc?id=1wqpmLlWht7Ihs1mH2WQnLdKxoSj6c8SN&export=download"

print("Downloading model! Please wait ...")
r = requests.get(url, allow_redirects = True)
with open("saved_model.pb","wb") as file:
    file.write(r.content)
print("Download successful")