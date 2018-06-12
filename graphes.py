import matplotlib.pyplot as plt
import os
import json as js
def loadExperiments():
	settings = {}
	path = "experiments"
	for i in os.listdir(path):
		settings[i] = {}
		settingsFile = open(path+'\\'+i+'\\'+'settings.txt')
		data = settingsFile.read().split()
		with open(path+'\\'+i+'\\'+'new_results') as jf:
			jsondata = js.load(jf)
		index=0
		while (index+2<len(data)):
			settings[i][data[index]] = data[index+2]
			index+=3
		settings[i]['results'] = jsondata
		settingsFile.close()
	return settings


def generatePopulationGraph(type):
	population = {}
	settings = loadExperiments()
	for exp in settings.keys():
		if not int(settings[exp][type]) in population.keys():
			population[int(settings[exp][type])] = {}
		population[int(settings[exp][type])][exp] = []
		population[int(settings[exp][type])][exp].append(settings[exp]['results']['Results']['Noob'][0])
		population[int(settings[exp][type])][exp].append(settings[exp]['results']['Results']['Adept'][0])
		population[int(settings[exp][type])][exp].append(settings[exp]['results']['Results']['Master'][0])
	#print(population)
	fig = plt.subplot(111)
	for x in sorted(population.keys()):
		noob = []
		adept = []
		master = []
		for res in population[x]:
			noob.append(population[x][res][0])
			adept.append(population[x][res][1])
			master.append(population[x][res][2])			
		avg=0
		for i in noob:
			avg+=int(i)
		avg = avg/len(noob)
		fig.bar(str(x)+' noob',avg,color='b',align='center')
		avg=0
		for i in adept:
			avg+=int(i)
		avg = avg/len(adept)
		fig.bar(str(x) + ' adept' ,avg,color='r',align='center')
		avg=0
		for i in master:
			avg+=int(i)
		avg = avg/len(master)
		fig.bar(str(x) + ' master',avg,color='g',align='center')
	plt.show()
	#plt.savefig(type+'fig')
		
def generatePGGraph():
	population = {}
	settings = loadExperiments()
	for exp in settings.keys():
		if not int(settings[exp]['POPULATION_SIZE'])*int(settings[exp]['GENERATIONS']) in population.keys():
			population[int(settings[exp]['POPULATION_SIZE'])*int(settings[exp]['GENERATIONS'])] = {}
		population[int(settings[exp]['POPULATION_SIZE'])*int(settings[exp]['GENERATIONS'])][exp] = []
		population[int(settings[exp]['POPULATION_SIZE'])*int(settings[exp]['GENERATIONS'])][exp].append(settings[exp]['results']['Results']['Noob'][0])
		population[int(settings[exp]['POPULATION_SIZE'])*int(settings[exp]['GENERATIONS'])][exp].append(settings[exp]['results']['Results']['Adept'][0])
		population[int(settings[exp]['POPULATION_SIZE'])*int(settings[exp]['GENERATIONS'])][exp].append(settings[exp]['results']['Results']['Master'][0])
	fig = plt.subplot(111)
	for x in sorted(population.keys()):
		noob = []
		adept = []
		master = []
		for res in population[x]:
			noob.append(population[x][res][0])
			adept.append(population[x][res][1])
			master.append(population[x][res][2])			
		avg=0
		for i in noob:
			avg+=int(i)
		avg = avg/len(noob)
		fig.bar(str(x)+' noob',avg,color='b',align='center')
		avg=0
		for i in adept:
			avg+=int(i)
		avg = avg/len(adept)
		fig.bar(str(x) + ' adept' ,avg,color='r',align='center')
		avg=0
		for i in master:
			avg+=int(i)
		avg = avg/len(master)
		fig.bar(str(x) + ' master',avg,color='g',align='center')
	plt.show()
	#plt.savefig('pmg_graph')
		


generatePopulationGraph('GENERATIONS')
generatePopulationGraph('POPULATION_SIZE')
generatePGGraph()
