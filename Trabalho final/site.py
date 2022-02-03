import os, requests
from bs4 import BeautifulSoup

url = requests.get("https://seade.gov.br/coronavirus/")
html = url.content

site = BeautifulSoup(html, "html.parser") 

print(site.prettify())

os.system("pause")