#finds and deletes small blocks

#calculate volumne 

import os
import numpy as np

def file_len(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i + 1

directory = 'C:/Users/Rebecca Napolitano/Google Drive/Documents/Research/mikehess/palazzo vecchio/2017_9_7_ElementiModels/FoundationModels/ExistingGeometry/'
filename ='testy.txt'
outFile = 'blockstesty.txt'
outFile2 = 'thisisatest.txt'
os.chdir(directory)

#create the files and delete other existing ones
outfile = open(outFile, "w")
outfile2 = open(outFile2,"w")
outfile.close()


#count blocks
total = 0

with open(filename) as f:
    for line in f:
        finded = line.find('block')
        if finded != -1 and finded != 0:
            total += 1
#print(total)
f.close()

#read in the gvol file
data = open(filename).read().split('\n')

#find discrete block sections
#change '   ' to ';;;'
#open outfile for writing
outfile = open(outFile, "w+")
for line in data:
    line= line.replace('   ', ';;;')
    outfile.write(line + '\n')
outfile.close()
#keep lines with ';;;'
data = open(outFile).read().split('\n')
flag = ';;;'
for line in data: 
    if ';;;' in line:
        line = line.replace(';;;','').replace('&','')
        outfile2.write(line + '\n')

#check for number of blocks
i = 0 #for line counting function   
fileLength = file_len(outFile2) #works!
numberBlocks = int(fileLength / 12)
if numberBlocks != total:
    print("Error with the number of blocks!")
else:
    print("All good")

#iterate through the list of lines, and put the blocks faces and blocks back together
#each face has 3 sets of points and each block has 4 faces, so each block has 12 lines of code 

j = 1
data = open(outFile2).read().split('\n')
while j <= numberBlocks:
    #grab twelve lines for that block
    start = 0 
    end = start + 12
    blockLine = data[start : end]
    
    #remove spaces at the end of some lines
    dataFixed = []
    for line in blockLine:
        if line[-1] == ' ':
            line = line[0:-1]
        dataFixed.append(line)
    #get unique lines
    uniqueLines = set(dataFixed)
    print("This is block " + str(j))
    print(uniqueLines)
    

    start = start + 12 #increments for each block
    j = j + 1
#    
#        
#        
    
    


        
            

#find unique vertex locations
#find volume of that block
#find vector from a to b
#find vector from a to c
#find vector from a to d
#find triple product 
#find 1/6 absolute value of the triple product

outfile2.close()

#make sure all files are closed
#delete outfiles created during process

