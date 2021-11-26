



#Trabajo Práctico de Registros y Corte de Control



from pyrecord import Record
import random, numpy as np

regc=Record.create_type("regc",
"acnum",
"sur",
"name",
"id",
"actype",
"sal",
"active")