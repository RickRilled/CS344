"""
This module will compute a list of probabilities based on the Bayesian Network from Figure 14.12a

An extension of this exercise, meaning part 2b-d(handCalculations),
can be found in paper at the office of Prof. VanderLinden

Written by Royce Lloyd for CS344 at Calvin College
3/8/2019
"""

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask


T, F = True, False

cloudy = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: .10, F: .50}),
    ('Rain', 'Cloudy', {T: .80, F: .20}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): .99, (T, F): .90, (F, T): .90, (F, F): .00})
])

#P(Sprinker | cloudy)
print(enumeration_ask('Sprinkler', dict(Cloudy=T), cloudy).show_approx())

#P(Cloudy| the sprinkler is running and it’s not raining)
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), cloudy).show_approx())

#P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), cloudy).show_approx())

#P(Cloudy | the grass is not wet)
print(enumeration_ask('Cloudy', dict(WetGrass=F), cloudy).show_approx())
