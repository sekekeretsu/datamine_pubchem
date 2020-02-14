import requests
from bs4 import BeautifulSoup
page=requests.get("https://www.ebi.ac.uk/merops/cgi-bin/smi_index")
#page=requests.get("https://www.twilio.com/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup")
#page.content
#print(page.content)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
#f=open("outpur.txt","w+")
#f.write(soup.prettify())
#f.close()
#html=list(soup.children)[]
#print(list(html.children))
print(soup.get_text())
f=open("outpur.txt","w+")
f.write(soup.get_text())
f.close()

