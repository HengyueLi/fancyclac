###  e4.41

import os,sys

QumPyPath = os.path.join(os.environ['PROJECTS'],'20230113_QumPy')
sys.path.append(QumPyPath)

from Circuit.Circuit import Circuit


#  inital state 
import sympy
a = sympy.symbols("psi_a")
b = sympy.symbols("psi_b")
Psi = [a,b] + [ 0 ]*6

c = Circuit(Nq=3,IsSymbol=True,Psi=Psi)
c.H(1).H(2).TOFFOLI(1,2,0).S(0).TOFFOLI(1,2,0).H(1).H(2)
for i in range(len(c.c)):
    print(i,sympy.simplify(c.c[i]))