import os
import json
from distutils.dir_util import copy_tree

#Copy subdirectory 
fromDirectory = "data/01row_data"
toDirectory = "data/02transform_data"

copy_tree(fromDirectory, toDirectory)

folders = ["data/02transform_data/global", "data/02transform_data/timeline/"]

#Check folders size
print("Initial Quantity of File")
print("Folder 1", len(os.listdir(folders[0])), "Folder 2", len(os.listdir(folders[1])), '\n')

#Delete if no Timeline or no Global
#Make list of files
strip_dir_1 = []
for filename in os.listdir(folders[0]):
    strip_dir_1.append(filename.strip("global_.json"))

strip_dir_2 = []
for filename in os.listdir(folders[1]):
    strip_dir_2.append(filename.strip("timeline_.json"))

#Check if is in other folder
for el in strip_dir_1:
    if el not in strip_dir_2:
        file_path = os.path.join(folders[0], f"global_{el}.json")
        os.remove(file_path)

for el in strip_dir_2:
    if el not in strip_dir_1:
        file_path = os.path.join(folders[1], f"timeline_{el}.json")
        os.remove(file_path)

#Check folders size
print("Post Individual Cut Quantity of File")
print("Folder 1", len(os.listdir(folders[0])), "Folder 2", len(os.listdir(folders[1])), '\n')

for folder in folders:
    for filename in os.listdir(folder):
        if folder == "data/global/":
            matchid = filename.strip("global_.json")
        if folder == "data/timeline/":
            matchid = filename.strip("timeline_.json")

        #Open file
        if folder == "data/global/":
            with open(f'./data/global/global_{matchid}.json') as json_file:
                data = json.load(json_file)

        if folder == "data/timeline/":
            with open(f'./data/timeline/timeline_{matchid}.json') as json_file:
                data = json.load(json_file)

        #Delete if invalid request
        if 'status' in data.keys():

            if os.path.isfile(f'./data/global/global_{matchid}.json'):
                os.remove(f'./data/global/global_{matchid}.json')
            if os.path.isfile(f'./data/timeline/timeline_{matchid}.json'):    
                os.remove(f'./data/timeline/timeline_{matchid}.json')
        
        #Delete if ARAM
        if "gameMode" in data.keys():
            if data["gameMode"] == "ARAM" :

                print(matchid)
                
                if os.path.isfile(f'./data/global/global_{matchid}.json'):
                    os.remove(f'./data/global/global_{matchid}.json')
                if os.path.isfile(f'./data/timeline/timeline_{matchid}.json'):
                    os.remove(f'./data/timeline/timeline_{matchid}.json')
        
#Check folders size
print("End Quantity of File")
print("Folder 1", len(os.listdir(folders[0])), "Folder 2", len(os.listdir(folders[1])), '\n')

