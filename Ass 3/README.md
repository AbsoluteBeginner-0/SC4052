The present code simulates a TextRank algorithm on a textual input with a command-line interface.
To run it, run main.py.

The command-line interface accepts the following commands:

sentence "<sentence>"
Adds a vertex with label "sentence" to the graph space.

text "<file.txt>"
Reads <file.txt> line-by-line and adds a vertex for each line.

text readall "<file.txt>"
Reads <file.txt> and split it into sentences, adds a vertex for each sentence. 

print
Prints the current graph information including vertices, edges, and adjacency matrix.

sim start
Creates a TextRank instance for the current graph. Only one TextRank instance may exist at a time.

sim stop
Deletes the current TextRank instance.

sim setp p
Sets the dampening factor to p, with 0 <= p <= 1

sim togglep [on/off]
Toggles between the simplified and modified versions of TextRank with "on" corresponding to the latter.

sim verbose [on/off]
Toggles verbose outputs.

sim step n
Run n iterations of the TextRank calculation.

sim gettop n
Returns the top n vertex labels of the TextRank instance.

file <path>
Loads all commands in file at <path>

exit
Exits CLI