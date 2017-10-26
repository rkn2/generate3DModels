#makes walls with roman bonding courses
import sys
import rhinostriptsyntax as rs
#file_path = location of usemasonrycommands.py
file_path = 'C:\\Users\\Rebecca Napolitano\\Documents\\GitHub\\generate3DModels\\'    
sys.path.append(file_path)
import useMasonryCmds as umc #this is where the commands for geometry generation, meshing, exporting, saving, etc are

############################################################################
#                           SET UP PARAMETERS

directory = "C:\\Users\\Rebecca Napolitano\\Documents\\datafiles\\Romanbondingcourses\\2017_10_26_experiments\\" #Where do you want the files to generate?
  
wallWidth = 7   
wallHeight = 3.3
wallDepth = 2
stoneHeight = 0.3 
stoneWidth = 0.5
brickHeight = 0.1
brickWidth = 0.3
firstCourse = 0.9
brickRow = 3
sideBaseWidth = 0.4
#TOL = 1e-5 #what does this do???
meshValue = '0.5 ' #parameter for gsurf meshing

#############################################################################

# do you have anything that needs meshing? anything deformable? commend out anything that does not apply

deformableKeys = []
deformableKeys.append('deformable')
deformableKeys.append('mortar')
deformableKeys.append('infill')

##############################################################################

#generating models 

i = 0 #number of bonding courses
j = 0 #width
k = 0 #settlement depth   

#make a list of the parameters you want the geometry generation to loop over
#iList = [1, 2]
#jList = [0.5, 2, 3, 4]
#kList = [0, 0.05, 0.1, 0.2]

iList = [1]
jList = [2]
kList = [0.2]

umc.new()
  
while i <= len(iList) - 1 :
    while j <= len(jList) - 1 :
        while k <= len(kList) - 1 :
            iEntry = iList[i]
            jEntry = jList[j]
            kEntry = kList[k]
            
            #buildBondingCourseWall(wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth, brickHeight="Enter", brickWidth="", firstCourse="", brickRow="", bondingCourses="", settleWidth="Enter", settleDepth=""):          
            umc.buildBondingCourseWallv2(wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth, brickHeight, brickWidth, firstCourse, brickRow, iEntry, jEntry, kEntry, sideBaseWidth)
            filename = "bc_r" + str(iEntry) + "-w" + str(jEntry) + "-s" + str(kEntry)  
            
            #mesh for export
            rs.Command("-_Mesh ")
            
            
            
            
            success = umc.exportLayers(directory, filename, ".wrl")
            if not (success):
                break  
            

            #mesh 
            umc.meshing(meshValue, directory)
                     
            success = umc.saveAs(directory, filename, ".3dm")
            if not (success):
                break

            #open a new file
            if i < len(iList) + 1:                             
                success = umc.new()
                #rs.Command('_Enter')
                if not (success):
                    break
            k = k + 1
        j = j + 1
        k = 0
    i = i + 1
    j = 0
    


#generating a second type of model so reset i, j, and k
    
i = 0 #number of bonding courses
j = 0 #width
k = 0 #settlement depth   

umc.new()            
while j <= len(jList) - 1 :
    while k <= len(kList) - 1 :
        #iEntry = iList[i]
        jEntry = jList[j]
        kEntry = kList[k]
        umc.buildNOBC(wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth, jEntry, kEntry, sideBaseWidth)
        filename = "nobc-w" + str(jEntry) + "-s" + str(kEntry) 
        success = umc.exportLayers(directory, filename, ".wrl")
        if not (success):
            break
        #mesh 
        umc.meshing(meshValue, directory)

        success = umc.saveAs(directory, filename, ".3dm")
        if not (success):
            break

        #umc.meshing(meshValue)
        #open a new file
        if k < len(kList) + 1:
            success = umc.new()
            if not (success):
                break
        k = k + 1
    j = j + 1
    k = 0

             
