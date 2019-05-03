A)

1.
in(X, Y) :- directlyIn(X, Y).

in(X, Y) :- directlyIn(X, Z), in(Z, Y).

2.
listtran(g|Tg,e|Te) :- listtran(Tg, Te).

B)

Yes, it uses a KB to check against the query given, ie q :- p