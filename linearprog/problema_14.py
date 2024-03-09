# problema_14.py

import pyomo.environ as pyomo

model = pyomo.ConcreteModel()

# declare decision variables
model.x1 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x2 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x3 = pyomo.Var(domain=pyomo.NonNegativeReals)

# declare constraints
model.c = pyomo.ConstraintList()
model.c.add( model.x1 == model.x2 )
model.c.add( model.x2 == model.x3 )
model.c.add( model.x1 <= 16000 )
model.c.add( model.x1 <= 20000 )
model.c.add( model.x1 <= 20000 )
model.c.add( model.x1 <= 12000 )
model.c.add( model.x1 <= 24000 )

# declare objective
model.objective = pyomo.Objective(rule = lambda model: 
                                  model.x1 , 
                                  sense = pyomo.maximize)

# solve
solver = pyomo.SolverFactory('glpk')
result = solver.solve(model)

print(result)
print('x1:', model.x1())