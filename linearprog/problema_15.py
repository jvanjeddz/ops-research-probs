# problema_15.py

import pyomo.environ as pyomo

model = pyomo.ConcreteModel()

# declare decision variables
model.x_x1 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x_x2 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x_x3 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x_x4 = pyomo.Var(domain=pyomo.NonNegativeReals)

model.x_z1 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x_z2 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x_z3 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x_z4 = pyomo.Var(domain=pyomo.NonNegativeReals)

model.s_x1 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.s_x2 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.s_x3 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.s_x4 = pyomo.Var(domain=pyomo.NonNegativeReals)

model.s_z1 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.s_z2 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.s_z3 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.s_z4 = pyomo.Var(domain=pyomo.NonNegativeReals)

# declare constraints
model.c = pyomo.ConstraintList()
model.c.add( model.s_x1 == 100 + model.x_x1 - 300)
model.c.add( model.s_x2 == model.s_x1 + model.x_x2 - 600)
model.c.add( model.s_x3 == model.s_x2 + model.x_x3 - 600)
model.c.add( model.s_x4 == model.s_x3 + model.x_x4 - 500)

model.c.add( model.s_z1 == 200 + model.x_z1 - 700)
model.c.add( model.s_z2 == model.s_z1 + model.x_z2 - 500)
model.c.add( model.s_z3 == model.s_z2 + model.x_z3 - 800)
model.c.add( model.s_z4 == model.s_z3 + model.x_z4 - 500)

model.c.add( model.s_z4 >= 300)

model.c.add( model.x_x1 <= 400)
model.c.add( model.x_x2 <= 400)
model.c.add( model.x_x3 <= 400)
model.c.add( model.x_x4 <= 400)

model.c.add( model.x_z1 <= 700)
model.c.add( model.x_z2 <= 700)
model.c.add( model.x_z3 <= 700)
model.c.add( model.x_z4 <= 700)

model.c.add( model.s_x1 + model.s_z1 <= 300)
model.c.add( model.s_x2 + model.s_z2 <= 300)
model.c.add( model.s_x3 + model.s_z3 <= 300)
model.c.add( model.s_x4 + model.s_z4 <= 300)

# declare objective
model.objective = pyomo.Objective(rule = lambda model: 
                                  ((model.s_x1 + model.s_x2 + model.s_x3 + model.s_x4)*(2)) 
                                  + (model.s_z1 + model.s_z2 + model.s_z3 + model.s_z4) 
                                  , sense = pyomo.minimize)


# solve
solver = pyomo.SolverFactory('glpk')
result = solver.solve(model)

print(result)
