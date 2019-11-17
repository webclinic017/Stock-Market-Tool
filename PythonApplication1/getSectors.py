import sectors
import Enums
import instantiate
import json
import numpy as np

def organizeSectors(symbols):
	
	energyServices = []
	energyServices.append("Energy Services")
	materials = []
	materials.append("Materials")
	industrials = []
	industrials.append("Industrials")
	consumerDiscretionary = []
	consumerDiscretionary.append("Consumer Discretionary")
	consumerStaples = []
	consumerStaples.append("Consumer Staples")
	healthCare = []
	healthCare.append("Healthcare")
	financials = []
	financials.append("Financials")
	informationTechnology = []
	informationTechnology.append("Information Technology")
	utilities = []
	utilities.append("Utilities")
	realEstate = []
	realEstate.append("Real Estate")
	communicationServices = []
	communicationServices.append("Communication Services")

	i=0
	while(i < len(symbols)):
		if(sectors.div[symbols[i]] == Enums.Sector.ENRS):
			energyServices.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.MATR):
			materials.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.INDU):
			industrials.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.COND):
			consumerDiscretionary.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.CONS):
			consumerStaples.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.HLTH):
			healthCare.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.FINL):
			financials.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.INFT):
			informationTechnology.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.UTIL):
			utilities.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.REAL):
			realEstate.append(symbols[i])
		elif(sectors.div[symbols[i]] == Enums.Sector.TELS):
			communicationServices.append(symbols[i])
		i+=1

	sectorList = [energyServices, materials, industrials, consumerDiscretionary, consumerStaples, healthCare, financials, informationTechnology, utilities, realEstate, communicationServices]
	
	return sectorList


def makeSectorData(sectorList, dataList, dataCalcList):

	sectorData = {}
	sec = 0
	for sector in sectorList:
		for tick in range(len(sector)):
			if(1 < len(sectorList[sec]) and 0 < tick):
				#print(sectorList[sec][0], ": ", sectorList[sec][tick])
				idx =  dataCalcList.index(sectorList[sec][tick] + "Calc.json")
				print(sectorList[sec][tick], ": ", sectorList[sec][0], dataCalcList.index(sectorList[sec][tick] + "Calc.json"))
				#print(dataList[idx])
				#print(dataCalcList[idx])
				
				#Grab a ticker's json data & dataCalc file for appending to sector data
				#with open(dataList[tick]) as json_file:
				#	data = json.load(json_file)
				with open(dataCalcList[idx]) as json_file:
					dataCalc = json.load(json_file)
				#print(data)
				#print()
				print(dataCalc)
				#print()
				print()
				print()

				#year=0
				#while(year < 34):
				#	#Stop if error:
				#	if(dataCalc['YEAR_INC'][year] != dataCalc['YEAR_BAL'][year] and dataCalc['YEAR_CF'][year] != dataCalc['YEAR_BAL'][year]):
				#		print("Year mismatch error: ", dataCalc['YEAR_INC'][year], dataCalc['YEAR_BAL'][year], dataCalc['YEAR_CF'][year])
				#		break
				#	print(dataCalc['NWC_TO_TA'][year])
				#	#sectorData['NWC_TO_TA'][sec][year]
				#	year += 1
		sec += 1

	return sectorData




##def findSector(symbol, sectorList):

#	for sector in sectorList:
#		for company in sector:
#			if(symbol == company):
#				return #sector name

#	return "Sector not found"
