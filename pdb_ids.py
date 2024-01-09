import os
pdb_files='/Users/neetumathews/biologics_files'
files = os.listdir(pdb_files)
file_names=[]
for x in files:
    if x.count("histone"):
        file_names.append(x[:-13])
    else:
        file_names.append(x[:-4])
    #remove endings
for x in range(len(file_names)):
    if file_names[x].count("pdb"):
        file_names[x]=file_names[x][3:]

total_molecules=[]
for x in file_names:
    if total_molecules.count(x)==0:
        total_molecules.append(x)
        #removes duplicates
    else:
        pass
print(total_molecules) #2838 unique molecules

        
        
