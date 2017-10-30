import sys
path1 = 'C:\\Users\\Rebecca Napolitano\\Documents\\GitHub\\generate3DModels\\'
sys.path.insert(0, path1) #navigate to function folder
import wrl23ddat as wrl

path = 'C:\\Users\\Rebecca Napolitano\\Documents\\datafiles\\Romanbondingcourses\\2017_10_16_simulations\\'
wrl.wrl23ddat(path)