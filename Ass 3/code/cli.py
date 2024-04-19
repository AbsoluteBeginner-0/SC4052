import graph
import nltk
import random
import shlex
import textrank

class CLI:
    __my_graph = None
    __my_textrank = None

    def ProcessCMD(self, command):

        if command[0] == 'sentence':
            if 2 != len(command):
                print(f"Invalid number of arguments! 'sentence' command expects 1 arguments, {len(command)} were given.")
                return 0
            self.__my_graph.AddNode(command[1])

        elif command[0] == 'text':
            if 3 == len(command):
                if 'readlines' == command[1]:
                    with open(command[2], 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            self.__my_graph.AddNode(line)
                    return 0
                print(f"Invalid command!")
                return 0
                            
            if 2 != len(command):
                print(f"Invalid number of arguments! 'text' command expects 1 arguments, {len(command)} were given.")
                return 0
            
            with open(command[1], 'r') as file:
                content = file.read()

            sentences = nltk.sent_tokenize(content)
            for sentence in sentences:
                self.__my_graph.AddNode(sentence)
             
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
                    self.__my_textrank = textrank.TextRank(self.__my_graph)
                elif 'stop' == command[1]:
                    if not self.__my_textrank:
                        print("[TextRank]: Need to start simulation first!")
                        return 0

                    del self.__my_textrank
                    self.__my_textrank = None
                    print("[TextRank]: Simulation ended!")
                else:
                    print("Invalid command.")
                    return 0
            elif 3 == len(command):
                if not self.__my_textrank:
                        print("[TextRank]: Need to start simulation first!")
                        return 0
                
                if 'gettop' == command[1]:
                    print(self.__my_textrank.GetTopN(int(command[2])))
                if 'step' == command[1]:
                    self.__my_textrank.StepN(int(command[2]))
                elif 'setp' == command[1]:
                    self.__my_textrank.SetRandomJump(float(command[2]))
                elif 'togglep' == command[1]:
                    if 'on' == command[2]:
                        self.__my_textrank.ToggleRandomJump(True)
                    elif 'off' == command[2]:
                        self.__my_textrank.ToggleRandomJump(False)
                    else:
                        print("Invalid command.")
                        return 0
                elif command[1] == 'verbose':
                    if 'on' == command[2]:
                        self.__my_textrank.SetVerbose(True)
                    elif 'off' == command[2]:
                        self.__my_textrank.SetVerbose(False)
                    else:
                        print("Invalid command.")
                        return 0
        
        else:
            print("Invalid command.")

    def Run(self):
        random.seed(42069)
        self.__my_graph = graph.Graph()
        self.__my_textrank = None
        while(True):
            choice = input()
            command = shlex.split(choice)

            if not command:
                continue

            if "file" == command[0]:
                try:
                    with open(command[1], 'r') as file:
                        for line in file:
                            cmd_line = line.strip().split(' ')
                            if cmd_line:
                                if 1 == self.ProcessCMD(cmd_line):
                                    return
                except FileNotFoundError:
                    print("File not found:", command[1])
                except Exception as e:
                    print("An error occurred while processing the file:", e)
            else:
                if (1 == self.ProcessCMD(command)):
                    break
