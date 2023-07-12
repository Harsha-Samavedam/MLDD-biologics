import requests
import os
import re
import pymol


def save_coordinates_to_file(pdb_id , path):
    pymol.cmd.fetch(pdb_id)
    pymol.cmd.select("elem P")
    xyz = pymol.cmd.get_coords('(sele)', 1)

    # Create a filename using only the PDB ID
    filename = f"{pdb_id}.txt"

    # Write the rounded coordinates to the file
    with open(os.path.join(path, filename), 'w') as file:
        for coord in xyz:
            rounded_coord = [round(c, 3) for c in coord]
            rounded_coord = [f"{c:.3f}" for c in rounded_coord]  # Format to 3 decimal places
            file.write(f"{' '.join(rounded_coord)}\n")

    print(f"Coordinates saved to {filename}")

folder_name =""
directory = "C:\\Users\\rionn.LAPTOP-RIONN-HP\\Documents\\PDB"
# Using GraphQL
url = "https://data.rcsb.org/graphql?query="
#done: 1, 2, 3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16,17,18, 19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 
entryIds = ''




query = f'''
    {{
    entries(entry_ids:{entryIds}) {{
        entry{{ id }}
        struct{{
            pdbx_descriptor
        }}
    }}
    }}
'''
response = requests.get(url+query)

if response.status_code == 200:
    data = response.json()
    for oneentry in data["data"]["entries"]:
        print(oneentry["entry"]["id"],"|",oneentry["struct"]["pdbx_descriptor"])
        #Create folder
        folder_name = oneentry["struct"]["pdbx_descriptor"] # folder name is molecule family
        if folder_name is None: # if null
            folder_name = "DNF" # Create folder named Did Not Find
        folder_name = re.sub(r"[^a-zA-Z0-9]+", "", folder_name)[:30]
        path = os.path.join(directory, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)

        
        pdb_id = oneentry["entry"]["id"]
        save_coordinates_to_file(pdb_id , path )

else:
    print(f'Request failed with status code:{response.status_code} - {response.reason}')


print("done")