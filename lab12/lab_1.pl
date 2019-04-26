12.1

A)
i)
1)killer(butch) "Butch is a killer"
2)marries(mia,marsellus) "mia and marsellus are married"
3)dead(zed) "zed is dead"
4)kills(marsellus,X):- giveMiaAFootmassage(X) "If someone gives mia a foot massage, marsellus kills them"
5)loves(mia,X):- goodDancer(X) "If you are a good dancer, mia loves you"
6)eats(jules):- isTasty(X) "If the thing is tasty, jules eats it"

ii)
1. yes "given"
2. no   "no witch"
3. no   "not explicitly stated"
4. no   "no witch"
5. yes  "can be deduced with the rule hasBroom and wizard(X)"
6. ron  "only wizard expressed"
7. no   "no witch"

B)

Yes, it can be implemented as follows

p
q:- p

C)
Horn clauses can be helpful in theorem because resolving two Horn clauses results in a Horn clause. Propositional logic
does not contain such a resolution, but might be better suited for readability.

D)
Prolog seems to only support ASK, since we ask it a query and it provides an answer

