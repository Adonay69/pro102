import os 
import shutil

source = "C:/Users/jacka/Downloads/images"
dest = "C:/Users/jacka/Downloads/result"

list_of_files = os.listdir(source)
print(list_of_files)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    #print(name)
    #print(ext)
    if ext == '':
        continue 
    if ext in ['.txt','.pdf']:
        path1 = source+'/'+file_name
        path2 = dest+'/'+'images'
        path3 = path2+'/'+file_name
        if os.path.exists(path2):
            print('moving....'+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving....'+file_name)
            shutil.move(path1,path3)
        
