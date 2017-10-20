#finds and deletes small blocks

#calculate volumne 

import os


directory = 'C:/Users/Rebecca Napolitano/Google Drive/Documents/Research/mikehess/palazzo vecchio/2017_9_7_ElementiModels/FoundationModels/ExistingGeometry/'
filename ='testy.txt'
outFile = 'blockstesty.txt'
outFile2 = 'thisisatest.txt'
os.chdir(directory)

outfile = open(outFile, "a+")
outfile2 = open(outFile2,"a+")

#count blocks
total = 0

with open(filename) as f:
    for line in f:
        finded = line.find('block')
        if finded != -1 and finded != 0:
            total += 1
f.close()

#read in the gvol file
data = open(filename).read().split('\n')

#find discrete block sections
#change '   ' to ';;;'
for line in data:
    line= line.replace('   ', ';;;')
    outfile.write(line + '\n')
outfile.close()

#throw away any lines that do not start with ';;;'
data2 = open(outfile).read()
for line in data2: 
    if line.find(';;;') !=0:
        outfile2.write(line + '\n')
              

#find unique vertex locations
#find volume of that block
#find vector from a to b
#find vector from a to c
#find vector from a to d
#find triple product 
#find 1/6 absolute value of the triple product

outfile.close()
outfile2.close()