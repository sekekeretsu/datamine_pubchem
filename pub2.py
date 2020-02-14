import pubchempy as pcp


results= pcp.get_compounds('UK-396082', 'name')
for compound in results:
	print(compound.isomeric_smiles)
	cmpid=compound 
	print(cmpid)
	print(compound.iupac_name)
