# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:53:50 2022

@author: Alex


Autocomplete Harp template 
"""
from os.path import join 
import shutil

templateFile = join("C:\\Users\\Alex\\Documents\\Repos\\harp-docs\\source\\Devices\\","template_test.rst")

deviceName = input("Enter deviceName:")
print("deviceName is: " + deviceName)

deviceHandle = input("Enter deviceHandle:")
imageSource = "../_static/images/devices/" + deviceHandle + ".png"
deviceHandle = "_ref" + deviceHandle
print("deviceHandle is: " + deviceHandle)

description = input("Enter device description:")

keyFeatures = input("Enter key features:")
keyFeaturesList = keyFeatures.replace("\n","\n- ")
keyFeaturesList = "- " + keyFeaturesList

useCases = input("Enter use cases:")
useCasesList = useCases.replace("\n","\n- ")
useCasesList = "- " + useCasesList

connections = input("Enter connections:")
connectionsList = connections.replace("\n","\n- ")
connectionsList = "- " + connectionsList

softwareLink = input("Enter softwarelink:")

softwareConfig = input("Enter softwareconfig:")
softwareConfigList = softwareConfig.replace("\n","\n- ")
softwareConfigList = "- " + softwareConfigList

filenameOut = deviceHandle + ".rst"
template = templateFile
target = join("C:\\Users\\Alex\\Documents\\Repos\\harp-docs\\source\\Devices\\",filenameOut)

shutil.copyfile(template, target)

fin = open(target, "rt")
data = fin.read()

data = data.replace('_REFDEVICE', deviceHandle)
data = data.replace('DEVICENAME', deviceName)
data = data.replace('IMAGESOURCE', imageSource)
data = data.replace('DESCRIPTION', description)
data = data.replace('KEYFEATURES', keyFeaturesList)
data = data.replace('CONNECTIVITY', connectionsList)
data = data.replace('USECASES', useCasesList)
data = data.replace('SOFTWARELINK', softwareLink)
data = data.replace('SOFTWARECONFIG', softwareConfigList)

fin = open(target, "wt")
fin.write(data)
fin.close()