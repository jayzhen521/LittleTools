import sys
from cmd import Cmd
import re

class ShaderString(Cmd):
    intro = '''====Shader String Generator, designed by "Searching Center, Energysh"====
    You can git source code from:https://github.com/jayzhen521/LittleTools.git
    Type help or ? to list commands.
    '''

    def default(self, argv):

        parameters = argv.split(' ')
        
        if parameters and parameters[0] != "exit" and len(parameters) >= 1:
            
            filename = parameters[0]
            filenameOut = filename + ".txt"

            target = ""

            with open(filename, 'rt') as f:

                while True:
                    line = f.readline()
                    if not line:
                        break

                    line = re.sub('\n', '', line)

                    target += '"{} \\n" +\n'.format(line)

                target += '"\\n"'
                
            print(target)

            with open(filenameOut, "wt") as f:
                f.write(target)

    def do_exit(self, arg):
        'Stop run'
        print('Stop running')
        # self.close()
        return True
                    

if __name__ == '__main__':
    ShaderString().cmdloop()