import sys
sys.path.append("/home/kshewani/data/kshewani/projects/RPI/urs2/urslib2") #urslib2 path

TYPE_SYMBOLS_SRC = '''

AG	AG
AS	AS
AU	AU
BA	BA
BR	BR
BR3	BR
C	C
C01	C
C02	C
C03	C
C04	C
C05	C
C06	C
C07	C
C08	C
C09	C
C0B	C
C1	C
C1'	C
C1'1	C
C10	C
C11	C
C118	C
C12	C
C120	C
C121	C
C13	C
C14	C
C140	C
C141	C
C143	C
C144	C
C15	C
C16	C
C17	C
C18	C
C19	C
C1A	C
C1B	C
C1C	C
C1D	C
C1E	C
C1F	C
C1G	C
C1H	C
C1I	C
C1J	C
C1K	C
C1L	C
C1M	C
C1N	C
C1O	C
C1P	C
C1Q	C
C1R	C
C1S	C
C1T	C
C1U	C
C1V	C
C1W	C
C1X	C
C1Y	C
C2	C
C2'	C
C2'1	C
C20	C
C21	C
C22	C
C23	C
C24	C
C25	C
C26	C
C27	C
C28	C
C29	C
C2A	C
C2B	C
C2C	C
C2D	C
C2E	C
C2G	C
C2M	C
C2N	C
C2P	C
C2R	C
C3	C
C3'	C
C3'1	C
C30	C
C31	C
C32	C
C33	C
C34	C
C35	C
C36	C
C37	C
C38	C
C39	C
C3A	C
C3B	C
C3C	C
C3D	C
C3E	C
C3G	C
C3N	C
C3P	C
C3R	C
C3U	C
C4	C
C4'	C
C4'1	C
C40	C
C41	C
C42	C
C43	C
C44	C
C45	C
C46	C
C47	C
C48	C
C49	C
C4A	C
C4B	C
C4C	C
C4D	C
C4E	C
C4N	C
C4R	C
C5	C
C5'	C
C5'1	C
C50	C
C51	C
C52	C
C53	C
C54	C
C55	C
C56	C
C57	C
C58	C
C59	C
C5A	C
C5B	C
C5C	C
C5D	C
C5E	C
C5M	C
C5N	C
C5R	C
C6	C
C6'	C
C60	C
C61	C
C62	C
C63	C
C64	C
C65	C
C67	C
C68	C
C69	C
C6A	C
C6B	C
C6C	C
C6M	C
C6N	C
C7	C
C7'	C
C70	C
C71	C
C72	C
C73	C
C74	C
C75	C
C76	C
C77	C
C79	C
C7A	C
C7B	C
C7M	C
C7N	C
C7X	C
C8	C
C80	C
C81	C
C82	C
C83	C
C84	C
C85	C
C86	C
C87	C
C8A	C
C8B	C
C8C	C
C8M	C
C9	C
C91	C
C92	C
C93	C
C94	C
C9A	C
C9B	C
CA	C
CA'	C
CA1	C
CA2	C
CA3	C
CA4	C
CA5	C
CA6	C
CA7	C
CA8	C
CA9	C
CAA	C
CAB	C
CAC	C
CAD	C
CAE	C
CAF	C
CAG	C
CAH	C
CAI	C
CAJ	C
CAK	C
CAL	C
CAM	C
CAN	C
CAO	C
CAP	C
CAQ	C
CAR	C
CAS	C
CAT	C
CAU	C
CAV	C
CAW	C
CAX	C
CAY	C
CAZ	C
CB	C
CB'	C
CB1	C
CB2	C
CB3	C
CB4	C
CB5	C
CB6	C
CBA	C
CBB	C
CBC	C
CBD	C
CBE	C
CBF	C
CBG	C
CBH	C
CBI	C
CBK	C
CBM	C
CBN	C
CBO	C
CBP	C
CBQ	C
CBR	C
CBS	C
CBT	C
CBU	C
CBV	C
CBW	C
CBX	C
CBY	C
CBZ	C
CC	C
CC1	C
CC2	C
CC3	C
CC4	C
CC5	C
CC6	C
CD	C
CD1	C
CD2	C
CE	C
CE1	C
CE2	C
CE3	C
CG	C
CG1	C
CG2	C
CH2	C
CH3	C
CHA	C
CHB	C
CHC	C
CHD	C
CI3	C
CL	CL
CL1	CL
CL7	CL
CM	C
CM'	C
CM1	C
CM2	C
CM4	C
CM5	C
CM6	C
CM7	C
CN	C
CN1	C
CN7	C
CO	CO
CS	CS
CV'	C
CW'	C
CX'	C
CX3	C
CX4	C
CX5	C
CX6	C
CXD	C
CXE	C
CXF	C
CXG	C
CXN	C
CXO	C
CXP	C
CXQ	C
CY'	C
CZ	C
CZ'	C
CZ2	C
CZ3	C
F	F
F01	F
F1	F
F1'	F
F2	F
F2'	F
F20	F
F21	F
F22	F
F3	F
F3'	F
F4	F
F5	F
F61	F
F7	F
F8	F
FAI	F
FE	FE
H	H
H1	H
H1'	H
H1'1	H
H10	H
H101	H
H102	H
H103	H
H11	H
H111	H
H112	H
H12	H
H121	H
H122	H
H13	H
H131	H
H132	H
H14	H
H15	H
H16	H
H161	H
H162	H
H163	H
H17	H
H171	H
H172	H
H18	H
H181	H
H182	H
H183	H
H19	H
H1A	H
H1B	H
H1D	H
H2	H
H2'	H
H2''	H
H2'1	H
H20	H
H21	H
H22	H
H23	H
H24	H
H25	H
H26	H
H261	H
H262	H
H263	H
H27	H
H271	H
H272	H
H28	H
H281	H
H282	H
H283	H
H29	H
H2A	H
H2B	H
H2C	H
H2D	H
H2N	H
H2O1	H
H3	H
H3'	H
H3'1	H
H3'2	H
H31	H
H32	H
H33	H
H34	H
H35	H
H36	H
H361	H
H362	H
H363	H
H37	H
H371	H
H372	H
H38	H
H381	H
H382	H
H39	H
H3A	H
H3B	H
H3D	H
H3U1	H
H3U2	H
H3U3	H
H4	H
H4'	H
H4'1	H
H40	H
H41	H
H42	H
H45	H
H461	H
H462	H
H463	H
H471	H
H472	H
H481	H
H482	H
H4A	H
H4B	H
H4D	H
H4N	H
H5	H
H5'	H
H5''	H
H5'1	H
H5'2	H
H5'A	H
H51	H
H51A	H
H51N	H
H52	H
H52A	H
H52N	H
H5A1	H
H5A2	H
H5B1	H
H5B2	H
H5M	H
H5N	H
H6	H
H61	H
H61A	H
H62	H
H62A	H
H6L	H
H6M	H
H6N	H
H7	H
H71	H
H71N	H
H72	H
H72N	H
H73	H
H8	H
H81	H
H82	H
H83	H
H8A	H
H8C	H
H9	H
H91	H
H92	H
H93	H
H9C1	H
H9C2	H
HA	H
HA2	H
HA3	H
HAA	H
HAC	H
HAE	H
HAF	H
HAG	H
HAH	H
HAI	H
HAJ	H
HAK	H
HAL	H
HAM	H
HAN	H
HAO	H
HAP	H
HAR	H
HAS	H
HAT	H
HAU	H
HB	H
HB1	H
HB2	H
HB3	H
HD1	H
HD11	H
HD12	H
HD13	H
HD2	H
HD21	H
HD22	H
HD23	H
HD3	H
HE	H
HE1	H
HE2	H
HE21	H
HE22	H
HE3	H
HG	H
HG1	H
HG11	H
HG12	H
HG13	H
HG2	H
HG21	H
HG22	H
HG23	H
HG3	H
HH	H
HH11	H
HH12	H
HH2	H
HH21	H
HH22	H
HM'1	H
HM'2	H
HM'3	H
HM11	H
HM12	H
HM13	H
HM21	H
HM22	H
HM23	H
HM51	H
HM52	H
HM53	H
HM71	H
HM72	H
HM73	H
HN0	H
HN1	H
HN10	H
HN11	H
HN12	H
HN13	H
HN2	H
HN21	H
HN22	H
HN23	H
HN3	H
HN31	H
HN32	H
HN33	H
HN4	H
HN41	H
HN42	H
HN43	H
HN5	H
HN51	H
HN52	H
HN53	H
HN6	H
HN61	H
HN62	H
HN63	H
HN7	H
HN91	H
HO1	H
HO2	H
HO2'	H
HO2A	H
HO2B	H
HO2N	H
HO3	H
HO3'	H
HO3A	H
HO3B	H
HO3N	H
HO4	H
HO5	H
HO5'	H
HO6	H
HZ	H
HZ1	H
HZ2	H
HZ3	H
I	I
I5	I
IR	IR
K	K
LU	LU
MG	MG
MN	MN
N	N
N01	N
N02	N
N03	N
N04	N
N05	N
N06	N
N07	N
N08	N
N09	N
N0A	N
N1	N
N1'	N
N10	N
N11	N
N12	N
N13	N
N139	N
N14	N
N15	N
N16	N
N17	N
N19	N
N1A	N
N1B	N
N1C	N
N1N	N
N2	N
N2'	N
N20	N
N21	N
N22	N
N23	N
N24	N
N25	N
N26	N
N27	N
N28	N
N29	N
N2A	N
N2B	N
N3	N
N3'	N
N31	N
N32	N
N33	N
N34	N
N35	N
N37	N
N39	N
N3A	N
N3B	N
N3C	N
N4	N
N4'	N
N40	N
N41	N
N45	N
N49	N
N4A	N
N5	N
N50	N
N51	N
N52	N
N53	N
N58	N
N59	N
N6	N
N61	N
N62	N
N63	N
N64	N
N6A	N
N6C	N
N7	N
N71	N
N72	N
N7A	N
N7B	N
N7C	N
N7N	N
N8	N
N82	N
N9	N
N91	N
N9A	N
N9B	N
N9C	N
NA	NA
NA2	N
NA7	N
NAA	N
NAB	N
NAC	N
NAE	N
NAG	N
NAH	N
NAK	N
NAL	N
NAM	N
NAR	N
NAS	N
NAT	N
NAW	N
NB	N
NB1	N
NB4	N
NBD	N
NBE	N
NBF	N
NBG	N
NBH	N
NBI	N
NBJ	N
NBK	N
NBL	N
NBN	N
NBP	N
NBQ	N
NBV	N
NC	N
NC1	N
NC4	N
NC6	N
NCA	N
NCB	N
NCC	N
NCD	N
ND	N
ND1	N
ND2	N
NE	N
NE1	N
NE2	N
NF1	N
NH1	N
NH2	N
NI	NI
NXT	N
NXU	N
NXV	N
NXW	N
NZ	N
NZ'	N
O	O
O01	O
O02	O
O03	O
O04	O
O05	O
O06	O
O07	O
O08	O
O09	O
O1	O
O1'	O
O10	O
O11	O
O12	O
O13	O
O14	O
O142	O
O15	O
O16	O
O17	O
O18	O
O19	O
O1A	O
O1B	O
O1C	O
O1D	O
O1G	O
O1N	O
O1S	O
O1V	O
O1X	O
O2	O
O2'	O
O2'1	O
O20	O
O21	O
O22	O
O23	O
O24	O
O25	O
O27	O
O28	O
O29	O
O2A	O
O2B	O
O2C	O
O2D	O
O2E	O
O2G	O
O2N	O
O2R	O
O2S	O
O2V	O
O2X	O
O3	O
O3'	O
O3'1	O
O30	O
O31	O
O32	O
O33	O
O34	O
O35	O
O36	O
O39	O
O3A	O
O3B	O
O3C	O
O3D	O
O3E	O
O3G	O
O3P	O
O3R	O
O3S	O
O3X	O
O4	O
O4'	O
O4'1	O
O40	O
O41	O
O42	O
O43	O
O44	O
O45	O
O48	O
O4A	O
O4B	O
O4D	O
O4E	O
O4P	O
O4R	O
O5	O
O5'	O
O5'1	O
O50	O
O51	O
O52	O
O53	O
O54	O
O56	O
O58	O
O5A	O
O5B	O
O5D	O
O5E	O
O5P	O
O5R	O
O6	O
O61	O
O62	O
O63	O
O66	O
O6A	O
O6B	O
O6P	O
O6R	O
O7	O
O72	O
O74	O
O78	O
O7A	O
O7N	O
O7R	O
O8	O
O80	O
O83	O
O85	O
O86	O
O8A	O
O8R	O
O9	O
OA1	O
OA4	O
OA5	O
OA6	O
OA8	O
OAB	O
OAC	O
OAD	O
OAE	O
OAF	O
OAG	O
OAH	O
OAI	O
OAS	O
OAT	O
OAU	O
OAV	O
OAX	O
OAY	O
OAZ	O
OB1	O
OB2	O
OB3	O
OB6	O
OBA	O
OBB	O
OBD	O
OBE	O
OBI	O
OBJ	O
OBL	O
OBR	O
OBU	O
OC	O
OC1	O
OC2	O
OC3	O
OCA	O
OCB	O
OD1	O
OD2	O
ODA	O
ODB	O
OE1	O
OE2	O
OG	O
OG1	O
OG2	O
OH	O
OH2	O
OH3	O
OH4	O
OH5	O
OH6	O
OH7	O
OM5	O
OM7	O
ON1	O
ON2	O
OO	O
OP	O
OP1	O
OP11	O
OP2	O
OP21	O
OP3	O
OP4	O
OP5	O
OP6	O
OS	OS
OW'	O
OX'	O
OXT	O
OY'	O
P	P
P'	P
P01	P
P02	P
P03	P
P1	P
P11	P
P2	P
P22	P
P26	P
P3	P
P30	P
PA	P
PAX	P
PAZ	P
PB	P
PBK	P
PBR	P
PBS	P
PC	P
PD	P
PG	P
PN	P
RH	RH
S	S
S1	S
S10	S
S15	S
S2	S
S2'	S
S23	S
S26	S
S2P	S
S3P	S
S4	S
S4'	S
S6	S
SD	S
SE	SE
SE1	SE
SE2	SE
SE2'	SE
SE4	SE
SG	S
SM	SM
SP1	S
SP2	S
SR	SR
TB	TB
TL	TL
U	U
UNK	X
V	V
ZN	ZN
'''

TYPE_SYMBOLS = {x.split()[0]:x.split()[1] for x in TYPE_SYMBOLS_SRC.strip().split('\n')}


def Atom(idstr):
    '''"1.A.G.22.B" -> Atom dict:
       atom = {"pdbx_PDB_model_num" : '1',
               "auth_asym_id"       : 'A',
               "auth_comp_id"       : 'G',
               "auth_seq_id"        : '22',
               "pdbx_PDB_ins_code"  : 'B',
              }
    '''

    splt = idstr.split('.')
    assert len(splt) == 5, "Incorrect DSSR-like id string: {}".format(idstr)

    atom = {"pdbx_PDB_model_num": splt[0],
            "auth_asym_id"      : splt[1],
            "auth_comp_id"      : splt[2],
            "auth_seq_id"       : splt[3],
            "pdbx_PDB_ins_code" : splt[4],
            }

    return atom


def WriteAtomToPDB(atom):
    """
    https://www.wwpdb.org/documentation/file-format-content/format33/sect9.html#ATOM
    COLUMNS        DATA  TYPE    FIELD        DEFINITION
    -------------------------------------------------------------------------------------
     1 -  6        Record name   "ATOM  "
     7 - 11        Integer       serial       Atom  serial number.
    13 - 16        Atom          name         Atom name.
    17             Character     altLoc       Alternate location indicator.
    18 - 20        Residue name  resName      Residue name.
    22             Character     chainID      Chain identifier.
    23 - 26        Integer       resSeq       Residue sequence number.
    27             AChar         iCode        Code for insertion of residues.
    31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
    39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
    47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
    55 - 60        Real(6.2)     occupancy    Occupancy.
    61 - 66        Real(6.2)     tempFactor   Temperature  factor.
    77 - 78        LString(2)    element      Element symbol, right-justified.
    79 - 80        LString(2)    charge       Charge  on the atom.
    """

    res = "ATOM  "
    atomid = str(atom['id'] % 10**5)
    res += ' '*(5 - len(atomid)) + atomid
    res += ' '

    atom['type_symbol'] = TYPE_SYMBOLS[atom['auth_atom_id']]

    if len(atom["auth_atom_id"]) == 4:
        res += atom["auth_atom_id"]
    else:
        half1 = atom["type_symbol"]
        half2 = atom["auth_atom_id"][len(atom["type_symbol"]):]
        res += ' '*(2 - len(half1)) + half1
        res += half2 + ' '*(2-len(half2))

    res += ' ' #label_alt_id

    res += ' '*(3 - len(atom["auth_comp_id"])) + atom["auth_comp_id"]

    res += ' '*(2 - len(atom["auth_asym_id"])) + atom["auth_asym_id"]

    residue_id = str(int(atom["auth_seq_id"]) % 10**4)
    res += ' '*(4 - len(residue_id)) + residue_id

    res += ' '*(1 - len(atom["pdbx_PDB_ins_code"])) + atom["pdbx_PDB_ins_code"]

    res += ' ' * 3
    
    for Cartn_coord in ("Cartn_x", "Cartn_y", "Cartn_z"):
        coord = "{:.3f}".format(round(atom[Cartn_coord], 3))
        res += ' '*(8 - len(coord)) + coord

    occup = "{:.2f}".format(round(atom["occupancy"], 2))
    res += ' '*(6 - len(occup)) + occup

    bfactor = "{:.2f}".format(round(atom["B_iso_or_equiv"], 2))
    res += ' '*(6 - len(bfactor)) + bfactor

    res += ' ' * 10

    res += ' '*(2 - len(atom["type_symbol"])) + atom["type_symbol"]

    res += ' ' * 2 #pdbx_formal_charge

    return res


def WriteTER(atom):

    res = ""
    res += "TER" + " "*3

    atomid = str(atom['id'] % 10**5)
    res += ' '*(5 - len(atomid)) + atomid

    res += ' ' * 6

    res += ' '*(3 - len(atom["auth_comp_id"])) + atom["auth_comp_id"]

    res += ' '*(2 - len(atom["auth_asym_id"])) + atom["auth_asym_id"]

    residue_id = str(int(atom["auth_seq_id"]) % 10**4)
    res += ' '*(4 - len(residue_id)) + residue_id

    res += ' '*(1 - len(atom["pdbx_PDB_ins_code"])) + atom["pdbx_PDB_ins_code"]

    return res
    

def WriteToPDB(entry, file):

    if not entry['IDLIST']:
        raise Exception("ERROR: entry IDLIST field is empty (WriteToPDB)")

    # get model identifiers and sort them
    models = set()
    for idstr in entry['IDLIST']:
        try:
            models.add(int(Atom(idstr)["pdbx_PDB_model_num"]))
        except:
            pass # ignore non-int models, set them to 1 later
    if not models: # if no integer models, consider everything model 1
        models.add(1) 
    models = [str(m) for m in sorted(models)]

    # Handle chain identifiers longer than 2-letter
    # By renaming all chains from A to zz
    newchains = {}
    if any(len(Atom(idstr)["auth_asym_id"]) > 2
           for idstr in entry['IDLIST']):
        chaincount = 0
        for idstr in entry['IDLIST']:
            chain = Atom(idstr)["auth_asym_id"]
            if chain not in newchains:
                newchains[chain] = IntToChain(chaincount)
                chaincount += 1        

    with open(file, 'w') as outp:

        # if renaming chains
        if newchains:
            outp.write("REMARK 250 RENAMED CHAINS:" + '\n')
            for chain in sorted(newchains.keys()):
                outp.write("REMARK 250 {} -> {}".format(chain, newchains[chain]) + '\n')
        
        for model in models:

            atomcount = 1
            prevatom  = None
            outp.write("MODEL        {} \n".format(model))

            for idstr in entry['IDLIST']:
                atom = Atom(idstr)

                # default occupancy and B-factor
                atom["occupancy"]      = 1.00 
                atom["B_iso_or_equiv"] = 0.00

                # if renaming chains
                if newchains:
                    atom["auth_asym_id"] = newchains[atom["auth_asym_id"]]
                
                # if uncertain model -> set to 1
                if not atom["pdbx_PDB_model_num"].isdigit():
                    atom["pdbx_PDB_model_num"] = '1'
                # skip residues from other models
                if atom["pdbx_PDB_model_num"] != model:
                    continue

                # Print TER line if new chain
                if atomcount > 1:
                    if atom['auth_asym_id'] != prevatom['auth_asym_id']:
                        outp.write(WriteTER(prevatom)+'\n')
                
                for atom_id in entry['IDDICT'][idstr]['ATOMS']:
                            
                    atom['id'] = atomcount
                    atomcount += 1

                    atom['auth_atom_id'] = atom_id
                    atom['Cartn_x'] = entry['IDDICT'][idstr][atom_id][0]
                    atom['Cartn_y'] = entry['IDDICT'][idstr][atom_id][1]
                    atom['Cartn_z'] = entry['IDDICT'][idstr][atom_id][2]

                    outp.write(WriteAtomToPDB(atom)+'\n')

                prevatom = {k:v for k,v in atom.items()}
      
            # Print TER line after the last atom in the model
            outp.write(WriteTER(atom)+'\n')

            outp.write("ENDMDL\n")
        outp.write("END\n")          



def WriteToCIF(entry, file):

    if not entry['IDLIST']:
        raise Exception("ERROR: entry IDLIST field is empty (WriteToCIF)")

    title = ["group_PDB",
             "id",
             "type_symbol",
             "label_atom_id",
             "label_alt_id",
             "label_comp_id",
             "label_asym_id",
             "label_entity_id",
             "label_seq_id",
             "pdbx_PDB_ins_code",
             "Cartn_x",
             "Cartn_y",
             "Cartn_z",
             "occupancy",
             "B_iso_or_equiv",
             "pdbx_formal_charge",
             "auth_seq_id",
             "auth_comp_id",
             "auth_asym_id",
             "auth_atom_id",
             "pdbx_PDB_model_num",
             ]

    atomcount    = 1
    residuecount = 1

    entities = {} # derive entity_id as index of the (model, chain) pair

    with open(file, 'w') as outp:

        outp.write("#\nloop_\n")

        for col in title:
            outp.write("_atom_site."+col+'\n')

        for idstr in entry['IDLIST']:
            atom = Atom(idstr)

            atom["group_PDB"] = "ATOM"
            atom["label_seq_id"] = residuecount
            residuecount += 1

            # default occupancy and B-factor
            atom["occupancy"]      = 1.00 
            atom["B_iso_or_equiv"] = 0.00

            # if uncertain model -> set to 1
            if not atom["pdbx_PDB_model_num"].isdigit():
                atom["pdbx_PDB_model_num"] = '1'

            if (atom["pdbx_PDB_model_num"],
                atom["auth_asym_id"]) not in entities:
                entity_id = len(entities) + 1
                entities[(atom["pdbx_PDB_model_num"],
                          atom["auth_asym_id"])] = entity_id

            atom["label_entity_id"] = entities[(atom["pdbx_PDB_model_num"],
                                                atom["auth_asym_id"])]
            atom["label_alt_id"]  = '.'
            atom["label_comp_id"] = atom["auth_comp_id"]
            atom["label_asym_id"] = atom["auth_asym_id"]

            # avoid empty strings
            for col in title:
                if col not in atom or not str(atom[col]).strip():
                    atom[col] = '?'
                
            for atom_id in entry['IDDICT'][idstr]['ATOMS']:
                            
                atom['id'] = atomcount
                atomcount += 1

                atom['auth_atom_id']  = atom_id
                atom["label_atom_id"] = atom['auth_atom_id']

                if atom['auth_atom_id'] == 'CA' and atom["label_comp_id"] == 'CA':
                    atom['type_symbol'] = 'CA'
                else:                    
                    atom['type_symbol']   = TYPE_SYMBOLS[atom['auth_atom_id']]
                
                atom['Cartn_x'] = entry['IDDICT'][idstr][atom_id][0]
                atom['Cartn_y'] = entry['IDDICT'][idstr][atom_id][1]
                atom['Cartn_z'] = entry['IDDICT'][idstr][atom_id][2]

                outp.write(' '.join([str(atom[col]) for col in title]) + '\n')

        outp.write("#\n")


def DSSRidstr(atom):
    '''1.A.G.22.B - DSSR-like id string
       [model.chain.res.resnum.inscode]'''
    return '.'.join([str(x) for x in [atom["pdbx_PDB_model_num"],
                                      atom["auth_asym_id"],
                                      atom["auth_comp_id"],
                                      atom["auth_seq_id"],
                                      atom["pdbx_PDB_ins_code"]]])

def GuessFormat(filepath):
    """Determine the format of a file -> 'cif' or 'pdb' """

    pdb = 0
    cif = 0

    with open(filepath) as file:
        for line in file:
            if line.startswith('#'):
                cif += 1
            elif line.startswith('_atom.site'):
                cif += 1
            elif line.startswith('loop_'):
                cif += 1
            elif line.startswith('END'):
                pdb += 1
            elif line.startswith('MODEL'):
                pdb += 1
            elif line.startswith('TER'):
                pdb += 1
            elif line.startswith('CONECT'):
                pdb += 1
            
                
    return ['pdb','cif'][int(cif > pdb)]

def ParseAtomPDB(line):
    '''https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html'''
    
    atom = {}
    atom["group_PDB"]          = line[:6].strip()
    atom["id"]                 = int(line[6:11])
    atom["auth_atom_id"]       = line[12:16].strip()
    atom["label_alt_id"]       = line[16].strip()
    atom["auth_comp_id"]       = line[17:20].strip()
    atom["auth_asym_id"]       = line[20:22].strip()
    atom["auth_seq_id"]        = int(line[22:26])
    atom["pdbx_PDB_ins_code"]  = line[26].strip()
    atom["Cartn_x"]            = float(line[30:38])
    atom["Cartn_y"]            = float(line[38:46])
    atom["Cartn_z"]            = float(line[46:54])
    atom["occupancy"]          = float(line[54:60]) if line[54:60].strip() else float("nan")
    atom["B_iso_or_equiv"]     = float(line[60:66]) if line[60:66].strip() else float("nan")
    atom["type_symbol"]        = line[76:78].strip()
    atom["pdbx_formal_charge"] = line[78:80].strip()

    # Convert SPDBV asterisks into prime symbols
    atom["auth_atom_id"] = atom["auth_atom_id"].replace('*',"'")
    # Convert SPDBV phosphate oxygen format O1P -> OP1, O2P -> OP2
    atom["auth_atom_id"] = atom["auth_atom_id"].replace('O1P','OP1').replace('O2P','OP2')

    if atom["pdbx_PDB_ins_code"] == '?':
        atom["pdbx_PDB_ins_code"] = ''

    if atom["pdbx_formal_charge"] == '?':
        atom["pdbx_formal_charge"] = ''

    if atom["label_alt_id"] == '.':
        atom["label_alt_id"] = ''

    return atom

def ParsePDB(filepath):
    '''https://mmcif.wwpdb.org/docs/pdb_to_pdbx_correspondences.html#ATOMP'''

    # By default, the model is set to 1
    model  = "1"

    title1 = ["group_PDB","id","auth_atom_id",
             "label_alt_id","auth_comp_id","auth_asym_id",
             "auth_seq_id","pdbx_PDB_ins_code","Cartn_x",
             "Cartn_y","Cartn_z","occupancy",
             "B_iso_or_equiv","type_symbol","pdbx_formal_charge"]
    title2 = ["label_asym_id","label_atom_id","label_comp_id",
              "label_entity_id","label_seq_id","pdbx_PDB_model_num"]

    titlei = {x:i for i,x in enumerate(title1+title2)}

    residuelst, residuedct = [], {}

    with open(filepath) as file:
        for line in file:
            if line.startswith('ATOM') or line.startswith('HETATM'):

                atom = ParseAtomPDB(line)

                atom["pdbx_PDB_model_num"] = model
                atom["label_asym_id"] = atom["auth_asym_id"]
                atom["label_atom_id"] = atom["auth_atom_id"]
                atom["label_comp_id"] = atom["auth_comp_id"]
                atom["label_seq_id"]  = atom["auth_seq_id"]
                atom['DSSR']          = DSSRidstr(atom)

                # new residue found
                if atom['DSSR'] not in residuedct:
                    residuelst.append(atom['DSSR'])
                    residuedct[atom['DSSR']] = {'ATOMS': []}
                    
                residue = residuedct[atom['DSSR']]
                # new atom found (otherwise we have a new altloc for an already found atom)
                if atom['auth_atom_id'] not in residue:
                    residue['ATOMS'].append(atom['auth_atom_id'])
                # consider only the last altloc version of the atom and ignore all the previous ones
                residue[atom['auth_atom_id']] = [atom[t] for t in ["Cartn_x", "Cartn_y", "Cartn_z"]]
                
            elif line.startswith('MODEL'):
                model = line.strip().split()[-1]

    Entry = {'IDLIST': residuelst,
             'IDDICT': residuedct}

    return Entry


def ParseAtomCIF(line, title):

    linesplit = line.strip().split()
    atom = {title[i]:linesplit[i] for i in range(len(title))}

    for frag in ("atom", "comp", "asym", "seq"):

        auth  =  "auth_{}_id".format(frag)
        label = "label_{}_id".format(frag)
        
        if auth not in atom and label in atom:
            atom[auth] = atom[label]
        elif label not in atom and auth in atom:
            atom[label] = atom[auth]

    # Convert all integers from strings
    for int_token in ("id", "auth_seq_id"):
        atom[int_token] = int(atom[int_token]) if int_token in atom else float("nan")

    # By default, the model is set to 1
    atom["pdbx_PDB_model_num"] = int(atom["pdbx_PDB_model_num"])\
                                 if "pdbx_PDB_model_num" in atom and\
                                 atom["pdbx_PDB_model_num"].isdigit() else 1

    # Convert all floats from strings
    for float_token in ("Cartn_x", "Cartn_y", "Cartn_z","occupancy","B_iso_or_equiv"):
        atom[float_token] = float(atom[float_token]) if float_token in atom else float("nan")
    
    if      "auth_atom_id"  not in atom: atom["auth_atom_id"]       = ''
    if     "label_atom_id"  not in atom: atom["label_atom_id"]      = ''
    if      "label_alt_id"  not in atom: atom["label_alt_id"]       = ''
    if      "auth_comp_id"  not in atom: atom["auth_comp_id"]       = ''
    if     "label_comp_id"  not in atom: atom["label_comp_id"]      = ''
    if      "auth_asym_id"  not in atom: atom["auth_asym_id"]       = ''
    if "pdbx_PDB_ins_code"  not in atom: atom["pdbx_PDB_ins_code"]  = ''
    if "pdbx_formal_charge" not in atom: atom["pdbx_formal_charge"] = ''

    if atom["pdbx_PDB_ins_code"] == '?':
        atom["pdbx_PDB_ins_code"] = ''

    if atom["pdbx_formal_charge"] == '?':
        atom["pdbx_formal_charge"] = ''

    if atom["label_alt_id"] == '.':
        atom["label_alt_id"] = ''

    # Strip double quotes for cases like this: "O3'"
    atom["auth_atom_id"] = atom["auth_atom_id"].strip('"') 
    atom["label_atom_id"] = atom["label_atom_id"].strip('"')

    # Convert SPDBV asterisks into prime symbols
    atom["auth_atom_id"]  = atom["auth_atom_id"].replace('*',"'")
    atom["label_atom_id"] = atom["label_atom_id"].replace('*',"'")
    # Convert SPDBV phosphate oxygen format O1P -> OP1, O2P -> OP2
    atom["auth_atom_id"]  = atom["auth_atom_id"].replace('O1P','OP1').replace('O2P','OP2')
    atom["label_atom_id"] = atom["label_atom_id"].replace('O1P','OP1').replace('O2P','OP2')

    return atom


def ParseCIF(filepath):
    
    title  = []
    titlei = None

    residuelst, residuedct = [], {}

    with open(filepath) as file:
        for line in file:
            if line.startswith("_atom_site."):
                title.append(line.strip().split('.')[-1])

            elif line.startswith('ATOM') or line.startswith('HETATM'):

                atom = ParseAtomCIF(line, title)

                if not titlei:

                    title2 = [k for k in atom if k not in title]
                    finaltitle  = title + title2
                    titlei = {x:i for i,x in enumerate(finaltitle)}

                atom['DSSR'] = DSSRidstr(atom)

                # new residue found
                if atom['DSSR'] not in residuedct:
                    residuelst.append(atom['DSSR'])
                    residuedct[atom['DSSR']] = {'ATOMS': []}

                residue = residuedct[atom['DSSR']]
                # new atom found (otherwise we have a new altloc for an already found atom)
                if atom['auth_atom_id'] not in residue:
                    residue['ATOMS'].append(atom['auth_atom_id'])
                # consider only the last altloc version of the atom and ignore all the previous ones
                residue[atom['auth_atom_id']] = [atom[t] for t in ["Cartn_x", "Cartn_y", "Cartn_z"]]
                
            elif line.startswith('MODEL'):
                model = line.strip().split()[-1]

    Entry = {'IDLIST': residuelst,
             'IDDICT': residuedct}

    return Entry


def FileToEntry(filepath, fileformat = None):
    """Parse an input file into a PDB entry dictionary:
    Entry = {'IDLIST': [idstr1, idstr2, ...],
             'IDDICT': {idstr1: {'ATOMS' : ['N1','C2', ...],
                                 'N1': [X, Y, Z],
                                 ...}
                       ...}
            }
    """
    # Decide on the file format
    if not fileformat or fileformat.lower() not in {'pdb', 'cif', 'mmcif'}:
        fileformat = GuessFormat(filepath)
    else:
        fileformat = fileformat.lower().replace('mmcif','cif')

    # Parse the file
    try:
        if fileformat == 'pdb':
            Entry = ParsePDB(filepath)
        else:
            Entry = ParseCIF(filepath)
    except Exception as err:
        print("ERROR: failed to parse {}-format data from {}"\
              .format(fileformat.upper(),filepath))
        raise err

    return Entry


def EntryToFile(entry, filepath, fileformat = None):
    """ Print an input entry into a file (filepath)
        in PDB/mmCIF format (fileformat)
        By default, if the format is not specified by the user,
        it will be determined based on the file extension or,
        if it cannot be done, the format will be set to PDB."""

    #If None, get from the file extension
    if not fileformat:
        fileformat = filepath.split('.')[-1]

    # to lowercase
    fileformat = fileformat.lower()

    # if uncertain, set to pdb
    if fileformat not in ('pdb','cif','mmcif'):
        fileformat = 'pdb'

    try:
        if fileformat == 'pdb':
            WriteToPDB(entry, filepath)
        else:
            WriteToCIF(entry, filepath)
        return 0
    except Exception as err:
        print("ERROR: failed to print an entry in {} format to {}"\
              .format(fileformat.upper(), filepath))
        raise err


def SaveInterfaces(filepath, interfaces):

    entry = FileToEntry(filepath)

    all_dssrs = entry['IDLIST'].copy()

    for dssrs,filename in interfaces:
        dssrs_set = set(dssrs)
        entry['IDLIST'] = [dssr for dssr in all_dssrs if dssr in dssrs_set]
        EntryToFile(entry,filename, filename.split('.')[-1])



'''
if __name__ == "__main__":

    
    filepath = "4v88.cif"

    interfaces = [
                  [['1.A5.C.573.', '1.DS.LYS.5.'], '4v88_1.cif'],
                  [['1.A2.A.1384.', '1.AU.LYS.32.'], '4v88_2.cif'],
                  [['1.A5.C.497.', '1.De.LYS.8.'], '4v88_3.cif'],
                  ]

    SaveInterfaces(filepath, interfaces)
'''


import os, re, csv, subprocess, requests, sys
import networkx as nx
from collections import defaultdict
from ContactExtractor import ContExt
from Bio.PDB import PDBParser, MMCIFParser, is_aa

def extract_metadata(filename):
    """
    Extracts experimental method, resolution, and chain composition (Protein, RNA, DNA)
    from PDB or mmCIF structure file using Biopython.
    Only the FIRST MODEL is used for chain and residue counting.
    """

    try:
        ext = os.path.splitext(filename)[1].lower()

        # --- Parse structure ---
        if ext == ".cif":
            parser = MMCIFParser(QUIET=True)
            structure = parser.get_structure("temp", filename)
            mmcif_dict = parser._mmcif_dict  # contains header data
            method = mmcif_dict.get("_exptl.method", ["Unknown"])[0] if "_exptl.method" in mmcif_dict else "Unknown"
            resolution = mmcif_dict.get("_refine.ls_d_res_high", ["Unknown"])[0] if "_refine.ls_d_res_high" in mmcif_dict else "Unknown"

        elif ext == ".pdb":
            parser = PDBParser(QUIET=True)
            structure = parser.get_structure("temp", filename)
            method, resolution = "Unknown", "Unknown"
            with open(filename) as f:
                for line in f:
                    if line.startswith("EXPDTA"):
                        method = line.strip().replace("EXPDTA", "").strip()
                    elif line.startswith("REMARK   2 RESOLUTION."):
                        parts = line.split()
                        for p in parts:
                            if "ANGSTROMS" in p.upper():
                                try:
                                    resolution = float(parts[3])
                                except Exception:
                                    pass

        else:
            return "Unknown", "Unknown", "Unknown"

        # --- Format resolution ---
        if resolution not in [None, "Unknown", "?"]:
            try:
                resolution = f"{float(resolution):.2f} Å"
            except ValueError:
                pass

        # --- Residue category definitions ---
        AMINO_ACIDS = {
            'ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE',
            'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL'
        }
        RNA_BASES = {'A', 'C', 'G', 'U', 'T'}
        DNA_BASES = {'DA', 'DC', 'DG', 'DT', 'DU'}

        prot_chains, rna_chains, dna_chains = [], [], []
        prot_res, rna_res, dna_res = 0, 0, 0

        # --- ONLY FIRST MODEL ---
        try:
            first_model = structure[0]
        except Exception:
            return method, resolution, "Unknown"

        # Count chains & residues from first model only
        for chain in first_model:
            residues = [r for r in chain.get_residues() if r.id[0] == ' ']
            resnames = {r.get_resname().strip() for r in residues}

            if any(rn in AMINO_ACIDS for rn in resnames):
                prot_chains.append(chain.id)
                prot_res += len(residues)

            elif any(rn in RNA_BASES - DNA_BASES for rn in resnames):
                rna_chains.append(chain.id)
                rna_res += len(residues)

            elif any(rn in DNA_BASES for rn in resnames):
                dna_chains.append(chain.id)
                dna_res += len(residues)

        # --- Build summary string ---
        chain_summary_parts = []
        if prot_chains:
            chain_summary_parts.append(f"Protein:{len(prot_chains)}({prot_res})")
        if rna_chains:
            chain_summary_parts.append(f"RNA:{len(rna_chains)}({rna_res})")
        if dna_chains:
            chain_summary_parts.append(f"DNA:{len(dna_chains)}({dna_res})")

        chain_summary = ", ".join(chain_summary_parts) if chain_summary_parts else "Unknown"

        return method, resolution, chain_summary

    except Exception as e:
        print(f"Warning: Could not extract metadata from {filename}: {e}")
        return "Unknown", "Unknown", "Unknown"

def contacts_extraction(structure_file):
    """
    Extracts pairwise contacts from a structure file using ContExt.
    Replaces underscores with dots in residue IDs before returning.
    """
    
    residue_mask = ""#1:A #1:C #1:G #1:T #1:U #1:DA #1:DC #1:DG #1:DT #1:DU #1:ALA #1:ARG #1:ASN #1:ASP #1:CYS #1:GLN #1:GLU #1:GLY #1:HIS #1:ILE #1:LEU #1:LYS #1:MET #1:PHE #1:PRO #1:SER #1:THR #1:TRP #1:TYR #1:VAL #1:1MA #1:2MG #1:6MZ #1:7MG #1:A2M #1:MA6 #1:OMG  #1:YYG #1:SAM #1:4AC #1:4SU #1:5MC #1:5MU #1:LV2 #1:OMC #1:OMU #1:SSU #1:UR3 #1:PSU #1:B8N #1:3TD #1:UY1 #1:CDP #1:UDP #1:ADP #1:GDP #1:CTP #1:UTP #1:ATP #1:GTP " "
    
    pairwise_contacts = ContExt(
        inpfile1=structure_file, 
        RANGE=6.0, 
        mask1=residue_mask, 
        mask2=residue_mask
    )
    
    # Replace underscores with dots in residue IDs
    updated_contacts = [
        (dist, atom1.replace("_", "."), atom2.replace("_", "."))
        for dist, atom1, atom2 in pairwise_contacts
    ]
    #print(updated_contacts)
    return updated_contacts


    # --- helper: run mkdssp and parse mmcif output to produce an SS map ---
def get_prot_ss_map(structure_fname):
    prot_ss_map = {}
    try:
        out_dir = "pdb_dssp"
        os.makedirs(out_dir, exist_ok=True)
        base = os.path.basename(structure_fname)
        out_name = os.path.splitext(base)[0] + "_dssp.cif"
        out_path = os.path.join(out_dir, out_name)

        cmd = ["mkdssp", "--output-format", "mmcif", structure_fname, out_path]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        headers, records = [], []
        with open(out_path, "r") as fh:
            in_loop = False
            for line in fh:
                line_strip = line.rstrip("\n")
                if line_strip.startswith("loop_"):
                    in_loop = True
                    headers = []
                    continue
                if in_loop and line_strip.startswith("_dssp_struct_summary."):
                    headers.append(line_strip.strip())
                    continue
                if in_loop and headers and not line_strip.startswith("_"):
                    parts = line_strip.split()
                    if len(parts) < len(headers):
                        parts += [None] * (len(headers) - len(parts))
                    rec = dict(zip(headers, parts))
                    records.append(rec)
                    continue
                if in_loop and headers and line_strip == "":
                    break

        for rec in records:
            chain = rec.get("_dssp_struct_summary.label_asym_id")
            seq_id = rec.get("_dssp_struct_summary.label_seq_id")
            comp_id = rec.get("_dssp_struct_summary.label_comp_id")
            ss = rec.get("_dssp_struct_summary.secondary_structure")
            if chain is None or seq_id is None or comp_id is None:
                continue
            ss_char = ss if ss and ss not in {".", "?", ""} else "C"
            key = f"#1/{chain}:{comp_id}.{seq_id}"
            prot_ss_map[key] = ss_char

        return prot_ss_map

    except FileNotFoundError:
        print("Warning: 'mkdssp' not found. Secondary structure defaulting to coil (C).")
        return {}
    except subprocess.CalledProcessError as e:
        print(f"Warning: mkdssp failed on {structure_fname}: {e}")
        return {}
    except Exception as e:
        print(f"Warning: failed to parse mkdssp output for {structure_fname}: {e}")
        return {}

    # --- fetch Pfam ID map ---

def get_pfam_for_structure(structure_file, mapping_file="pdb_pfam_mapping.txt"):

    # --- utility for clean string ---
    def clean(s):
        return s.strip().lower().replace("\ufeff", "") if isinstance(s, str) else ""

    # --- read mapping file into rows ---
    def read_mapping_file(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = [line for line in f if line.strip() and not line.startswith("#")]
            if not lines:
                raise ValueError("Mapping file contains no usable data.")

            header_line = lines[0].strip()
            delimiter = "\t" if "\t" in header_line else None

            if delimiter:
                reader = csv.DictReader(lines, delimiter=delimiter)
                rows = [dict((k.strip(), v.strip()) for k, v in row.items()) for row in reader]
            else:
                parts = [line.split() for line in lines]
                header = [h.strip() for h in parts[0]]
                rows = [dict(zip(header, row)) for row in parts[1:]]

        return rows

    # --- normalize structure name ---
    structure_name = clean(os.path.basename(structure_file).split('.')[0])

    # --- process mapping rows ---
    pfam_map = {}
    rows = read_mapping_file(mapping_file)

    for row in rows:
        pdb_id = clean(row.get("PDB"))
        if pdb_id != structure_name:
            continue  # skip irrelevant rows

        chain = row.get("CHAIN", "").strip()
        pfam_id = row.get("PFAM_ACCESSION", "").strip()
        pfam_name = row.get("PFAM_NAME", "").strip()

        # PDB_START / PDB_END define domain boundaries in PDB numbering
        try:
            start = int(row.get("PDB_START", "").strip())
            end = int(row.get("PDB_END", "").strip())
        except:
            continue  # malformed row → skip

        if chain and pfam_id:
            entry = {
                "pfam_id": pfam_id,
                "pfam_name": pfam_name,
                "start": start,
                "end": end
            }
            pfam_map.setdefault(chain.upper(), []).append(entry)

    return pfam_map

    # --- read Rfam IDs from file ---
def fetch_rfam_mapping(rfam_file, structure_name):
    """Returns a dict: chain -> list of Rfam IDs for the given PDB structure"""
    chain_to_rfam = defaultdict(list)
    pdb_id = os.path.splitext(os.path.basename(structure_name))[0].lower()  # e.g., "1vql"
    if not os.path.exists(rfam_file):
        print(f"Warning: Rfam file '{rfam_file}' not found.")
        return {}
    with open(rfam_file) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("rfam_acc"):
                continue
            parts = line.split()
            if len(parts) < 3:
                continue
            rfam_acc, pdb_entry, chain = parts[0], parts[1].lower(), parts[2]
            if pdb_entry != pdb_id:
                continue
            chain_to_rfam[chain].append(rfam_acc)
     #print(list((ch, sorted(set(ids))) for ch, ids in chain_to_rfam.items()))
    return {ch: sorted(set(ids)) for ch, ids in chain_to_rfam.items()}

#sys.path.append("/home/kshewani/projects/RPI/urs2")
from urslib2 import RSS, DSSR, SplitmmCIF, SplitPDB

def build_na_ss_map(
        structure_fname,
        model_number=1,
        mmcif_out_root='rnass_out',
        out_dir_name='pdb_dssr'
    ):
    """
    Split mmCIF/PDB into model-specific mmCIFs using SplitmmCIF.Into_models,
    run DSSR + RSS on each model, write NA secondary-structure labels into
    out_dir_name, and return a map { normalized NA id -> SS label }.
    """

    # -----------------------
    # Prepare folders
    # -----------------------
    rnass_models = "rnass_models"
    rnass_out = "rnass_out"

    os.makedirs(rnass_models, exist_ok=True)
    os.makedirs(rnass_out, exist_ok=True)
    os.makedirs(out_dir_name, exist_ok=True)

    na_map = {}

    # -----------------------
    # Split input into model files
    # -----------------------
    try:
        SplitmmCIF.Into_models(structure_fname, rnass_models)
    except Exception as e:
        print(f"Warning: SplitmmCIF.Into_models failed: {e}")
        return {}

    #try:
    #    SplitPDB.All(rnass_models, rnass_models)
    #except Exception:
    #    pass

    # -----------------------
    # Identify the correct processed file
    # -----------------------
    base = os.path.splitext(os.path.basename(structure_fname))[0]

    processed = [
        f for f in os.listdir(rnass_models)
        if f.startswith(base) and f.lower().endswith((".pdb", ".cif", ".cif1"))
    ]
    if not processed:
        # fallback: original file with new location
        shutil.copy(structure_fname, os.path.join(rnass_models, os.path.basename(structure_fname)))
        processed = [os.path.basename(structure_fname)]

    pdbmodel = os.path.join(rnass_models, processed[0])

    # -----------------------
    # DSSR output
    # -----------------------
    outmodel = os.path.join(rnass_out, base + ".out1")

    if not os.path.exists(outmodel):
        try:
            DSSR.run(pdbmodel, rnass_out)
        except Exception as e:
            print(f"Warning: DSSR run failed for {pdbmodel}: {e}")
            return {}

    # -----------------------
    # RSS Secondary structure
    # -----------------------
    try:
        model = RSS.SecStruct(pdbmodel, outmodel)
    except Exception as e:
        print(f"Warning: RSS.SecStruct failed for {pdbmodel}: {e}")
        return {}

    # -----------------------
    # Parse chains
    # -----------------------
    parser = (
        MMCIFParser(QUIET=True)
        if pdbmodel.lower().endswith((".cif", ".cif1"))
        else PDBParser(QUIET=True)
    )

    sid = os.path.basename(pdbmodel).split(".")[0]
    structure = parser.get_structure(sid, pdbmodel)

    RNA_RES_LOCAL = {'A', 'C', 'G', 'U'}
    DNA_RES_LOCAL = {'DA', 'DC', 'DG', 'DT'}

    rna_chains, dna_chains = set(), set()

    for m in structure:
        for ch in m:
            residues = [res for res in ch if res.id[0] == ' ']
            if not residues:
                continue
            resnames = {res.get_resname().upper() for res in residues}
            if any(r in RNA_RES_LOCAL for r in resnames):
                rna_chains.add(ch.id)
            elif any(r in DNA_RES_LOCAL for r in resnames):
                dna_chains.add(ch.id)

    target_chains = rna_chains | dna_chains

    # -----------------------
    # Normalize DSSR ID
    # -----------------------
    def normalize_na_id(dssr_id, model_number=model_number):
        parts = dssr_id.strip(".").split(".")
        if len(parts) != 3:
            return dssr_id
        chain, resname, resid = parts
        return f"#{model_number}/{chain}:{resname}.{resid}"

    # -----------------------
    # Write NA SS file + fill na_map
    # -----------------------
    txt_out = os.path.join(out_dir_name, base + ".txt")

    with open(txt_out, "w") as fh:
        for chain_id in sorted(target_chains):
            if chain_id not in model.chains:
                continue

            residues = model.chains[chain_id].get("RES", [])
            for n in residues:
                if "DSSR" not in n:
                    continue

                dssr_raw = n["DSSR"]
                ss = model.NuclSS(dssr_raw)
                norm = normalize_na_id(dssr_raw)

                fh.write(f"{norm} {ss}\n")
                na_map[norm] = ss

    return na_map


def find_interaction_clusters(pairwise_distances, structure_name, method=None, resolution=None, chain_summary=None,
                              output_csv="pairwise_table.csv", summary_csv="interfaces_summary_table.csv",
                              pfam_file="pdb_pfam_mapping.txt", rfam_file="Rfam.pdb"):
    """
    Identifies nucleotide–amino acid interaction clusters from pairwise atom distances.
    """

    # ---------------------------------------------------------
    NUCLEOTIDES = {'A', 'C', 'G', 'T', 'U',
                   'DA', 'DC', 'DG', 'DT', 'DU',
                   '1MA', '2MG', '6MZ', '7MG', 'A2M', 'MA6', 'OMG', 'YYG', 'SAM', '4AC', '4SU', '5MC', '5MU', 'LV2', 'OMC', 'OMU', 'SSU', 'UR3', 'PSU', 'B8N', '3TD', 'UY1', 'CDP', 'UDP', 'ADP', 'GDP', 'CTP', 'UTP', 'ATP', 'GTP'}
    AMINO_ACIDS = {
        'ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE',
        'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL' }
    AMINO_ACIDS = {
        'ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE',
        'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL'
    }

    # atom id pattern (captures: model, chain, resname, resid, atom)
    #atom_id_pattern = re.compile(r"#(\d+)/(\w+):([A-Za-z0-9]+).(\d+)\.@?([A-Za-z0-9'\"-]+)?")
    atom_id_pattern = re.compile(r"#(\d+)/(\w+):([A-Za-z0-9]+)\.(\d+)\.@([A-Za-z0-9]+)")
    residue_type = {}
    residue_contacts = set()
    na_pairs = set()
    pairwise_min_distance = {}

    if not pairwise_distances:
        return [], {}, []


    # build maps: protein SS and nucleotide SS from the single structure
    prot_ss_map = get_prot_ss_map(structure_name)        
    na_ss_map = build_na_ss_map(structure_name)          
    pfam_map = get_pfam_for_structure(structure_name, mapping_file=pfam_file)
    rfam_map = fetch_rfam_mapping(rfam_file, structure_name)

    # --- Process pairwise distances ---
    for item in pairwise_distances:
        if not isinstance(item, (list, tuple)) or len(item) != 3:
            continue

        distance, atom1_str, atom2_str = item
        match1 = atom_id_pattern.search(atom1_str)
        match2 = atom_id_pattern.search(atom2_str)
        if not match1 or not match2:
            continue

        model1, chain1, resname1, resid1, atom1 = match1.groups()
        model2, chain2, resname2, resid2, atom2 = match2.groups()
        atom1 = atom1 or "UNK"
        atom2 = atom2 or "UNK"

        # normalize the residue ids used elsewhere in the function (use underscore)
        try:
            res1_id = f"#{model1}/{chain1}:{resname1}.{resid1}"
            res2_id = f"#{model2}/{chain2}:{resname2}.{resid2}"
        except Exception:
            # skip malformed ids
            continue

        type1 = 'N' if resname1 in NUCLEOTIDES else 'AA' if resname1 in AMINO_ACIDS else 'OTHER'
        type2 = 'N' if resname2 in NUCLEOTIDES else 'AA' if resname2 in AMINO_ACIDS else 'OTHER'
        residue_type[res1_id] = type1
        residue_type[res2_id] = type2

        if res1_id != res2_id:
            residue_contacts.add(frozenset([res1_id, res2_id]))

        if (type1 == 'N' and type2 == 'AA') or (type1 == 'AA' and type2 == 'N'):
            aa_res, na_res = (res1_id, res2_id) if type1 == 'AA' else (res2_id, res1_id)
            pair_key = (aa_res, na_res)
            ss_for_aa = prot_ss_map.get(aa_res, "C")

            # ---- Pfam domain assignment (domain-level)
            # aa_res format: '#1/A:SER.45'
            m_pf = re.match(r"#\d+/(\w+):([A-Za-z0-9]+)\.(\d+)", aa_res)
            if m_pf:
                ch = m_pf.group(1).upper()
                aa_resnum = int(m_pf.group(3))
                pfam_hits = []
                if ch in pfam_map:
                    for domain in pfam_map[ch]:
                        # get pfam id key from domain (support both 'pfam_id' and 'pfam' keys)
                        pfid = domain.get("pfam_id") or domain.get("pfam")
                        if pfid and domain.get("start") <= aa_resnum <= domain.get("end"):
                            pfam_hits.append(pfid)
                pfam_id = ",".join(sorted(set(pfam_hits))) if pfam_hits else "NA"
            else:
                pfam_id = "NA"

            # Extract Rfam ID for nucleotide chain (match chain id)
            chain_match_na = re.search(r"#\d+/(\w+):", na_res)
            rfam_id = ",".join(rfam_map.get(chain_match_na.group(1), [])) if chain_match_na else "NA"

            if pair_key not in pairwise_min_distance or distance < pairwise_min_distance[pair_key]["distance"]:
                na_ss_value = na_ss_map.get(na_res, "NA")
                pairwise_min_distance[pair_key] = {
                    "amino_acid": aa_res,
                    "nucleotide": na_res,
                    "closest_atoms": (atom1, atom2),
                    "distance": round(float(distance), 3),
                    "AA_secondary_structure": ss_for_aa,
                    "NA_secondary_structure": na_ss_value,
                    "pfam_id": pfam_id,
                    "rfam_id": rfam_id
                }

            na_pairs.add(frozenset([res1_id, res2_id]))

    # --- Build connectivity graph ---
    G = nx.Graph()
    vertices = {tuple(sorted(p)) for p in na_pairs}
    G.add_nodes_from(vertices)

    aa_to_nucleotides = defaultdict(set)
    nucleotide_to_aas = defaultdict(set)

    for n_res, aa_res in vertices:
        if residue_type.get(n_res) == 'AA':
            n_res, aa_res = aa_res, n_res
        aa_to_nucleotides[aa_res].add(n_res)
        nucleotide_to_aas[n_res].add(aa_res)

    for aa_res, associated_nucleotides in aa_to_nucleotides.items():
        if len(associated_nucleotides) > 1:
            nucleotide_list = list(associated_nucleotides)
            for i in range(len(nucleotide_list)):
                for j in range(i + 1, len(nucleotide_list)):
                    n1, n2 = nucleotide_list[i], nucleotide_list[j]
                    if frozenset([n1, n2]) in residue_contacts:
                        G.add_edge(tuple(sorted((n1, aa_res))), tuple(sorted((n2, aa_res))))

    for n_res, associated_aas in nucleotide_to_aas.items():
        if len(associated_aas) > 1:
            aa_list = list(associated_aas)
            for i in range(len(aa_list)):
                for j in range(i + 1, len(aa_list)):
                    aa1, aa2 = aa_list[i], aa_list[j]
                    if frozenset([aa1, aa2]) in residue_contacts:
                        G.add_edge(tuple(sorted((n_res, aa1))), tuple(sorted((n_res, aa2))))

    # --- Clusters / interfaces ---
    all_components = sorted(list(nx.connected_components(G)), key=len, reverse=True)
    output_clusters_data = []
    res_id_pattern = re.compile(r'(#\d+/\w+):([A-Z0-9]+)\.(\d+)')  # not used for lookup, only formatting
    pairwise_table = []
    summary_table = []

    for i, component in enumerate(all_components):
        unique_raw_residues = set()
        for pair in component:
            unique_raw_residues.update(pair)

        cluster_residues_map = {}
        for res_id in sorted(list(unique_raw_residues)):
            # format display id: '#1/A:ALA_67' -> '#1/A:ALA.67' for readability
            #m = re.match(r'(#\d+/\w+):([A-Za-z0-9]+)_(\d+)', res_id)
            m = re.match(r'(#\d+/\w+):([A-Za-z0-9]+)\.(\d+)', res_id)
            if m:
                model_chain, resname, resid = m.groups()
                formatted_id = f"{model_chain}:{resname}.{resid}"
                cluster_residues_map[res_id] = formatted_id
            else:
                cluster_residues_map[res_id] = res_id

        cluster_data = {
            'id': i + 1,
            'is_connected': len(component) > 1,
            'residues': cluster_residues_map
        }
        output_clusters_data.append(cluster_data)

        interface_pairs = []
        interface_pfams = set()
        interface_rfams = set()

        for pair_key, val in pairwise_min_distance.items():
            if val["amino_acid"] in unique_raw_residues and val["nucleotide"] in unique_raw_residues:
                pairwise_table.append({
                    "interface_name": f"{i + 1}",
                    "structure_name": os.path.basename(structure_name),
                    "amino_acid_residue": val["amino_acid"],
                    "nucleic_acid_residue": val["nucleotide"],
                    "closest_distance": val["distance"],
                    "atoms_involved": f"{val['closest_atoms'][0]}-{val['closest_atoms'][1]}",
                    "AA_secondary_structure": val.get("AA_secondary_structure", "C"),
                    "NA_secondary_structure": val.get("NA_secondary_structure", "NA"),
                    "method": method if method else "Unknown",
                    "resolution": resolution if resolution else "Unknown",
                    "pfam_id": val.get("pfam_id", "NA"),
                    "rfam_id": val.get("rfam_id", "NA")
                })
                interface_pairs.append(val)
                pf = val.get("pfam_id", "")
                if pf and pf != "NA":
                    interface_pfams.update(pf.split(","))
                interface_rfams.update(val.get("rfam_id", "NA").split(","))

        if interface_pairs:
            
            # --- Collect unique secondary structures for the summary table ---
            protein_ss_set = {p.get("AA_secondary_structure", "C") for p in interface_pairs}
            na_ss_set = {p.get("NA_secondary_structure", "NA") for p in interface_pairs}

            # Convert to comma-separated strings, sorted by SS key
            protein_ss_str = ", ".join(sorted(protein_ss_set))
            na_ss_str = ", ".join(sorted(na_ss_set))
            aa_count = sum(1 for r in unique_raw_residues if residue_type.get(r) == 'AA')

            # classify NA type
            RNA_NAMES = {'A', 'U', 'G', 'C'}
            DNA_NAMES = {'DA', 'DT', 'DG', 'DC'}

            rna_count = 0
            dna_count = 0
            for r in unique_raw_residues:
                if residue_type.get(r) == 'N':
                    # r is '#1/T:DG.130' -> extract resname
                    rn = str(r).split(":")[-1].split(".")[0].upper()
                    if rn in RNA_NAMES:
                        rna_count += 1
                    elif rn in DNA_NAMES:
                        dna_count += 1
            na_class = 'RNA' if rna_count >= dna_count else 'DNA'
            total_res = len(unique_raw_residues)

            pair_list = []
            for p in interface_pairs:
                aa_res = p["amino_acid"]
                na_res = p["nucleotide"]
                aa_atom, na_atom = p["closest_atoms"]
                dist = f"{p['distance']:.3f}"
                pair_list.append(f"{aa_res}-{na_res}({aa_atom}-{na_atom}:{dist})")
            pair_str = ", ".join(pair_list)

            summary_table.append({
                "interface_name": f"{i + 1}",
                "structure_name": os.path.basename(structure_name),
                "num_amino_acids": aa_count,
                "num_RNA_NA": rna_count,
                "num_DNA_NA": dna_count,
                "total_residues": total_res,
                "RNA/DNA class": na_class,
                "Protein_SS": protein_ss_str,
                "NA_SS": na_ss_str,
                "method": method if method else "Unknown",
                "resolution": resolution if resolution else "Unknown",
                "pfam_ids": ",".join(sorted(x for x in interface_pfams if x and x != "NA")),
                "rfam_ids": ",".join(sorted(x for x in interface_rfams if x and x != "NA")),
                "chains(residues)": str(chain_summary) if chain_summary else "Unknown",
                "residue_pairs": pair_str
            })

    # --- Write detailed pairwise CSV ---
    if pairwise_table:
        header = [
            "interface_name", "structure_name", "amino_acid_residue", "nucleic_acid_residue",
            "closest_distance", "atoms_involved", "AA_secondary_structure", "NA_secondary_structure",
            "method", "resolution", "pfam_id", "rfam_id"
        ]
        write_mode = "a" if os.path.exists(output_csv) else "w"
        with open(output_csv, write_mode, newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header, delimiter="\t")
            if write_mode == "w":
                writer.writeheader()
            writer.writerows(pairwise_table)

    # --- Write interface summary CSV ---
    if summary_table:
        header_summary = [
            "interface_name", "structure_name", "num_amino_acids", "num_RNA_NA", "num_DNA_NA",
            "total_residues", "RNA/DNA class", "Protein_SS", "NA_SS", "method", "resolution",
            "pfam_ids", "rfam_ids", "chains(residues)", "residue_pairs"
        ]
        write_mode = "a" if os.path.exists(summary_csv) else "w"
        with open(summary_csv, write_mode, newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header_summary, delimiter="\t")
            if write_mode == "w":
                writer.writeheader()
            writer.writerows(summary_table)

    return output_clusters_data, residue_type, pairwise_table

def reformat_cluster_residues(clusters_data, structure_name):

    def normalize_residue_string(raw):
        """Normalize residue string like '#1/A:ALA_67' → '1.A.ALA.67.'.
        Preserve chain ID's original case; uppercase residue name.
        """
        if not raw:
            return ""
        s = str(raw).strip().lstrip("#")
        s = s.replace("/", ".").replace(":", ".").replace("_", ".")
        s = re.sub(r"\.+", ".", s)
        parts = [p for p in s.split(".") if p]
        model = parts[0] if len(parts) > 0 else ""
        chain = parts[1] if len(parts) > 1 else ""
        resname = parts[2] if len(parts) > 2 else ""
        resid = parts[3] if len(parts) > 3 else ""

        # preserve chain EXACTLY as in input (no .upper())
        # but keep residue name uppercase for consistency
        resname = resname.upper()
        normalized = ".".join(p for p in (model, chain, resname, resid) if p)
        if not normalized.endswith("."):
            normalized += "."
        return normalized

    formatted = []
    basename = os.path.splitext(os.path.basename(structure_name))[0]

    for cluster in clusters_data:
        cid = cluster.get("id", "NA")
        residues_map = cluster.get("residues", {}) or {}

        raw_residues = []
        if isinstance(residues_map, dict):
            for k, v in residues_map.items():
                chosen = v if v else k
                raw_residues.append(chosen)
        else:
            raw_residues.extend(residues_map if isinstance(residues_map, list) else [])

        seen, normalized = set(), []
        for r in raw_residues:
            n = normalize_residue_string(r)
            if n and n not in seen:
                normalized.append(n)
                seen.add(n)

        size = len(normalized)
        out_name = f"{size}_{basename}_{cid}.cif"
        formatted.append([normalized, out_name])

    return formatted

def main(filename):
    try:
        print(f"Extracting metadata from {filename}...")
        method, resolution, chain_summary = extract_metadata(filename)
        print(f"  Method: {method}")
        print(f"  Resolution: {resolution}")
        print(f"  Chains: {chain_summary}")
        print("Extracting contacts within 6.0 Å...")
        contacts = contacts_extraction(filename)

        if not contacts:
            print("No contacts found.")
            return

        print("Analyzing interaction clusters...")
        clusters_data, residue_types, pairwise_table = find_interaction_clusters(
            contacts,
            structure_name=filename,
            method=method,
            resolution=resolution, chain_summary=chain_summary,
            output_csv="interfaces_pairwise_table.csv"
        )
        #print(clusters_data)
        # Reformat residues for printing
        reformatted_clusters = reformat_cluster_residues(clusters_data, filename)
        #print("Reformated")
        #print(reformatted_clusters)
        interfaces = []

        if reformatted_clusters:
            input_base = os.path.splitext(os.path.basename(filename))[0]
            output_folder = os.path.join("interfaces", input_base)
            os.makedirs(output_folder, exist_ok=True)

            # reformatted_clusters is a list of [residue_list, out_name] entries
            for idx, item in enumerate(reformatted_clusters, start=1):
                residues_list, out_name = item
                # build the final output path inside the folder
                output_filename = os.path.join(output_folder, out_name)
                interfaces.append([residues_list, output_filename])
        else:
            print("No connected components found.")
        #print(interfaces)
        SaveInterfaces(filename, interfaces)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    from pathlib import Path

    input_dir = Path("test_PDB")
    pdb_files = list(input_dir.glob("*.[pP][dD][bB]"))
    cif_files = list(input_dir.glob("*.[cC][iI][fF]"))
    all_files = pdb_files + cif_files

    total_files = len(all_files)
    print(f"Total files to process: {total_files}")

    for idx, file_path in enumerate(all_files, start=1):
        print(f"\nProcessing file {idx}/{total_files}: {file_path.name} ...")
        main(str(file_path))


