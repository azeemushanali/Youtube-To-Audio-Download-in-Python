# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:31:41 2020

@author: Azeemushan
"""
from selenium import webdriver
import requests
import time
import re

def download(dwnld_link):
    '''Without filename'''
    r = requests.get(dwnld_link,allow_redirects = True)
    open('file.mp3','wb').write(r.content)
  
def download2(dwnld_link):
    '''With filename'''
    print("File is being downloaded")
    r = requests.get(dwnld_link,allow_redirects = True)
    filename = driver.find_element_by_id('title').text + '.mp3'
    new_name = re.sub(r'[|]+', "", filename)
    open(new_name,'wb').write(r.content)
    #os.rename('temp.mp3',new_name)
    print("File name - ",filename," has been downloaded")
    


def fetch(url):
    driver.get('https://ytmp3.cc/')
    driver.find_element_by_id('input').send_keys(url)
    driver.find_element_by_id('submit').click()
    time.sleep(20)
    try:
        dwnld_url = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/a[1]').get_attribute('href')
        download2(dwnld_url)
    except Exception as e:
        print(e)

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)


fetch('https://www.youtube.com/watch?v=s-Cu1EDHJZ0')
print('''Enter your choice?
           1- Enter Single link manually - 
           2- Multiple Links from link.txt file''')
inp = input()
if inp == '1':
    link = input("Enter your link here - \n")
    print(link)
elif inp == '2':
    file = open('link.txt','r')
    f1 = file.readlines()
    for i in f1:
        fetch(i)
   
     