#IMPORTANT NOTICE!
#IF YOU EDIT THIS FILE MAKE SURE TO EDIT THE FILE IN THE APP DATA FOR RHINO
#sometimes you might have to close rhino, open script editor (editScript) close that and then try to use the command


import rhinoscriptsyntax as rs
import os
import shutil
import sys

# Saves a file with name filename and extension filetype in directory (directory
# must be a full path, with double backslashes). Returns False in case of 
# failure.
def saveAs(directory, filename, filetype):
    
    # adds slashes to directory
    if directory[-1] != "\\":
        directory += "\\"
        
    # make cmdstr, add extra Enters to bypass options for .wrl
    path = "\"" + directory + filename + filetype + "\""
    cmdstr = "-_SaveAs " + path 
    if filetype == ".wrl":
        cmdstr += " Enter Enter"
        
    return rs.Command(cmdstr)

# Exports each layer as a separate file called "filename-layername" if there are
# multiple layers, or just "filename" if there is only one layer, saved in 
# directory with extension filetype. Returns True if all layers are exported 
# successfully and False otherwise.

def exportLayers(directory, filename, filetype):
    
    success = True
    
    # adds slashes to directory
    if directory[-1] != "\\":
        directory += "\\"
    
    # iterates through layers
    layers = rs.LayerNames() 
    for layer in layers:
        
        if layer != 'concrete':
        
            # select layer
            rs.Command("-_SelLayer " + layer)
            
            #mesh so that you can have only simple planes        
            rs.Command("-_Mesh DetailedOptions SimplePlane=Yes Enter")
            
            # make cmdstr, include layer if there are multiple layers
            if len(layers) > 1:
                path = "\"" + directory + filename + "_" + layer + filetype + "\""
            else:
                path = "\"" + directory + filename + filetype + "\""
                
            rs.Command("-_SelNone ")
            rs.Command("-_SelLayer " + layer)
            rs.Command("-_Invert ")
            rs.Command("Hide Enter")
            rs.Command("-_SelMesh ")
    
            cmdstr = "-_Export " + path
            if filetype == ".wrl":
                cmdstr += " Enter Enter"
            
            # execute command
            cmd = rs.Command(cmdstr)
            if not(cmd):
                success = False
                
            rs.Command("-_SelNone")
            rs.Command("Show ")
        
    return success


# Creates a new file with units dictated by string units. Deletes all but one
# layer. Returns False in case of failure, and True otherwise. Options: "Micron"
# ("M"), "Millimeter" ("i"), "Centimeter" ("C"), "Meter" ("e"), "Kilometer" 
# ("K"), "Microinch" ("r"), "Mil" ("l"), "Inch" ("n"), "Foot" ("F"), "Mile". 
def new(units="Meter"):
    
    # create new file
    successNew = rs.Command("-_New None")
    
    # change units
    successProp = rs.Command("-_DocumentProperties Units UnitSystem " + units + 
                                " No Enter Enter")
    
    # delete all but one layer
    layerCt = rs.LayerCount()
    for i in range(layerCt - 1):
        layer = rs.CurrentLayer()
        rs.DeleteLayer(layer)
    
    return successNew and successProp

# Runs a command with name command and arguments args
def runCommand(command, args):
    cmdstr = command
    for arg in args:
        cmdstr += " "
        if isinstance(arg, (str, unicode)):
            cmdstr += arg
        else:
            cmdstr += str(arg)
    rs.Command(cmdstr)

# Given all the arguments used for the command, runs the buildMasonryWall
# command
def buildMasonryWall(stoneWidth, stoneHeight, stoneDepth, mortarWidth, wallWidth, wallHeight, mortar="yes"):
    args = [stoneWidth, stoneHeight, stoneDepth, mortarWidth, wallWidth, 
                wallHeight, mortar]
    runCommand("_buildMasonryWall", args)

# Given parameters for bonding course wall, executes buildBondingCouseWall
# command. Returns False in case of error and True otherwise.
def buildBondingCourseWall(wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth, brickHeight="Enter", brickWidth="", firstCourse="", brickRow="", bondingCourses="", settleWidth="Enter", settleDepth=""):
    
    # check for missig brick parameters
    if brickHeight == "Enter" and brickWidth != "":
        print "Error: brickWidth but no brickHeight"
        return False
    if ((brickWidth == "" or firstCourse == "" or brickRow == "" or 
            bondingCourses == "")and brickHeight != "Enter"):
        print "Error: Missing brick information"
        return False
    
    # check for missing settlement parameters
    if settleWidth == "Enter" and settleDepth != "":
        print "Error: settleDepth but no settleWidth"
        return False
    if settleDepth == "" and settleWidth != "Enter":
        print "Error: settleWidth but no settleDepth"
        return False
    
    # run command
    args = [wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth,
                brickHeight, brickWidth, firstCourse, brickRow, bondingCourses, 
                settleWidth, settleDepth]
    runCommand("_buildBondingCourseWall", args)
    
    return True

# Given parameters for opus latericium wall, executes buildOpusLat command
def buildOpusLat(wallHeight, wallWidth, wallDepth, stoneHeight, stoneWidth, stoneDepth, settleWidth="Enter", settleDepth=""):
    
    # check that settleWidth and settleDepth are consistent
    if settleWidth == "Enter" and settleDepth != "":
        print "Error: settleDepth but no settleWidth"
        return
    if settleDepth == "" and settleWidth != "Enter":
        print "Error: settleWidth but no settleDepth"
        return
    
    args = [wallHeight, wallWidth, wallDepth, stoneHeight, stoneWidth,
                stoneDepth, settleWidth, settleDepth]
    runCommand("_buildOpusLat", args)

# Given parameters for opus quasi reticulatum wall, executes buildOpusQuasiRet
# command
def buildOpusQuasiRet(wallHeight, wallWidth, wallDepth, stoneLength, stoneDepth, settleWidth="Enter", settleDepth=""):
    
    # check that settleWidth and settleDepth are consistent
    if settleWidth == "Enter" and settleDepth != "":
        print "Error: settleDepth but no settleWidth"
        return
    if settleDepth == "" and settleWidth != "Enter":
        print "Error: settleWidth but no settleDepth"
        return
    
    args = [wallHeight, wallWidth, wallDepth, stoneLength, stoneDepth, 
                settleWidth, settleDepth]
    runCommand("_buildOpusQuasiRet", args)

# Given parameters for opus incertum wall and importFile--a file containing a 
# base stone geometry, executes buildOpusIncertum command. If importFile is 
# "Enter", default file "Incertum.3dm" is used.
def buildOpusIncertum(wallHeight, wallWidth, wallDepth, stoneDepth, aveDiam, settleWidth="Enter", settleDepth="", importFile="Enter"):
    
    # check that settleWidth and settleDepth are consistent
    if settleWidth == "Enter" and settleDepth != "":
        print "Error: settleDepth but no settleWidth"
        return
    if settleDepth == "" and settleWidth != "Enter":
        print "Error: settleWidth but no settleDepth"
        return
        
    args = [importFile, wallHeight, wallWidth, wallDepth, stoneDepth, aveDiam, 
                settleWidth, settleDepth]
    runCommand("_buildOpusIncertum", args)

# Given all the arguments used for the command, where "Enter" gives the default 
# value, runs the buildZipperVault command
def buildZipperVault(radius, vaultLength, stoneDepth, stoneWidth, stoneHeight, orientHeight="Enter", orientDepth="Enter", startHeight="Enter"):
    args = [radius, vaultLength, startHeight, orientHeight, orientDepth,
                stoneDepth, stoneWidth, stoneHeight]
    runCommand("_buildZipperVault", args)

# Given all the arguments used for the command, where "Enter" gives the default 
# value and "" is used when the prompt does not appear, runs the buildArch 
# command
def buildArch(thickness, depth, voussoirs, span="Enter", height="Enter", angle="", haunches="no", haunchHeight="", haunchWidth=""):
    if haunches == "yes":
        if haunchHeight == "":
            haunchHeight = "Enter"
        if haunchWidth == "":
            haunchWidth = "Enter"
    args = [span, height, angle, thickness, depth, voussoirs, haunches,
                haunchHeight, haunchWidth]
    runCommand("_buildArch", args)

# Given all the arguments used for the command, where "Enter" gives the default 
# value and "" is used when the prompt does not appear, runs the 
# buildMultilayerArch command
def buildMultilayerArch(stoneHeight, depth, voussoirs, layers, span="Enter", height="Enter", angle=""):
    args = [span, height, angle, stoneHeight, depth, voussoirs, layers]
    runCommand("_buildMultilayerArch", args)

# Given the type of barrel vault (1, 2, or 3) and all the arguments used for the 
# command, where "Enter" gives the default value and "" is used when the prompt
# does not appear, runs one of the buildBarrelVault commands
def buildBarrelVault(type, thickness, depth, vaultDepth, voussoirs, span="Enter", height="Enter", angle="", haunches="no", haunchHeight="", haunchWidth=""):
    if type > 3 or type < 1:
        print "Error: type out of range"
        return 1
    if haunches == "yes":
        if haunchHeight == "":
            haunchHeight = "Enter"
        if haunchWidth == "":
            haunchWidth = "Enter"
    args = [span, height, angle, thickness, depth, vaultDepth, voussoirs,
                haunches, haunchHeight, haunchWidth]
    cmd = "_buildBarrelVault" + str(type)
    runCommand(cmd, args)

# Given parameters for corbelled arch, executes buildCorbelledArch command
def buildCorbelledArch(stoneHeight, stoneWidth, depth, span, overhang, haunches="no", haunchHeight="", haunchWidth=""):
    args = [stoneHeight, stoneWidth, depth, span, overhang, haunches, 
                haunchHeight, haunchWidth]
    runCommand("_buildCorbelledArch", args)

# Given parameters for corbelled vault, executes buildCorbelledVault command
def buildCorbelledVault(stoneHeight, stoneWidth, stoneDepth, vaultDepth, span, overhang, haunches="no", haunchHeight="", haunchWidth=""):
    args = [stoneHeight, stoneWidth, stoneDepth, vaultDepth, span, overhang, 
                haunches, haunchHeight, haunchWidth]
    runCommand("_buildCorbelledVault", args)

# Given parameters for groin vault, executes buildGroinVault command
def buildGroinVault(span, xDim, yDim, stoneHeight, stoneDepth, stoneWidth):
    args = [span, xDim, yDim, stoneHeight, stoneDepth, stoneWidth]
    runCommand("_buildGroinVault", args)


#builds bonding course wall without bonding courses in there
def buildNOBC(wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth, settleWidth="Enter", settleDepth="", sideBaseWidth=""):
    # check for missing settlement parameters
    if settleWidth == "Enter" and settleDepth != "":
        print "Error: settleDepth but no settleWidth"
        return False
    if settleDepth == "" and settleWidth != "Enter":
        print "Error: settleWidth but no settleDepth"
        return False
    
    # run command
    args = [wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth,
                settleWidth, settleDepth, sideBaseWidth]
    runCommand("_buildNOBC", args)
    
    return True

def buildBondingCourseWallv2(wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth, brickHeight="Enter", brickWidth="", firstCourse="", brickRow="", bondingCourses="", settleWidth="Enter", settleDepth="", sideBaseWidth = ""):
    
    # check for missig brick parameters
    if brickHeight == "Enter" and brickWidth != "":
        print "Error: brickWidth but no brickHeight"
        return False
    if ((brickWidth == "" or firstCourse == "" or brickRow == "" or 
            bondingCourses == "")and brickHeight != "Enter"):
        print "Error: Missing brick information"
        return False
    
    # check for missing settlement parameters
    if settleWidth == "Enter" and settleDepth != "":
        print "Error: settleDepth but no settleWidth"
        return False
    if settleDepth == "" and settleWidth != "Enter":
        print "Error: settleWidth but no settleDepth"
        return False
    
    # run command
    args = [wallWidth, wallHeight, wallDepth, stoneHeight, stoneWidth,
                brickHeight, brickWidth, firstCourse, brickRow, bondingCourses, 
                settleWidth, settleDepth, sideBaseWidth]
    runCommand("_buildBondingCourseWallv2", args)
    
    return True

def meshing(meshValue, directory):
    #meshValue = '0.5 '
            
    os.chdir(directory)
                
    #meshcommands
    angle = ' _angle=0'
    aspectratio =' _aspectratio=0' 
    distance = ' _distance=0'
    grid = ' _grid=0'
    maxedgelength = ' _maxedgelength=' + meshValue
    maxedgelengthstr= maxedgelength
    minedgelength = ' _minedgelength=' + meshValue
    minedgelengthstr = minedgelength
    
    advOptions = angle + aspectratio + distance + grid + maxedgelengthstr + minedgelengthstr
    
    #gsurfcommands
    
    mode = '_mode=tri'
    minedgelength = '_minedgelength=' + meshValue
    maxedgelength = '_maxedgelength=' + meshValue
    ridgeangle = '_ridgeangle=20'
    maxgradation = '_maxgradation=1'
    deleteinput = '_deleteinput=Yes'
    
    gsurfOptions = mode + minedgelength + maxedgelength + ridgeangle + maxgradation + deleteinput
    
    #gvol options
    gvol_mode = '_mode=tet '
    outputformat = '_outputformat=3DEC '
    
    gvolOptions = gvol_mode + outputformat
    
    rs.Command("-_SelNone ")
    layers = rs.LayerNames()
    for layer in layers:
        if layer == 'concrete':
                           
            rs.Command("-_SelLayer " + layer)
            #rs.Command("_Enter")
            rs.Command("Invert ")
            rs.Command("Hide Enter")
            rs.Command("-_SelLayer " + layer)
            rs.Command("-_Mesh _DetailedOptions _AdvancedOptions " + advOptions + '_Enter _Enter')
            rs.Command("-_SelNone ")
            rs.Command("-_SelMesh ")
            rs.Command("-_Gsurf " + gsurfOptions + '_Enter _Enter')
            rs.Command("-_SelMesh")
            rs.Command("-_Gvol " + gvolOptions + '_Enter _Enter')    
          
    return True