#Bayes
#prob of output=0 given input x1=x1 and x2=x2
#prob o output=1 given inputx1=x1 and x2=x2
#take the prob that is bigger, instead of just 1 number with a threshold, 2 numbers

#Prob of A given B = Prob of A and B / Prob of B (naive bayes rule)
#prob of A and B = Prob of B * Prob of (A given B) = Prob of A * Prob of ( B given A)

#Prob of A given B = Prob of A * Prob of B given A / (Prob of A * Prob of B given A + Prob of not A * Prob of B given not A)
#denom = prob of B and A + prob of B and not A (total probability)
#not A = output = 1
#A output = 0

#Prob of B given A, prob of B given not A, prob of x1, x2 given output = 0, prob of x1, x2 given output = 1
#function = 1/(standard dev * sqrt(2pi)) * exp(-(x-mean)^2/(2*standard dev^2))
#P of x1, x2 = P of x1 * P of x2, means independent events

#prob of output =0 given x1, x2) = Prob(output=0) * Prob(x1, x2 | output =0) / (Prob output=0)*P(x1, x2 | output = 0) + P(output=1)*P(x1, x2 | output = 1)
#Prob of output=1 given x1, x2 = same thing but outpu=1 in numerator ^^^
#Prob of output =0 = pi_0 = n_0/n
#prob of output = 1 = pi_1 = n_1/n
#n = n0 +n1 = 400?
#P(x1, x2 | output = 1) = P(x1 | output=1) * P(x2 | output=1) ASSUMPTION, independent from naive
#P of x1 | output = 1 = f_1(x_1)
#P of x_2 | output = 1 = f_2(x_2)
#p0 * f_0(x_1) * f_0(x_2) / pi_0*f_0(x_1)*f_0(x_2) + pi_1*f_1(x_1)*f_2(x_2)