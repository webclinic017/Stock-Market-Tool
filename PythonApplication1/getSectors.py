import sectors
import Enums

def makeSectors(symbols):
	
	energyServices = []
	materials = []
	industrials = []
	consumerDiscretionary = []
	consumerStaples = []
	healthCare = []
	financials = []
	informationTechnology = []
	utilities = []
	realEstate = []
	communicationServices = []

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
	#print("energyServices: ", len(energyServices), energyServices)
	#print("materials: ", len(materials), materials)
	#print("industrials: ", len(industrials), industrials)
	#print("consumerDiscretionary: ", len(consumerDiscretionary), consumerDiscretionary)
	#print("consumerStaples: ", len(consumerStaples), consumerStaples)
	#print("healthCare: ", len(healthCare), healthCare)
	#print("financials: ", len(financials), financials)
	#print("informationTechnology: ", len(informationTechnology), informationTechnology)
	#print("utilities: ", len(utilities), utilities)
	#print("realEstate: ", len(realEstate), realEstate)
	#print("communicationServices: ", len(communicationServices), communicationServices)

	sectorList = [energyServices, materials, industrials, consumerDiscretionary, consumerStaples, healthCare, financials, informationTechnology, utilities, realEstate, communicationServices]
	
	#for x in range(len(sectorList)): 
	#	print(sectorList[x]) 
	return sectorList


#def findSector(symbol, sectorList):

#	for sector in sectorList:
#		for company in sector:
#			if(symbol == company):
#				return #sector name

#	return "Sector not found"
