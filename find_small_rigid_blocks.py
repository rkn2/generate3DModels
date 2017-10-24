import rhinoscriptsyntax as rs


tolerance = 170 #m3


#pick an object
object_id = rs.GetObjects()

#Loop between my objects
for object_i in object_id:
    #deselect any objects
    rs.Command("-_selnone")
    #get block id
    #print object_i
    object_i = str(object_i)
    block = rs.Command("-_SelID " + object_i)
    #get volume
    volume = rs.Command("-_Volume ")
    print volume
#    #delete if too small
#    if volume < tolerance:
#        rs.Command("-_Delete")
#        print "Deleting block"
#    