import json

def writeToJsonFile(path, fileName, data):
    filePathNameExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameExt, 'w') as fp:
        json.dump(data, fp)


path = './'
fileName = 'example'

data = {}
data['row1'] = 'testRow1'
data['row2'] = 'testRow2'

writeToJsonFile(path, fileName, data)


