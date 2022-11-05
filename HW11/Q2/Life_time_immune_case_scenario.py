# Example 4 (Life-time immune case)
import matplotlib.pyplot as plt
from scr.ODE_solver import ODE_solver

# Parameter values
alpha_e = 0.65
alpha_i = 0.005
gamma = 0
kappa = 0.05
ro = 0.08
beta = 0.1
mo = 0.02

# Initial conditions
s = 1
e = 0.001
i = 0.002
r = 0.001
p = 0.002

days = 300

t, s, e, i, r, p = ODE_solver(alpha_e, alpha_i, gamma, kappa, ro, beta, mo, s, e, i, r, p, days)

plt.figure(figsize=(6, 4))
plt.xlabel('Days', fontsize = 12)
plt.ylabel('Population Ratio', fontsize = 12)
plt.xlim([0,days])
plt.ylim([0,1])
plt.grid(linewidth=0.25)

plt.plot(t, s, 'b')
plt.plot(t, e, 'aqua')
plt.plot(t, i, 'r')
plt.plot(t, r, 'lime')
plt.plot(t, p, 'k')

plt.legend(('S(t)','E(t)','I(t)','R(t)','P(t)'))
