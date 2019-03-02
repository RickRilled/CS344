'''
This module implements the Bayesian network displaying the relationship
between getting a raise, the weather, and happiness.
It's taken from the AIMA Python code.

Written by Royce Lloyd for CS344, 3/1/2019
'''
from probability import BayesNet, enumeration_ask


T, F = True, False

happy = BayesNet([
    ('Sunny', '', .7),
    ('Raise', '', .01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])


print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())

"""
These are independent of each other, so it makes sense that they do not have
much affect on each other.
"""

print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happy).show_approx())

"""
Happy is dependant on both raise and sunny. Because we know Raise is less likely to happen, it is
more probable that you hare happy because it is sunny. 
P(Raise | H ^ S) = a * P(H ^ R ^ S)
= a * <P(H | R ^ S) * P(S) * P(R),
        P(H | -R ^ S) * P(S) * P(-R)>
= a * <1 * .7 * .01,
        .7 * .7 * .99>
= a * <.007, .4851>
= <.0142, .9858>
"""

# b.

print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())


"""
This result is very similar to our previous question. Given that we are happy,
we must have either gotten a raise, or it was sunny. Because the odds of getting
a raise are so much smaller than it being sunny, there is a better chance of sunny being 
the cause. See how P(Raise) = 0.01
"""

print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

"""
Similar to the cancer problem, the values did not jump as high as i expect when we
pointed to Raise being the cause of our happiness. Because it is so unlikely to begin with,
small jumps in the "true" value field are more significant. 
"""

