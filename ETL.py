from Extract_acidentes import extract_acidentes
from Extract_datatran import extract_datatran

from Transform_acidentes import transform_acidentes
from Transform_datatran import transform_datatran

# from Transform_acidentes import load_acidentes
from Load_datatran import load_datatran



print("Extraindo dados...")
extract_datatran()
extract_acidentes()


print("Transformando dados...")
transform_acidentes()
transform_datatran()


print("Carregando dados...")
# 
load_datatran()
