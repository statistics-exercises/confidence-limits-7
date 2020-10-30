import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand = plt.gca()
        for i in range(6) :
            x, y = fighand.patches[i].get_xy() 
            self.assertTrue( np.fabs(x+0.5*fighand.patches[i].get_width()-1-i)<1e-7, "the x coordinates of the bars in your graph are incorrect" )
            
    def test_normalised(self) :
        ssum = 0.
        fighand=plt.gca()
        for i in range(6) : ssum = ssum + fighand.patches[i].get_height()
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "the histogram has not been normalised correctly" )
        
    def test_plot(self) : 
    fighand=plt.gca()
    for i in range(6) :
        bar = np.sqrt( (1/6)*(1-(1/6)) )*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( fighand.patches[i].get_height() - (1/6) )<bar, "the heights of the bars in your histogram appear to be incorrect" )
    
