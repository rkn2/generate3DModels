import rhinoscriptsyntax as rs
import os
import shutil
import sys

file_path = 'C:\\Users\\Rebecca Napolitano\\Documents\\GitHub\\generate3DModels\\'  
sys.path.append(file_path)
import find_small_rigid_blocks as zeroVol

directory = 'G:\\My Drive\\Documents\\Research\\mikehess\\palazzo vecchio\\2017_9_7_ElementiModels\\FoundationModels\\ExistingGeometry\\2017_10_30\\'
fileName = 'this_is_a_test'
filetype = '.wrl'
meshValue = '10 '
mesh = ['1']

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

#find zero volume blocks
zeroVol.zero_vol_rigid_blocks()


#get layers
layers = rs.LayerNames()

os.chdir(directory)

for layer in layers:
    rs.Command("Show")
    rs.Command("-_SelNone ")
    
    if layer in mesh:
        #run mesh, gsurf, gvol        
        rs.Command("-_SelLayer " + layer)
        rs.Command("Invert ")
        rs.Command("Hide Enter ")
        rs.Command("-_SelLayer " + layer)
        rs.Command("-_Mesh _DetailedOptions _AdvancedOptions " + advOptions + '_Enter _Enter')
        rs.Command("-_SelNone ")
        rs.Command("-_SelMesh ")
        rs.Command("-_Gsurf " + gsurfOptions + '_Enter _Enter')
        rs.Command("-_SelMesh")
        rs.Command("-_Gvol " + gvolOptions + '_Enter _Enter') 
        #rename gvol
        saveName = fileName + "_" + layer + ".3ddat"
        shutil.move('GVol.3ddat', saveName)
        
        
    else:
        #grab only that layer
        rs.Command("-_SelLayer " + layer)
        #simple planes
        rs.Command("-_Mesh DetailedOptions SimplePlane=Yes Enter")
        
        #make cmdstr for export
        path = "\"" + directory + fileName + "_" + layer + filetype + "\""    
        cmdstr = "-_Export " + path
        if filetype == '.wrl':
            cmdstr += " Enter Enter"   
        
        #selmesh and export           
                
        rs.Command("-_SelNone ")
        rs.Command("-_SelLayer " + layer)
        rs.Command("-_Invert ")
        rs.Command("Hide Enter")
        rs.Command("-_SelMesh ")   
            
        cmd = rs.Command(cmdstr)
        if not (cmd):
            success = False   
        rs.Command("-_SelNone")
        rs.Command("Show ")
        
        
        