import requests
from bs4 import BeautifulSoup


livre_recherche="python"

url="https://www.google.com/search?tbm=bks&q="+livre_recherche+"&oq="+livre_recherche+""

print("url du get ",url)

try:
    reponse = requests.get(url)
    if reponse.status_code==200:
        html_soup=BeautifulSoup(reponse.text,'html.parser')
        all_div =html_soup.findAll('div',attrs={'class':'srg'})
        
        print(all_div)
except:
    print("Error in the get request ")