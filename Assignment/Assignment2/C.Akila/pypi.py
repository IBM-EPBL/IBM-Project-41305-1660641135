import camelcase
from jinja2 import Template
import requests
from flask import Flask 
import datetime 
import numpy as np

 #numpy 
arr = np.array([1, 2, 3, 4, 5])
print(" NUMPY ")
print(arr) 
print(type(arr)) 
print("\n")

 #datetutil 
print(" DATEUTIL ")
now = datetime.date.today()
print(now) 
print("\n") 




#requests
r = requests.get('https://api.spotify.com/')
r.status_code
print(" REQUESTS ")
print(r.headers) 
print("\n") 

#jinja2 
template = """hostname {{ hostname }}"""
data = {"hostname": "core-sw-waw-01"}
j2_template = Template(template) 
print(" JINJA2 ")
print(j2_template.render(data)) 
print("\n")

 #camelcase 
c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(" CAMELCASE ")
print(c.hump(txt)) 
print("\n")

