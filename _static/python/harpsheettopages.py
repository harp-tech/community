# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:32:41 2022

@author: Alex
"""
from os.path import join 

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp

docDir = "C:\\Users\\Alex\\Documents\\Repos\\harp-docs\\source\\Devices\\"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Alex\\Desktop\\harp-352616-f57e1230cd03.json",scope)
client = gspread.authorize(creds)

sheet = client.open("HARP Devices").sheet1   
data = sheet.get_all_records() 
pp(data)


pageTemplateFile = join(docDir,"page_template.rst")
cardTemplateFile = join(docDir,"card_template.rst")


allCardsFile = join(docDir,"allCards.rst")

for count, idevice in enumerate(data):

    finCardTemplate = open(cardTemplateFile, "rt")
    finPageTemplate = open(pageTemplateFile, "rt")

    deviceCard = finCardTemplate.read()
    devicePage = finPageTemplate.read()

    print(data[count].get("deviceName"))
    
    devicePage = devicePage.replace('DEVICENAME', data[count].get("deviceName"))

    devicePage = devicePage.replace('CONNECTIVITY', data[count].get("connections"))

    deviceHandle = data[count].get("deviceHandle")

    devicePage = devicePage.replace('DEVICEHANDLE',deviceHandle)
    
    devicePage = devicePage.replace('KEYFEATURES', data[count].get("keyFeatures"))
    
    devicePage = devicePage.replace('USECASES', data[count].get("useCases"))

    devicePage = devicePage.replace('SOFTWARECONFIG', data[count].get("softwareConfig"))
    
    devicePage = devicePage.replace('SOFTWARELINK', data[count].get("softwareLink"))
    
    devicePage = devicePage.replace('DESCRIPTION', data[count].get("description"))
    
    deviceCard = deviceCard.replace('CARDTEXT', data[count].get("cardText"))
    
    deviceCard = deviceCard.replace('DEVICENAME', data[count].get("deviceName"))
    
    deviceCard = deviceCard.replace('CATEGORY', data[count].get("categories"))
    
    deviceCard = deviceCard.replace('DEVICEHANDLE', deviceHandle)
    
    filenameOut = deviceHandle + ".rst"
    target = join(docDir,filenameOut)

    finPageOut = open(target, "wt")
    finPageOut.write(devicePage)
    finPageOut.close()
    
    finCardsAll = open(allCardsFile, "a")
    finCardsAll.write(deviceCard)
    finCardsAll.close()
    
    


