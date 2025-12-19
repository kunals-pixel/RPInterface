**Prerequisites: networkx, Biopython, ContactExtractor, mkdssp, urs2, x3dna**
Install dependencies: 
- “pip install networkx, biopython, os, re, csv, subprocess, requests, sys, pandas, matplotlib”
Install Contactextractor and for more information check https://github.com/febos/ContExt
- “pip install ContactExtractor”
Install dssp for protein secondary structure:
- “sudo apt-get install dssp”
For RNA secondary structure download usrlib2 and append (sys.path.append) the path at the top of the script_interface.py:
- git clone https://github.com/febos/urslib2.git”
Register and download x3dna-dssr binary from http://forum.x3dna.org/
- Add the path of x3dna binary to /path_to_urslib2/urslib2/config.py
Download Rfam mappings (Rfam.pdb.gz): https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/
Download Pfam mappings (pdb_pfam_mapping.txt): https://ftp.ebi.ac.uk/pub/databases/Pfam/mappings/


__Download PDBs containing nucleic acids__

- “python pdb_download.py” #Date used 01 Dec 2025
after successful execution it will generate a folder ‘PDB’


**Run script to save interfaces and generate tables**
Keep Rfam.pdb and pdb_pfam_mapping.txt in same folder as script_interfaces.py and PDB  then run the script to identify and save interfaces: 
- “python script_interfaces.py” or “python script_interfaces_parallel.py” #adjust MAX_WORKERS in the script according to your system.


