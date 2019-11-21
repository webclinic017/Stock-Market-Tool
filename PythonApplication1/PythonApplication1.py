import manageJson
import glob
import os
import Enums
import boundings
import getSectors

#Keep the folder clean of previous json files
files = glob.glob("*.json")
for file in files:
	if(files != None):
		os.remove(file)

symbols = glob.glob("*.xlsx")
i=0
while(i < len(symbols)):
	symbols[i] = symbols[i].strip(".xlsx")
	manageJson.runJson(symbols[i])
	i += 1

jsonObjs = glob.glob("*.json")
dataList = []
dataCalcList = []
i=0
while(i < len(jsonObjs)): 
	if("Calc" not in jsonObjs[i] and "Rating" not in jsonObjs[i]):
		dataList.append(jsonObjs[i])
	if("Calc" in jsonObjs[i]):
		dataCalcList.append(jsonObjs[i])
	i += 1

if(len(dataList) != len(dataCalcList)):
	print("There has been an error")


#Generate sector data
ratings = {}
sectorList = getSectors.organizeSectors(symbols)
allSectorData = getSectors.makeSectorData(sectorList, dataList, dataCalcList)
#print(sectorData)
#print(sectorList)
#print(dataList)
#print(dataCalcList)
#Turn Calcs into meaningful interpreatations
sec=0
while(sec < len(allSectorData)):
	#print(allSectorData[i])
	#print(allSectorData[sec]['SECTOR'], ": ", allSectorData[sec]['LENGTH'])
	tick = 1
	count = 0
	while(count < allSectorData[sec]['LENGTH']):
		idx =  dataCalcList.index(sectorList[sec][tick] + "Calc.json")
		#print("sec: ", sec, "tick: ", tick, "data: ", dataList[idx], "Calc: ", dataCalcList[idx])
		boundings.genRatings(dataList[idx], dataCalcList[idx], allSectorData[sec])
		tick += 1
		count += 1
	sec += 1

#Generate recommendations

