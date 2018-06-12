import matplotlib.pyplot as plt
import os
import json as js
path = "experiments"

for i in os.listdir(path):
	elitism = False
	settingsFile = open(path+'\\'+i+'\\'+'settings.txt')
	data = settingsFile.read().split()
		
	settingsFile.close()
	#print (data)