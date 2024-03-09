# nonlinearproblem.py

# Las dimensiones óptimas para una lata de 710 ml (tallboy). 
# Se considera que la lata es un cilindro con radio r y altura h. Se debe encontrar el radio y la altura que
# minimice el área superficial del cilindro a la vez que se mantiene el volumen establecido.
# El área superficial del cilindro es aproximadamente la cantidad de aluminio necesaria para la
# fabricación de la lata, así que se busca aproximar la cantidad mínima de aluminio necesaria para el caso.

# Área superficial de un cilindro: 2πr(r+h)
# Volumen de un cilindro: πr**2h

import pyomo.environ as pyomo
from math import pi

model = pyomo.ConcreteModel()

# declare decision variables
model.r = pyomo.Var(bounds=(0,None))
model.h = pyomo.Var(bounds=(0,None))

# declare constraints
model.c = pyomo.ConstraintList()
model.c.add( expr=pi*model.h*model.r**2 == 710 )

# declare objective
model.o = pyomo.Objective(expr=2*pi*model.r*(model.r + model.h),sense=pyomo.minimize)

# solve
solver = pyomo.SolverFactory('baron')
result = solver.solve(model)

print(result)
print('Objetivo:', model.o(), '\nradio:', model.r(), '\naltura:', model.h())