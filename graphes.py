import matplotlib.pyplot as plt
import os
path = "experiments"

for i in os.listdir(path):
	settingsFile = open(path+'\\'+i+'\\'+'settings.txt')
	data = settingsFile.read().split()
	for _ in range(len(data)):
		if data[_] == 'POPULATION_SIZE' and data[_+2] == '200':
			print ('+1')
		
	settingsFile.close()
	#print (data)