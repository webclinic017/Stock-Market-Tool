
import readXlsx
import glob
#import TestCalculations
import Reported
import json
import inspect
import Calcs
import doCalcs
import os
import boundings


def decorateReadingFile(path, fileName):
	myfile = open(fileName, "r+")
	contents = myfile.read()        
	contents = contents.replace('null', '0')
	newFile = open('new' + fileName, "w")
	newFile.write(contents)        
	myfile.close()               
	newFile.close()  

def ToFile(path, fileName, data):
	filePathNameExt = './' + path + '/' + fileName + 'Calc' + '.json'
	
	with open(filePathNameExt, 'w') as fp:
		json.dump(data, fp)


def runJson(symbol):
	readXlsx.createLocaljsonObj(symbol)
	
	path = './'

	#Read JSON object
	data = {}
	decorateReadingFile(path, (symbol + ".json"))
	newJsonFile = 'new' + symbol + ".json"
	with open(newJsonFile) as json_file:
		data = json.load(json_file)

	#Generate all the calculations
	dataCalcs = doCalcs.calculate(data)

	if(newJsonFile):
		os.remove(newJsonFile)