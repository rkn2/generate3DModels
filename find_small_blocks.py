#finds and deletes small blocks

#calculate volumne 
#import glob
import os

directory = 'C:/Users/Rebecca Napolitano/Google Drive/Documents/Research/mikehess/palazzo vecchio/2017_9_7_ElementiModels/FoundationModels/ExistingGeometry/'
filename ='testy.txt'
os.chdir(directory)

#read in the gvol file
dataFile = open(filename, 'r')
data = dataFile.read()
dataFile.close()


#get the section for the first block
start = '; block'
end = ';block'
numberBlocks = data.find(start)
for i = 1: numberBlocks:
    data.find(start)



#find unique vertex locations
#find volume of that block
#find vector from a to b
#find vector from a to c
#find vector from a to d
#find triple product 
#find 1/6 absolute value of the triple product

