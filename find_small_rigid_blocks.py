import rhinoscriptsyntax as rs

#def zero_vol_rigid_blocks():
tolerance = 1e-4
rs.Command("-_show Enter")
rs.Command("-_SelMesh Hide ")
rs.Command("-_SelAll ")
object_id = rs.GetObjects(message="Bla", preselect=True)
count = 0

for object_i in object_id:
    #deselect any objects
    rs.Command("-_selnone")
    
    #get block id
    object_i = str(object_i)
    block = rs.Command("-_SelID " + object_i)
    
    #getvolume
    i = rs.coercebrep(object_i)

    blockVolume = i.GetVolume()
    
    
    #delete where appropriate
    if blockVolume < tolerance:
        rs.Command("-_Delete")
        print "Deleting block"
        count += 1

rs.Command("-_SelNone ")        
count = str(count) + " zero volume blocks were deleted"
print count 