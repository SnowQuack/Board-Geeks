from sheets import prod
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import requests
import pytz
import os

def print_progress_bar(iteration, total, prefix="", suffix="", length=30, fill="=", head=">", track="."):
    filled_length = int(length * iteration // total)
    if filled_length == 0:
        bar = track * length
    elif filled_length == 1:
        bar = head + track * (length - 1)
    elif filled_length == length:
        bar = fill * filled_length
    else:
        bar = fill * (filled_length-1) + ">" + "." * (length-filled_length)
    print("\r" + prefix + "[" + bar + "] " + str(iteration) + "/" + str(total), suffix, end = "\r")
    if iteration == total: 
        print()

#################GAMEOLOGY################################
##########################################################
for index,link in enumerate(prod.col_values(11)[1:]):
    print(index,link)
    if link != '':
        response = requests.get(link)
        soup = BeautifulSoup(response.text,'lxml')
        print_progress_bar(index+1,prod.col_count)
        price = soup.find('span', attrs={
            'class':'price'
        })
        if price != None: prod.update_acell("G{}".format(index+2),price.string)

################Games Empire##############################
##########################################################

for index,link in enumerate(prod.col_values(12)[1:]):
    if link != '':
        response = requests.get(link)
        soup = BeautifulSoup(response.text,'lxml')
        print_progress_bar(index,prod.col_count)
        price = soup.find('div', attrs={
            'class':'price--main'
        })
        if price != None: prod.update_acell("H{}".format(index+2),price.find('span',class_='money').string.strip())


################Gamesmen##################################
##########################################################

for index,link in enumerate(prod.col_values(13)[1:]):
    if link != '':
        response = requests.get(link)
        soup = BeautifulSoup(response.text,'lxml')
        print_progress_bar(index,prod.col_count)
        price = soup.find('span', attrs={
            'class':'price'
        })
        if price != None: prod.update_acell("I{}".format(index+2),price.string)    

################Advent Games##############################
##########################################################

for index,link in enumerate(prod.col_values(14)[1:]):
    if link != '':
        print(index,link)
        response = requests.get(link)
        soup = BeautifulSoup(response.text,'lxml')
        print_progress_bar(index,prod.col_count)
        price = soup.find('div', attrs={
            'class':'our-price'
        })
        if price != None: prod.update_acell("J{}".format(index+2),('$' + price.find('meta')['content']))    