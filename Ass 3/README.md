The present code simulates a PageRank algorithm on a directed graph with a command-line interface.
To run it, run main.py.

The command-line interface accepts the following commands:

vertex <vertex-name>
Adds a vertex with label "vertex-name" to the graph space.

edge <a> <b>
Adds an edge from vertex "a" to vertex "b" in the graph space. Both "a" and "b" must be existing vertices.

print
Prints the current graph information including vertices, edges, and adjacency matrix.

sim start
Creates a PageRank instance for the current graph. Only one PageRank instance may exist at a time.

sim stop
Deletes the current PageRank instance.

sim setp p
Sets the dampening factor to p, with 0 <= p <= 1

sim togglep [on/off]
Toggles between the simplified and modified versions of PageRank with "on" corresponding to the latter.

sim step n
Run n iterations of the PageRank calculation.

file <path>
Loads all commands in file at <path>

exit
Exits CLI