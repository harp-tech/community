# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 17:32:41 2022

@author: Alex
"""
#%% import 

from os.path import join 

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#%% set file and folder locations 

docDir = "C:\\Users\\Alex\\Documents\\Repos\\harp-docs\\source\\Devices\\"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Alex\\Desktop\\harp-352616-f57e1230cd03.json",scope)

#%% collect device data from google sheet 

client = gspread.authorize(creds)

devicesheet = client.open("HARP Devices").sheet1  
devicedata = devicesheet.get_all_records() 

#%% create output files 

pageTemplateFile = join(docDir,"page_template.rst")
cardTemplateFile = join(docDir,"card_template.rst")


#%% clear allcards.rst

allCardsFile = join(docDir,"allCards.rst")

finCardsAll = open(allCardsFile, "w")
finCardsAll.write("")
finCardsAll.close()

#%% replace device card template values with extracted device data from sheet 

for count, idevice in enumerate(devicedata):

    finCardTemplate = open(cardTemplateFile, "rt")
    finPageTemplate = open(pageTemplateFile, "rt")

    deviceCard = finCardTemplate.read()
    devicePage = finPageTemplate.read()

    print(devicedata[count].get("deviceName"))
    
    devicePage = devicePage.replace('DEVICENAME', devicedata[count].get("deviceName"))

    devicePage = devicePage.replace('CONNECTIVITY', devicedata[count].get("connections"))

    deviceHandle = devicedata[count].get("deviceHandle")

    devicePage = devicePage.replace('DEVICEHANDLE', "alldevices\\" + deviceHandle)
    
    devicePage = devicePage.replace('REFDEVICE',deviceHandle)
    
    devicePage = devicePage.replace('KEYFEATURES', devicedata[count].get("keyFeatures"))
    
    devicePage = devicePage.replace('USECASES', devicedata[count].get("useCases"))

    devicePage = devicePage.replace('SOFTWARECONFIG', devicedata[count].get("softwareConfig"))
    
    devicePage = devicePage.replace('SOFTWARELINK', devicedata[count].get("softwareLink"))
    
    devicePage = devicePage.replace('DESCRIPTION', devicedata[count].get("description"))
    
    deviceCard = deviceCard.replace('CARDTEXT', devicedata[count].get("cardText"))
    
    deviceCard = deviceCard.replace('DEVICENAME', devicedata[count].get("deviceName"))
    
    deviceCard = deviceCard.replace('CATEGORY', devicedata[count].get("categories"))
    
    deviceCard = deviceCard.replace('DEVICEHANDLE', deviceHandle)
    
    filenameOut = "alldevices\\" + deviceHandle + ".rst"
    target = join(docDir,filenameOut)

    finPageOut = open(target, "wt")
    finPageOut.write(devicePage)
    finPageOut.close()
    
    finCardsAll = open(allCardsFile, "a")
    finCardsAll.write(deviceCard)
    finCardsAll.close()

#%% generate table of common device registers 




