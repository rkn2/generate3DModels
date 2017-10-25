import rhinoscriptsyntax as rs

tolerance = 1e-4
object_id = rs.GetObjects()

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
    
    #print type(blockVolume)