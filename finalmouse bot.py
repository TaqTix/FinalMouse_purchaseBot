# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:40:38 2019

@author: TsGh
"""
#  https://www.finalmouse.com/cart/add?id= 

import requests
import json
from selenium import webdriver
import time
import smtplib, ssl

def availabilityCheck():
    r = requests.get('https://finalmouse.com/products.json')
    products = json.loads((r.text))['products']
    
    for product in products:
        #print(product)
        #print(product['title'])
        productname = product['title']
        
        if productname == 'Ultralight 2 - Cape Town':
            print(productname)
            
            productUrl = 'https://finalmouse.com/products/' + product['handle']
            print(productUrl)
            return productUrl
        
    return False
driver = webdriver.Chrome(executable_path=r'C:\Users\akrus\Downloads\chromedriver_win32\chromedriver.exe')  
cont = False
while cont == False:        
        
    driver.get('https://finalmouse.com/products/ultralight-2-cape-town')
    purchaseBtn = driver.find_element_by_xpath('//button[@class="btn product-single__cart-submit btn--secondary"]')
    
    if purchaseBtn.is_enabled() == False:
        print("not yet available")
        time.sleep(10)
        driver.refresh()
    else:
        cont = True;
        print("ready to purchase")

#print(purchaseBtn)
#available = purchaseBtn.is_enabled()

port = 465; #ssl port
smtp_server = "smtp.gmail.com"
sender_email = 'acrypto91@gmail.com'
receiver_email = '4803359226@vtext.com'
password = 'rhfqwhmkdrklxnhv'
message = """\
Subject: Final Mouse is AVAILABLE!

head over to finalmouse.com to purchase the new Ultralight 2 cape-town mouse"""

context = ssl.create_default_context() 
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("acrypto91@gmail.com", password)
    #send email now
    server.sendmail(sender_email, receiver_email, message)
    server.close()
driver.close()



#if we get here, the purchaseBtn has been clicked, now time to enter our shipping information
#driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('acrypto91@gmail.com')





#while driver.find_element_by_xpath('//button[@class="btn product-single__cart-submit"]').click == False:
 #   time.sleep(10)   
  #  if driver.find_element_by_xpath('//button[@class="btn product-single__cart-submit"]').click == True:
   #     print('ready for purchase')
        



