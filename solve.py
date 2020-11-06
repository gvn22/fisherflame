import numpy as np
import dedalus.public as de

de.logging_setup.rootlogger.setLevel('ERROR')

x_basis = de.Chebyshev('x',256,interval=(0,1),dealias=3/2)
domain = de.Domain([x_basis],float)
prob = de.IVP(domain, variables=['c','cx'])

prob.parameters['D'] = 0.00001
prob.parameters['R'] = 0.001

prob.add_equation("cx - dx(c) = 0")
prob.add_equation("dt(c) - D*dx(cx) = R*c*(1-c)")
prob.add_bc("left(cx) = 0")
prob.add_bc("right(cx) = 0")

ts = de.timesteppers.RK222
solver = prob.build_solver(ts)
solver.stop_sim_time = 10000
solver.stop_iteration = 1e4
solver.stop_wall_time = np.inf

u = solver.state['c']
x = domain.grid(0)
u['g'] = 0.5*(np.tanh(x/0.05-10)+1)

analysis = solver.evaluator.add_file_handler('analysis_tasks',sim_dt=0.1,max_writes=100)
analysis.add_task('integ(R*c*(1-c))',name='s')
analysis.add_task('R*c*(1-c)',name='r')
analysis.add_task('c',name='c')

dt = 0.01

print('Solving KPP equations...')
while solver.ok:
    solver.step(dt)
    # if solver.iteration % 100 == 0:
        # print('Completed iteration {}'.format(solver.iteration))
