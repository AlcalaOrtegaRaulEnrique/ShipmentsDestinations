import os

shipmentsDestinationsFile=open(input("Input the file containing the street addresses of the shipment destinations: "))
driversNamesFile=open(input("Input the file containing the names of the drivers: "))
vowels = ['a', 'e', 'i', 'o', 'u']
evenByDriver = {}
oddByDriver = {}
sortedEven = []
sortedOdd = []
shipmentDestinationsAssignment = {'Total SS': 0}

def sortDriversScore():
	for driver in driversNamesFile:
		driver = driver.strip(os.linesep)
		driverName = driver.split()
		driverNameFormatted = ' '.join(driverName)
		lettersByDriver = {'Vowels': 0,'Consonants': 0, 'even': 0, 'odd': 0}
		score={'even': 0, 'odd': 0}
		driverName = ''.join(driverName)
		driverName = driverName.lower()
		for character in driverName:
			if(character in vowels):
				lettersByDriver['Vowels']+=1 
			else:
				lettersByDriver['Consonants']+=1
				lettersByDriver['even'] = lettersByDriver['Vowels']*1.5
				lettersByDriver['odd'] = lettersByDriver['Consonants']
				evenByDriver[driverNameFormatted] = lettersByDriver['Vowels']*1.5
				oddByDriver[driverNameFormatted] = lettersByDriver['Consonants']
	sortedEven[:] = sorted(evenByDriver.items(), key=lambda x: x[1])
	sortedOdd[:] = sorted(oddByDriver.items(), key=lambda x: x[1])

def assignShipmentDestinationsToDrivers():
	evenIndex=len(sortedEven)-1
	oddIndex=len(sortedOdd)-1
	for line in shipmentsDestinationsFile:
		line = line.strip(os.linesep)
		shipmentDestination=line.split()
		shipmentDestination = ' '.join(shipmentDestination)
		notAssignedDriver  = 'true'
		while(notAssignedDriver == 'true'):
			if(len(shipmentDestination) % 2 == 0):
				driverName = sortedEven[evenIndex][0]
				baseSS = sortedEven[evenIndex][1]
				if driverName not in shipmentDestinationsAssignment:
					shipmentDestinationsAssignment[driverName] = shipmentDestination
					shipmentDestinationsAssignment['Total SS']+=baseSS
					notAssignedDriver = 'false'
				else:
					notAssignedDriver = 'true'
				evenIndex -= 1 					
			else:
				driverName = sortedOdd[oddIndex][0]
				baseSS = sortedOdd[oddIndex][1]
				if driverName not in shipmentDestinationsAssignment:
					shipmentDestinationsAssignment[driverName] = shipmentDestination
					shipmentDestinationsAssignment['Total SS']+=baseSS 
					notAssignedDriver = 'false'
				else:
					notAssignedDriver = 'true'
				oddIndex -= 1
	print(shipmentDestinationsAssignment)

sortDriversScore()
assignShipmentDestinationsToDrivers()