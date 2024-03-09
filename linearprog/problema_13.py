# problema_13.py

import pyomo.environ as pyomo

model = pyomo.ConcreteModel()

# declare decision variables
model.x1 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x2 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x3 = pyomo.Var(domain=pyomo.NonNegativeReals)

# declare constraints
model.c = pyomo.ConstraintList()
model.c.add( model.x1*(5) + model.x2*(8) + model.x3*(13) <= 4000 )
model.c.add( model.x1*(12) + model.x2*(18) + model.x3*(14) <= 6000 )
model.c.add( model.x1*(5) + model.x2*(8) + model.x3*(13) <= 600 )

# declare objective
model.objective = pyomo.Objective(rule = lambda model: 
                                  model.x1*(6) + model.x2*(12) + model.x3*(10) , 
                                  sense = pyomo.maximize)

# solve
solver = pyomo.SolverFactory('glpk')
result = solver.solve(model)

print(result)
print('x1:', model.x1(), '\nx2:', model.x2(), '\nx3:', model.x3())
