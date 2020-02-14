import urllib
import pubchempy as pcp
#mol="clacinomycin A"
#c=pcp.Compound.from_cid(1423)
c=pcp.get_compounds('asprin','name')
print(c.molecular_formula)
print(c.molecular_weight)
print(c.isomeric_smiles)

