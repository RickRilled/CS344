"""
AHHHHHHHHHH
"""


from csp import backtracking_search, parse_neighbors, CSP, min_conflicts, AC3

def scheduler():

    classes = "CS232 CS108 CS212 CS112 CS336 CS344".split()
    profs = "Adams VanderLinden Plantinga Schuurman Norman Nelsen".split()
    times = "mwf0800 mwf0900 mwf1000 th1230".split()
    rooms = "nh253 sb382".split()

    variables = classes

    all_domains = []
    for room in rooms:
        for time in times:
            for prof in profs:
                all_domains.append(room + " " + time + " " + prof)

    domains = {}
    for var in variables:
        domains[var] = all_domains

    neighbors = parse_neighbors("""CS344: nh253 mwf0800""", variables)
    for type in [variables]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def scheduler_constraint(A, a, B, b, recurse=0):

        conflict = (a == b)

        if(a.split()[0] == b.split()[0]) and (a.split()[2] == b.split()[2]):
            return conflict

        if(a.split()[1] == b.split()[1]) and (a.split()[2] == b.split()[2]):
            return conflict

        if recurse == 0:
            return scheduler_constraint(B, b, A, a, 1)

        return True

    return CSP(variables, domains, neighbors, scheduler_constraint)


print(backtracking_search(scheduler()))
#print(AC3(scheduler()))
print(min_conflicts(scheduler()))




