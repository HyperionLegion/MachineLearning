#Bayes
#prob of output=0 given input x1=x1 and x2=x2
#prob o output=1 given inputx1=x1 and x2=x2
#take the prob that is bigger, instead of just 1 number with a threshold, 2 numbers

#Prob of A given B = Prob of A and B / Prob of B (naive bayes rule)
#prob of A and B = Prob of B * Prob of (A given B) = Prob of A * Prob of ( B given A)

#Prob of A given B = Prob of A * Prob of B given A / (Prob of A * Prob of B given A + Prob of not A * Prob of B given not A)
#denom = prob of B and A + prob of B and not A (total probability)
