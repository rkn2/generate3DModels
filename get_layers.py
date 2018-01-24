import rhinoscriptsyntax as rs

directory = 'G:\\My Drive\\Documents\\Research\\mikehess\\palazzo vecchio\\2017_9_7_ElementiModels\\FoundationModels\\ExistingGeometry\\2017_10_30\\'
fileName = 'this_is_a_test'
filetype = '.wrl'


#get layers
layers = rs.LayerNames()
rs.Command("Show")
for layer in layers:
    #grab only that layer
    rs.Command("-_SelLayer " + layer)
    rs.Command("-_Invert")
    rs.Command("Hide Enter")
    rs.Command("-_SelAll")
    
    #make cmdstr for export
    path = "\"" + directory + fileName + "_" + layer + filetype + "\""
    
    cmdstr = "-_Export " + path
    if filetype == '.wrl':
        cmdstr += " Enter Enter"
    
    cmd = rs.Command(cmdstr)
    if not (cmd):
        success = False
    
    rs.Command("-_SelNone")
    rs.Command("Show ")