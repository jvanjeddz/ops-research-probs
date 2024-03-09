# problema_12.py

import pyomo.environ as pyomo

model = pyomo.ConcreteModel()

# declare decision variables
model.x11 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x21 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x31 = pyomo.Var(domain=pyomo.NonNegativeReals)

model.x12 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x22 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x32 = pyomo.Var(domain=pyomo.NonNegativeReals)

model.x13 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x23 = pyomo.Var(domain=pyomo.NonNegativeReals)
model.x33 = pyomo.Var(domain=pyomo.NonNegativeReals)

# declare constraints
model.c = pyomo.ConstraintList()
model.c.add( model.x11 + model.x12 + model.x13 <= 2000 )
model.c.add( model.x21 + model.x22 + model.x23 <= 4000 )
model.c.add( model.x31 + model.x32 + model.x33 <= 1000 )

model.c.add( model.x11 >= (0.8)*(model.x11 + model.x21 + model.x31) )
model.c.add( model.x31 <= (0.2)*(model.x11 + model.x21 + model.x31) )
model.c.add( model.x12 >= (0.2)*(model.x12 + model.x22 + model.x32) )
model.c.add( model.x32 <= (0.8)*(model.x12 + model.x22 + model.x32) )
model.c.add( model.x33 <= (0.7)*(model.x13 + model.x23 + model.x33) )



# declare objective
model.objective = pyomo.Objective(rule = lambda model: 
                                  (4)*(model.x11 + model.x21 + model.x31) 
                                  + (3)*(model.x12 + model.x22 + model.x32) 
                                  + (2)*(model.x13 + model.x23 + model.x33)
                                  - (3)*(model.x11 + model.x12 + model.x13) 
                                  - (2)*(model.x21 + model.x22 + model.x23) 
                                  - (1)*(model.x31 + model.x32 + model.x33)
                                  , sense = pyomo.maximize)

# solve
solver = pyomo.SolverFactory('glpk')
result = solver.solve(model)

print(result)

print('x11:', model.x11(), '\nx12:', model.x12(), '\nx13:', model.x13())
print('x21:', model.x21(), '\nx22:', model.x22(), '\nx23:', model.x23())
print('x31:', model.x31(), '\nx32:', model.x32(), '\nx33:', model.x33())