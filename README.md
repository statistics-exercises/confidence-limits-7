# Histograms Revision 

Let's quickly revise how to compute a histogram before getting on to how to generate histograms with error bars calculated by resampling.   __To complete this task you need to write a code to estimate the histogram for an experiment in which a fair six-sided dice is rolled.__  Each bar in this histogram will thus be an estimate of getting that value when you roll the dice.

To complete the exercise you will need to:

1. Write a function called `dice_roll` that returns the outcome from the roll of a fair six-sided dice.  This function should return a discrete random variable that is greater than or equal to 1 and less than or equal to 6.
2. Call the function `dice_roll` in order to generate 200 samples from this distribution.  Use the list array `counts` to count how often each of the various possible values this random variable can take comes up in these samples.  Remember that you do not need to use if statements to do this counting as you can use the value of the random variable to refer to the appropriate element of the list.  
3. Convert the `counts` of how often each variable comes up to a fraction that measures the fraction of samples for which the random variable was equal to each of the values sampled.

If you have completed the code correctly the bars in the chart that will appear should all have similar heights.
