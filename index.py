import requests
from bs4 import BeautifulSoup
import time


########################## GOOGLE TRADUCTION #############################
view='home'
myOperations='translate'
langueDepart = 'fr'
tranduireEn='ht'
text_a_tranduire='bonjour'
base_url='https://translate.google.com/'
final_url ="https://translate.google.com/#view=home&op=translate&sl="+langueDepart+"&tl="+tranduireEn+"&text="+text_a_tranduire+""

video_recherche ='black m'

lien_video ="https://www.google.com/search?tbm=vid&biw=&bih=&q="+video_recherche+"&oq="+video_recherche+""

print("url final =>",final_url)

class_body='displaying-homepage with-sl-list with-lang-list'
response=requests.get(final_url)
    
if response.status_code==200:
        
    html_soup=BeautifulSoup(response.text,'html.parser')
    body =html_soup.findAll('body')
    print(body)
    print(html_soup.find(text_a_tranduire))
    # my_div=html_soup.find('div',attrs={'class':"homepage-content-wrap"})
        
    # print(my_div)
        
else:
    print("Error",response.status_code)

