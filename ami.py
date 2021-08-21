import numpy as np
import matplotlib.pyplot as plt

L = 32 # number of digital samples per data bit
Fs = 8*L # Sampling frequency
voltageLevel = 5 # peak voltage level in Volts
data = (np.random.rand(10000)>0.5).astype(int) # random 1s and 0s for data
clk = np.arange(0,2*len(data)) % 2 # clock samples

#teste
ami = 1*data; previousOne = 0 

for ii in range(0,len(data)):
  if (ami[ii]==1) and (previousOne==0):
    ami[ii] = voltageLevel
    previousOne=1;
  if (ami[ii]==1) and (previousOne==1):
    ami[ii]= -voltageLevel
    previousOne = 0;