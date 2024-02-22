import os
full_dataset='/Users/neetumathews/Full DNA Dataset'
#full_dataset is from the GitHub pdb_files branch titled “Full DNA Dataset”
content=os.listdir(full_dataset)
families=[]
for f in content:
    if f!=".DS_Store":
        families.append(f)
        
#families contains all the families (main folders) in the Full DNA Dataset

def get_pdbcode(fullname,family_name): #splicing to just get the 4 letter code
    if fullname.count("pdb"):
        print(fullname[3:7].upper(),family_name)
    else:
        print(fullname[:4].upper(),family_name)
        
def get_textfiles(family,folder_path):
    pdb_ids=os.listdir(folder_path) #files inside the subfolder
    for file in pdb_ids:
        if file.endswith(".txt"):
            get_pdbcode(file,family)
        elif file.endswith(".ini") or file==".DS_Store":
            pass #some of the subfolders had desktop.ini
        else:
            #subfolder is the path of the subfolders inside the family_folder
            subfolder=folder_path+f'/{file}'
            get_textfiles(fam,subfolder) #get pdb_ids inside the specified subfolder
            
for fam in families:
    family_folder=f'/Users/neetumathews/Full DNA Dataset/{fam}' #pathway to a specified main folder
    get_textfiles(fam,family_folder)
