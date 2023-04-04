import sys
import subprocess
from subprocess import PIPE

class SSM:
    def ssmCheck(self,file1,file2,fname):
        subprocess.call([sys.executable,"generate_ast.py","1",file1])
        subprocess.call([sys.executable,"generate_ast.py","2",file2])
        subprocess.call([sys.executable, 'winnowing.py', 'program1', 'program2',file1,file2])