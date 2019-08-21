import datetime
import time
import requests
from bs4 import BeautifulSoup
from pushbullet import PushBullet

# PushBullet API Key and set device

pb = PushBullet("o.abcd........")

phone = pb.devices[1]

# Create sent items list

sent_items = []

def itemsearch():
   
    # Get Freecycle websites (offer only) and create a list of 'href'
    
    links = ['https://groups.freecycle.org/group/KensingtonandChelseaUK/posts/offer','https://groups.freecycle.org/group/WestminsterUK/posts/offerWestminsterUK/posts/offer']

    my_list = []

    for url in links:
        page = BeautifulSoup(requests.get(url).text,'html.parser')
        for link in page.find_all('a', href=True):
            if link['href'] not in my_list:
                my_list.append(link['href'])
            
   # Search my_list for 'the one'
   
    the_one = 'kettle' # <<< WHAT ARE YOU LOOKING FOR (LOWER CASE)
    flength = len(the_one)
    
    for item in my_list:
        for i in range(len(item)): 
            chunk = item[i:i+flength].lower()
            if chunk == the_one:
                if item not in sent_items: # Check item has not been sent previously
                        push = pb.push_note("Check this out!",item, device=phone) # Push to phone
                        sent_items.append(item)
      
    my_list.clear()

    #Frequency of search
    
    time.sleep(1800)

while True:
    itemsearch()