from scipy.integrate import odeint
from scr import vectorfield

def ODE_solver(alpha_e, alpha_i, gamma, kappa, ro, beta, mo, s, e, i, r, p, days):
    """
    Use ODEINT to solve the differential equations defined by the vectorfield.

    Arguments:
        alpha_e, alpha_i, gamma, kappa, ro, beta, mo : Parameter values
        s, e, i, r, p : Initial conditions
        days : number of days for simulation
    Output:
        t, s, e, i, r, p: Simulation time and the resulted sunction
    """

    # ODE solver parameters
    abserr = 1.0e-8
    relerr = 1.0e-6
    stoptime = days
    numpoints = days*20

    # Create the time samples for the output of the ODE solver.
    t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

    # Pack up the parameters and initial conditions
    c = [alpha_e,alpha_i,gamma,kappa,ro,beta,mo]
    w0 = [s,e,i,r,p]

    # Call the ODE solver.
    wsol = odeint(vectorfield, w0, t,args=(c,),
                  atol=abserr, rtol=relerr)
    # Gathering the results
    s = []
    e = []
    i = []
    r = []
    p = []
    for t1, w1 in zip(t, wsol):
            t1 = t
            s.append(w1[0])
            e.append(w1[1])
            i.append(w1[2])
            r.append(w1[3])
            p.append(w1[4])
            
    return t, s, e, i, r, p
