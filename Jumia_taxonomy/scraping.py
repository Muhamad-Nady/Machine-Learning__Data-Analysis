import requests
from bs4 import BeautifulSoup
import os
main_dir = "/home/muhamad/Downloads/MyWork/SixDays/second project"
#############################################
# Get URL of main subcatories for main product
baseurl = 'https://www.jumia.com.eg/ar/mlp-jumia-global/'
response = requests.get('https://www.jumia.com.eg/ar/sporting-goods/')
soup = BeautifulSoup(response.content, 'html')
productlist = soup.find_all('div', class_="col -df -j-end -fsh0")
productsurl = []
for product in productlist:
    items = product.findChildren('a', href=True)
    for item in items:   
    #for link in item.find('a', href=True):
        item = item['href'].split('/')
        item.insert(3, 'ar')
        item  = '/'.join(item)
        productsurl.append(item)
productsurl.pop()
################################################
"""# Get URL of  subcatories for main product
#for respone in productsurl:
response = requests.get( 'https://www.jumia.com.eg/ar/computers-tablets/')
#if response.status_code == 200:
soup = BeautifulSoup(response.content, 'html')
subproductlist = soup.find_all('h2', class_="-m -upp -fs14 -pvs -phm")
subproductsurl = []
for product in productlist:
    items = product.findChildren('a', href=True)productsurl
    for item in items:   
        subproductsurl.append(item['href'])"""
################################################    
# Extract the catogries and subcatogries

baseurl = 'https://www.jumia.com.eg/ar/mlp-jumia-global/'
productspaths = []
for url in productsurl:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    productcatogry = soup.find('div', class_="brcbs col16 -pvs")
    path = []
    for item in productcatogry:
        elemntpath = str(str(item).split('>')[1][:-len('</a')])
        path.append(elemntpath)            
###########################3
# Saving the images
    path = "/".join(path)
    path = os.path.join(main_dir, path)
    if not os.path.exists(path):
        os.makedirs(path)
     
#############################################
# Getting images URLS 
    products_images = []
    def getdata(url):  
        r = requests.get(url)  
        return r.text  
    htmldata = getdata(url)  
    soup = BeautifulSoup(htmldata, 'html.parser')  
    for item in soup.find_all('img'): 
        products_images.append((item['data-src']))  

    coma = ''
    while True:
        if coma in products_images:
            products_images.remove(coma)
        else:
            break
#############################
# Downloading images from jumia
    for i, url in enumerate(products_images[1:]):    
        response = requests.get(url)
        if response.status_code == 200:
            with open(path+ "/sample" + str(i) + ".jpg", 'wb') as f:
                f.write(response.content)
