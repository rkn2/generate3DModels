import numpy as np
path = 'C:/Users/Rebecca Napolitano/Documents/Itasca/3dec520/My Projects/a.3dec'
rmag = 1e-1

class vertex_replacer:    
    def reset(self):
        self.block_rep = {}
    def convert_and_randomize(self,vert_s,line):
        vert_f = [float(x) for x in vert_s]
        vert_r = vert_f + rmag * 2. * ( np.random.rand(3) - 0.5 )
        key_start = l[i].find(vert_s[0])
        
        key_end = l[i].find(vert_s[2]) + len(vert_s[2])
        old_key = l[i][key_start:key_end]
        new_key = '%.6e %.6e %.6e '%tuple(vert_r)
        if len(old_key) > 50:
            self.block_rep[old_key] = new_key
        
    def vert_replace(self,line):
        for old_key in self.block_rep.keys():
            if old_key in l[i]:
                line = line.replace(old_key,self.block_rep[old_key])
        return line

vr = vertex_replacer()
fid = open(path,'r')
l = fid.readlines()
i = 1
while i < len(l):
    # find next block
    while '; block' not in l[i]:
        i += 1
    vr.reset()
    #print(l[i]) #reset is fine
    i += 1
    while '; block' not in l[i]:
        if 'face ID' in l[i]:
            #vert_s = l[i].split()[3:6]
            vert_s = l[i].split()[3]
            #print('face',vert_s)
            vr.convert_and_randomize(vert_s,l[i])
            l[i] = vr.vert_replace(l[i])        
        else:
            try:
                vert_s = l[i].split()[:3]                
                vr.convert_and_randomize(vert_s,l[i])
                #print('vert',vert_s)
                l[i] = vr.vert_replace(l[i])
            except:
                pass
        i += 1
        if i >= len(l):
            break
        
fid.close()
fid = open(path.replace('a.3dec','r.3ddat'),'w')
fid.writelines(l)
fid.close()

# does not work, mistake somewhere, not getting new line...?