import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diplom.settings")
from denotat.models import Sort
from bs4 import BeautifulSoup
def create_soup():
    soup=BeautifulSoup(open('/home/student/VKR/diplom/denotat.html'))
    x=soup.findAll('div',{'class':'post post_teaser shortcuts_item'})	
    
    return BeautifulSoup(open('/home/student/VKR/diplom/denotat.html')).soup.findAll('div',{'class':'post post_teaser shortcuts_item'})

for div in x:	
	
	d
