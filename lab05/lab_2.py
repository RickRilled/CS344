'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

Written by Royce Lloyd for CS344, 3/1/2019
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])


"""
P(Cancer | positive results on both tests)
If you got a positive result on both tests, what are the odds you have cancer?
"""
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

"""
P(Cancer | 1, 2) = a * P(Cancer, 1, 2)
= a * < P(cancer) * P(1 | cancer) * P(2 | cancer), 
        P(-cancer) * P(1 | -cancer) * P(2 | -cancer)>
= a * <.01 * .9 * .9, .99 * .2 * .2>
= a * <.0081, .0396>
= <.170, .830>
"""


"""
P(Cancer | a positive result on test 1, but a negative result on test 2)
If you get a positive result on test 1, but not on test 2, what are the odds you have cancer?
"""
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
"""
P(Cancer | 1, 2-) = a * P(cancer, 1, 2)
= a * < P(cancer) * P(1 | cancer) * P(2- | cancer),
        P(-cancer) * P(+ | cancer) * P(2- | cancer)>
= a * <.01 * .9 * .1,
        .99 * .2 * .8>
= a * <.0009, .1584>
= <.0057, .994>
"""


"""
The results are not as conclusive as I would expect. However, 
adding another test with more possibility of getting a false positive
might contribute to the low truth possibility.

Failing one test drastically affects the possibility of having cancer. One failing almost 
guarantees the first one was a false positive. 
"""







