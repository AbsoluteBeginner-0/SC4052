import graph
import pagerank
import random

class CLI:
    __my_graph = None
    __my_pagerank = None

    def ProcessCMD(self, command):
        if command[0] == 'vertex':
            if 2 != len(command):
                print(f"Invalid number of arguments! 'vertex' command expects 2 arguments, {len(command)} were given.")
                return 0

            label = command[1]
            try:
                self.__my_graph.AddNode(label)
            except Exception as e:
                print(repr(e))
                return 0
            
            print(f"Vertex '{label}' added.")
        elif command[0] == 'edge':
            if 3 != len(command):
                print(f"Invalid number of arguments! 'edge' command expects 3 arguments, {len(command)} were given.")
                return 0

            label_from = command[1]
            label_to = command[2]

            try:
                self.__my_graph.AddEdge(label_from, label_to)
            except Exception as e:
                print(repr(e))
                return 0
            else:
                print(f"Edge from '{label_from}' to '{label_to}' added.")

        elif command[0] == 'print':
            if 1 != len(command):
                print(f"Invalid number of arguments! 'print' command expects 1 arguments, {len(command)} were given.")
                return 0
            self.__my_graph.Print()
        elif command[0] == 'exit':
            print("Exiting...")
            return 1

        elif command[0] == 'sim':
            if 2 == len(command):
                if 'start' == command[1]:
                    self.__my_pagerank = pagerank.PageRank(self.__my_graph)
                elif 'stop' == command[1]:
                    del self.__my_pagerank
                    self.__my_pagerank = None
                else:
                    print("Invalid command.")
                    return 0
            elif 3 == len(command):
                if 'step' == command[1]:
                    if not self.__my_pagerank:
                        print("Need to start simulation first!")
                        return 0
                    self.__my_pagerank.StepN(int(command[2]))
                elif 'setp' == command[1]:
                    self.__my_pagerank.SetRandomJump(float(command[2]))
                elif 'togglep' == command[1]:
                    if 'on' == command[2]:
                        self.__my_pagerank.ToggleRandomJump(True)
                    elif 'off' == command[2]:
                        self.__my_pagerank.ToggleRandomJump(False)
                    else:
                        print("Invalid command.")
                        return 0
            else:
                print("Invalid command.")
                return 0
        else:
            print("Invalid command.")

    def Run(self):
        random.seed(42069)
        self.__my_graph = graph.Graph()
        self.__my_pagerank = None
        while(True):
            choice = input()
            command = choice.split(' ')

            if "file" == command[0]:
                try:
                    with open(command[1], 'r') as file:
                        for line in file:
                            cmd_line = line.strip().split(' ')
                            if cmd_line:
                                self.ProcessCMD(cmd_line)
                except FileNotFoundError:
                    print("File not found:", command[1])
                except Exception as e:
                    print("An error occurred while processing the file:", e)
            else:
                if (1 == self.ProcessCMD(command)):
                    break
