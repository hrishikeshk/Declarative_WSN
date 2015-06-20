# This centralized (in other words, simulated) shortest path routing

from pyDatalog import pyDatalog
pyDatalog.create_terms("Src, Dest, Cost, Cost1, Cost2, Next, Path, Path2, path, link, edge, a, b, c, d, e")

#links with cost
+link(e, a, 1)
+link(a, b, 5)
+link(a, c, 1)
+link(b, d, 1)
+link(c, b, 1)

#recursive rules to define paths with cost
path(Src, Dest, Path, Cost) <= link(Src, Dest, Cost) & (Path == [Src] + [Dest])
path(Src, Dest, Path, Cost) <= link(Src, Next, Cost1) & path(Next, Dest, Path2, Cost2) & Path == [Src] + Path2 & Cost == Cost1 + Cost2
spCost(Src, Dest, Cost) <= path(Src, Dest, Path, Cost1) & (Cost == min_(Cost1)) 
shortestPath(Src, Dest, Path, Cost) <= spCost(Src, Dest, Cost) & path(Src, Dest, Path, Cost)
print (shortestPath(Src, Dest, Path, Cost)) & (Src == a) & (Dest == d)
