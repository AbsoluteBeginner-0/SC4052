import graph
import pagerank

class CLI:

    def Run():
        my_graph = graph.Graph()
        my_pagerank = None
        while(True):
            choice = input()
            command = choice.split(' ')
            
            if command[0] == 'vertex':
                if 2 != len(command):
                    print(f"Invalid number of arguments! 'vertex' command expects 2 arguments, {len(command)} were given.")
                    continue

                label = command[1]
                try:
                    my_graph.AddNode(label)
                except Exception as e:
                    print(repr(e))
                    continue
                
                print(f"Vertex '{label}' added.")
            elif command[0] == 'edge':
                if 3 != len(command):
                    print(f"Invalid number of arguments! 'edge' command expects 3 arguments, {len(command)} were given.")
                    continue

                label_from = command[1]
                label_to = command[2]
                # weight = float(command[3])

                try:
                    my_graph.AddEdge(label_from, label_to)
                except Exception as e:
                    print(repr(e))
                    continue
                else:
                    print(f"Edge from '{label_from}' to '{label_to}' added.")

            elif command[0] == 'print':
                if 1 != len(command):
                    print(f"Invalid number of arguments! 'print' command expects 1 arguments, {len(command)} were given.")
                    continue
                my_graph.Print()
            elif command[0] == 'exit':
                print("Exiting...")
                break

            elif command[0] == 'sim':
                if 2 == len(command):
                    if 'start' == command[1]:
                        my_pagerank = pagerank.PageRank(my_graph)
                    elif 'stop' == command[1]:
                        del my_pagerank
                        my_pagerank = None
                    else:
                        print("Invalid command.")
                        continue
                elif 3 == len(command):
                    if 'step' == command[1]:
                        if not my_pagerank:
                            print("Need to start simulation first!")
                            continue
                        my_pagerank.StepN(command[2])
                    elif 'setp' == command[1]:
                        my_pagerank.SetRandomJump(command[2])
                    elif 'togglep' == command[1]:
                        if 'on' == command[2]:
                            my_pagerank.ToggleRandomJump(True)
                        elif 'off' == command[2]:
                            my_pagerank.ToggleRandomJump(False)
                        else:
                            print("Invalid command.")
                            continue
                else:
                    print("Invalid command.")
                    continue

            else:
                print("Invalid command.")
