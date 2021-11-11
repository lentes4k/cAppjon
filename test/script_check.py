import sys
sys.path.append(".")
import subprocess

def check():
 
  salida = subprocess.check_output('pylint --errors-only cappjon')
  
  return salida
