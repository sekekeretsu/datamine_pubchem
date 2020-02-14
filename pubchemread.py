import urllib
import pubchempy as pcp
mol="clacinomycin A"
c=pcp.Compound.from_cid(1423)
cs=pcp.get_compounds('6-diazo-5-oxo-L-norleucylglycine','name')
print(c.molecular_formula)
print(c.molecular_weight)
print(c.isomeric_smiles)
