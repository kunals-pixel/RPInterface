**Prerequisites: networkx, Biopython, ContactExtractor, mkdssp, urs2, x3dna**

__Download PDBs containing nucleic acids__

“mkdir PDB”

“python pdb_download.py” #change the date to the present date

**Identify the complexes (protein-RNA/DNA)**

“python script_check_structures.py” #run in the folder where PDBs are downloaded

**Run script to save interfaces and generate tables**

"python script_interface_tables.py"
