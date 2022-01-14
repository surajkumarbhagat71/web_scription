import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
#step 1: get the HTML

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)




# Step 2: parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')

#print(soup)
#print(soup.prettify)


# get all paragraph form html

#paras = soup.find_all('p')
#print(paras)

#ancar = soup.find_all('a')
#print(ancar)

#get first element html page

#print(soup.find('p'))

print(soup.find('p')['class'])

#find all the elemtns with class lead

#print(soup.find_all("p",class_="lead"))

#get all text form paragraph

#print(soup.find('p').get_text())

#print(soup.get_text())



# link fatch html page

ancar = soup.find_all('a')


for link in ancar:
    print(link.get('href'))



all_link = set()

for link in ancar:
    if(link.get('href') !='#'):
        all_link.add("https://codewithharry.com" + link.get('href'))


for x in all_link:
    print(x)
    
    













