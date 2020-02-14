import pubchempy as pcp


results= pcp.get_compounds('(+)-2-[4-[(-1-acetimidoyl-4-piperidinyl)oxy]-3-(7-amidino-2-naphthyl)propionic acid','name')
for compound in results:
	print(compound.isomeric_smiles)
	cmpid=compound 
	print(cmpid)
	print(compound.iupac_name)
