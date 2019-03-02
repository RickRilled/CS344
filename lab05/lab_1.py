'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
Edited by Royce Lloyd
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.
"""
P(Alarm | burglary ∧ ¬earthquake)
If there was a burglary, but not an earthquake, what are the odds the alarm goes off?
The alarm is dependant on a burglary. It makes sense that there would be a high probability 
of it going off if there was a burglary. 
"""
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())


"""
P(John | burglary ∧ ¬earthquake)
If there was a burglary, but not an earthquake, what are the odds john calls?
John calling is dependant on the alarm. Since that can go off for either B or E, there is a chance
that John will call.
"""
print(enumeration_ask('John', dict(Burglary=T, Earthquake=F), burglary).show_approx())

"""
P(Burglary | alarm)
If there was an alarm, what are the odds there was a burglary?
This is about what I expected. There is a chance the alarm went off by some other means.
"""
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

"""
P(Burglary | john ∧ mary)
If John and Mary call, what are the odds there was a burglary?
"""
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())




