import matplotlib.pyplot as plt
import numpy as np

def dice_roll() : 
  # Your code to generate the outcome when we roll a fair six sided dice goes here.
  
  
counts = np.zeros(6)
for i in range(200) : 
  # Your code to generate multiple random variables using the function
  # called dice_roll above and to count how often each outcome comes
  # up goes here.
  
  

for i in range(6) : 
  # Your function to convert the count of the number of times each 
  # value for the random variable comes up to the fraction of times
  # each outcome comes up goes here.
  
  
  
# These command will plot your histogram
plt.bar( [1,2,3,4,5,6], counts, width=0.1 )
plt.xlabel("Random variable value")
plt.ylabel("Fraction of occurances")
plt.savefig("myhistogram.png")
