import rhinoscriptsyntax as rs

tolerance = 155e-07 #m3

geometry = rs.Command("-_SelAll ")
typeGeometry = type(geometry)
print typeGeometry

rs.Command("-_SelNone ")

for block in geometry:
    #grab it 
    blockSelected = rs.Command("-_Select " + block)
    #find volume
    blockVolume = rs.Command("-_Volume ")
    #delete if too small
    if blockVolume < tolerance:
        rs.Command("-_Delete")
        print "Block deleted"
    