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
#filename ='testy.txt'
filename = "GVol.3ddat"
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
#if numberBlocks != total:
#    print("Error with the number of blocks!")

#iterate through the list of lines, and put the blocks faces and blocks back together
#each face has 3 sets of points and each block has 4 faces, so each block has 12 lines of code 
start = 0 
j = 1
data = open(outFile2).read().split('\n')
while j <= numberBlocks:
    #grab twelve lines for that block
    
    end = start + 12
    #print("for block " + str(j) + "start is  "+ str(start) + "end is " + str(end))
    blockLine = data[start : end]
    
    #remove spaces at the end of some lines
    dataFixed = []
    for line in blockLine:
        if line[-1] == ' ':
            line = line[0:-1]
        dataFixed.append(line)
    uniqueLines = set(dataFixed)
    #print("This is block " + str(j))
    #print(uniqueLines)
    if len(uniqueLines) != 4:
        print("Error in number of vertices!!")
    dataFixed2 = []
    #make array not list of strings
    for line in uniqueLines:
        line = line
        dataFixed2.append(line)
    #break it into each point
    dataFixed3 = []
    for line in dataFixed2:
        line = line.split(" ")
        dataFixed3.append(line) 
    #convert all strings to floats
    dataFixed4 = []
    for line in dataFixed3:
        newLine = []
        for entry in line:
            entry = float(entry)
            newLine.append(entry)
        dataFixed4.append(newLine)
    
    #calculate volume of triangle base pyramid
    #>4 odd it is a pyramid; >4 even it is a prism; #do these using rhino functions
    #find ab
    abx = dataFixed4[1][0]-dataFixed4[0][0]
    aby = dataFixed4[1][1]-dataFixed4[0][1]
    abz = dataFixed4[1][2]-dataFixed4[0][2]
    #find ac
    acx = dataFixed4[2][0]-dataFixed4[0][0]
    acy = dataFixed4[2][1]-dataFixed4[0][1]
    acz = dataFixed4[2][2]-dataFixed4[0][2]
    #find ad
    adx = dataFixed4[3][0]-dataFixed4[0][0]
    ady = dataFixed4[3][1]-dataFixed4[0][1]
    adz = dataFixed4[3][2]-dataFixed4[0][2]
    #make a matrix
    matrixBlock = [[abx, aby, abz], [acx, acy, acz], [adx, ady, adz]]  
    #find triple product or determinate
    det = np.linalg.det(matrixBlock)
    #take absolute value
    det = abs(det)
    #find volume (abs(det)/6)
    volume = det/6
    if volume < 1e-5: 
        print("Volume of block " + str(j) + " is:")
        
        print(volume)
        xcent
        ycent
        zcent
        centroid = []
        centroid = [xcent, ycent, zcent]
        print("Centroid of problem block is " + centroid)

    start = start + 12 #increments for each block
    j = j + 1
     
    
    


        
            



outfile2.close()

#make sure all files are closed
#delete outfiles created during process

