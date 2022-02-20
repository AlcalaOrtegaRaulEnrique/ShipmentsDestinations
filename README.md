# ShipmentsDestinations

Application that assigns shipment destinations to drivers in a way that maximizes the total SS over the set of drivers.

*Instructions on how to build/run the app:

1. First of all, download this repository on your local machine.

2. Once you downloaded the repository, unzip it and you will see the folder project. 

3. In order to test the application you can use the two files inside the project folder, which are called: 'shipmentsDestinations.txt' and 'driversNames.txt'. The first containing the street addresses of the shipment destinations and the second containing the names of the drivers.  But if you prefer you can supply your own files of names. Only take these considerations: the names must be separated by newlines and not containing accents, the files must have .txt file extension and you must have put them inside of the project folder. 

3. After that open the terminal and make sure to have python 3 installed on your local machine. Now  go to the project folder and run the command "python3 main.py".

4. Once the application is running, first input the file name containing the street addresses of the shipment destinations, after input the file name of the file containing the names of the drivers. Finally as a result you will see a python dictionary containing the total SS and a matching between shipment destinations and drivers.

