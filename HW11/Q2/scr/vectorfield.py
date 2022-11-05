import numpy as np

def vectorfield(w, t, c):
    """
    Defines the differential equations for both compartmental pandemic models.

    Arguments:
        w :  vector of the state variables:
                  w = [s,e,i,r,p]
        t :  time
        p :  vector of the parameters:
                  p = [alpha_e,alpha_i,gamma,kappa,ro,beta,mo]
    Output:
        model:   differential equations
    """
    s,e,i,r,p = w
    alpha_e,alpha_i,gamma,kappa,ro,beta,mo = c

    # Create f = (s',p',i',r',p'):
    model = [-(alpha_e*s*e)-(alpha_i*s*i)+(gamma*r),
         (alpha_e*s*e)+(alpha_i*s*i)-(kappa*e)-(ro*e),
         (kappa*e)-(beta*i)-(mo*i),
         (beta*i)+(ro*e)-(gamma*r),
         (mo*i)]

    return model
