# This centralized (in other words, simulated) shortest path routing

from pyDatalog import pyDatalog
pyDatalog.create_terms("Y, Minimum, Src, Dest, Cost, Cost1, Cost2, Next, Path, Path2, path, link, a, b, c, d, e, spCost, shortestPath, X")

#links with cost
+link(e, a, 1)
+link(a, b, 5)
+link(a, c, 1)
+link(b, d, 1)
+link(c, b, 1)

def Minimum(X):
    return min_(X, order_by=Cost1) 


#recursive rules to define paths with cost
path(Src, Dest, Path, Cost) <= link(Src, Dest, Cost) & (Path == [Src] + [Dest])
path(Src, Dest, Path, Cost) <= link(Src, Next, Cost1) & path(Next, Dest, Path2, Cost2) & (Src != Dest) & (Path == [Src] + Path2) & (Cost == Cost1 + Cost2)

#spCost(Src, Dest, Cost) <= (Y == path(Src, Dest, Path, Cost1)) & ( Cost == Minimum(Cost1) )
#spCost(Src, Dest, Cost) <= ( Cost == Minimum(Y) ) & (Y == path(Src, Dest, Path, Cost1))
#spCost(Src, Dest, Cost) <= ( Cost == min(X, order_by=Cost1) ) & (X == path(Src, Dest, Path, Cost1))
#spCost(Src, Dest, Cost) <= ( Cost == min(Cost1) ) & (X == path(Src, Dest, Path, Cost1))

#shortestPath(Src, Dest, Path, Cost) <= (Cost == spCost(Y)) & ( Y == path(Src, Dest, Path, Cost) )

(shortestPath[Src, Dest]==min_(Path, order_by=Cost)) <= (path( Src , Dest, Path, Cost))

#print (shortestPath(Src, Dest, Path, Cost)) & (Src == a) & (Dest == d)
print (shortestPath [Src, Dest] == Path ) & (Src == a) & (Dest == d)

