# -*- coding: utf-8 -*-
"""
This function takes the .wrl files and makes them .3ddat files
"""

import glob
import os
import shutil
import subprocess

def wrl23ddat(file_path):

    VTPT_path = 'C:/Users/Rebecca Napolitano/Documents/Itasca/3dec520/My Projects/'

    os.chdir(file_path)
    fileHandles = glob.glob('*.wrl')

    
    for entry in fileHandles:
        
        entry3ddat = entry.replace('.wrl','.3ddat')
        
        if os.path.exists(entry3ddat) == False: #check to see if we need to do it
            print(entry + ' is new')
            
            os.chdir(VTPT_path)
            #write a new file called a.wrl that has the same information as entry
            shutil.copyfile(file_path+entry, 'a.wrl')
            #run vtpt
            proc = subprocess.Popen("VTPT.exe", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0)
            #pyautogui.press('enter')
            count=0    
            all_outs = ''
            while True:
                buff = proc.stdout.readline().decode("utf-8").strip()
                outs = str(buff)
                if proc.poll() != None:
                    count += 1
                if count > 10:
                    break
                all_outs += outs
            if 'Successful termination' not in all_outs:
                print('ERROR RUNNING VTPT:')
                print(all_outs)
            print('')
            #delete a.wrl file
            os.remove('a.wrl')
            #change the name of a.3dec back to its name + .3dec extension
            shutil.move('a.3dec', file_path+entry.replace('.wrl','.3ddat'))
        
        else:
            print(entry + ' is already done')
        
    
