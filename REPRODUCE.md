**Prerequisites: networkx, biopython, ContactExtractor, mkdssp, urs2, x3dna**

Install dependencies: 
- “pip install networkx, biopython, os, re, csv, subprocess, requests, sys, pandas, matplotlib”

Install Contactextractor and for more information check https://github.com/febos/ContExt
- “pip install ContactExtractor”

Download and install dssp(mkdssp version 4.5.7) for protein secondary structure from the following address:
- https://github.com/PDB-REDO/dssp

For RNA secondary structure download usrlib2 and append (_sys.path.append_) the path at the top of the script_interface.py:
- git clone https://github.com/febos/urslib2.git”

Register and download x3dna-dssr binary from http://forum.x3dna.org/
- Add the path of x3dna binary to _"/path_to_urslib2/urslib2/config.py"_

Download Rfam mappings (Rfam.pdb.gz): https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/

Download Pfam mappings (pdb_pfam_mapping.txt): https://ftp.ebi.ac.uk/pub/databases/Pfam/mappings/


__Download PDBs containing nucleic acids__

- “python pdb_download.py”    
after successful execution it will generate a folder ‘PDB’. Structures were downloaded up to 01 Dec 2025. Change date in the script to current if required



**Identify and save interfaces**

Keep _Rfam.pdb_ and _pdb_pfam_mapping.txt_ in same folder as script_interfaces.py and folder PDB then run the script to identify and save interfaces: 

- “python script_interfaces.py” or
- “python script_interfaces_parallel.py”    _Number of threads can be changed by adjusting MAX_WORKERS in the script according to system._


