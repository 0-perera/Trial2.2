# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:25:25 2023

@author: Sofia
"""

import matplotlib.pyplot as plt       # Import plotting functions
import numpy as np                    # Import numerical functions
from scipy.optimize import curve_fit  # Import Curve fitting function from scipy

file = open('lockinamp_2.csv', 'r')
# Use numpy functions to read .csv (comma separated values)
dataset=np.loadtxt(file, delimiter=',').T
#print(dataset)


# Store information in easier to use variables/objects
X=dataset[0]    # Store X-values
Y=dataset[2]    # Store Y-values
#YERR=dataset[2] # Store Y errors 


# Define our functions 
# (this needs changes for fitting different functions)
def fitFunc(x,t):
  return 1/(np.sqrt(1+2*np.pi*x*t))
  return np.arctan2(1,np.pi*x*t)



init=np.array([0.01])          # Initial guess of fitting parameter (starting values)
pnames=[ "Decay"]   # Keep human readable names of parameter


# Here is were the magic happens
pars,covar = curve_fit(fitFunc,X,Y,init) # Run the fitting #for fitting without error weighting remove the "sigma=YERR", 
#print(pars)

stdev=np.sqrt(np.diag(covar))   # Store reported standard errors
#print(stdev)

f_fit=fitFunc(X,*pars)          # Save results curve Y-values
f_guess=fitFunc(X,*init)        # Save initial guess Y-values (always look at this when thing go wrong)


# Create a graph with all results
plt.figure()            # Initialise new figure
plt.xlabel("weight (g)")    # Assign x-label
plt.ylabel("displacement (mm)")    # Assign y-label 
plt.errorbar(X,Y,fmt='o',capsize=4)      # (Scatter plot with errors)
plt.plot(X,f_fit,'--')            # Fitted curve
#plt.plot(X,f_guess,'-.g')            # Initial curve  

plt.savefig("Hookes-law.svg")            # Save plot (for Office365, Openoffice)
plt.show()
print(pars)
print(pnames)
print(pnames[0]+':\t'+"{:.3g}".format(pars[0])+' ± '+"{:.1g}".format(stdev[0]))
