import os

def rename_files():
    file_list = os.listdir(r"/Users/Giorgio/Downloads/prank")
    print (file_list)

    os.chdir("/Users/Giorgio/Downloads/prank")
    for file_name in file_list:
       print(file_name)
       new_name = file_name.translate(None,'0123456789')
       print (new_name)
       os.rename(file_name, new_name)
    
rename_files()
