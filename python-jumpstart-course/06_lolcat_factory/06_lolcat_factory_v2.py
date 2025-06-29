import os
import shutil
import requests
import subprocess
import platform

str1 = "LOLCAT_FACTORY_V2"
print("-"*60)
print(f'{str1:-^60}')
print("-"*60)

# -- lets check where are we, current working dir.
work_dir = os.getcwd()
print(work_dir)
# c:/Users/Admin/Luka+Py/06_lolcat_factory/06_lolcat_factory_v2.py


# -- define everything inside a function:
def get_cat():
    # filepath + folder_name = path - This will be the folder that will contain downloaded images
    file_path = 'c:/Users/Admin/Luka+Py/06_lolcat_factory/'
    folder_name= 'cats_images'
    path= os.path.join(file_path,folder_name)
    # os.path.exists - > returns True in case the given path is a directory or a file 
    # Here we check if there is no directory nor file.
    if not os.path.exists(path):
        print(f'The directory at {path} does not exist. Directory will be created.')
        os.makedirs(path)  # Create the directory if it doesn't exist
    else:
        print(f'Directory {path} exists, proceeding to download image.')
    # -- define the response, base url

    base_url = 'https://cataas.com/cat' # - '/cat' -> this one will return a random cat
    response = requests.get(base_url,stream=True)

    if response.status_code == 200: # value for status code between 200 and 299 represents successful responses (reference [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status])
        # Here I define file name that will be downloaded.
        file_name = 'random_cat.jpg'
        response = requests.get(base_url,stream=True)
        full_file_path = os.path.join(path,file_name)
        with open(full_file_path,'wb') as file:  # Here I made a huge mistake first because i was trying to pass path which previously represented directory and not a full path.
            # i will define full path above
            shutil.copyfileobj(response.raw,file)
            print(f"Image downloaded {file_path}")
        if platform.system()=='Windows':
            subprocess.call(['explorer',file_path])
        # this line succesfully opens the folder with downloaded image
get_cat() # seems to work fine :D
