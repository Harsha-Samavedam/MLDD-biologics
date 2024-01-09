import os
full_dataset='/Users/neetumathews/Full DNA Dataset'
content=os.listdir(full_dataset)
families=[]
for f in content:
    if f!=".DS_Store":
        families.append(f)
        
#families contains all the families in the Full DNA Dataset

def get_textfiles(family,folder_path):
    pdb_ids=os.listdir(folder_path)
    for file in pdb_ids:
        if file.endswith(".txt"):
            print(file, family)
            timepass.append(file)
        elif file.endswith(".ini") or file==".DS_Store":
            pass #some of the subfolders had desktop.ini
        else:
            #subfolder is the path of the subfolders inside the family_folder
            subfolder=folder_path+f'/{file}'
            get_textfiles(fam,subfolder) #get all the pdb_ids inside every subfolder inside family_folder
for fam in families:
    family_folder=f'/Users/neetumathews/Full DNA Dataset/{fam}'
    get_textfiles(fam,family_folder)

