###  e2.70

import os,sys
QumPyPath = os.path.join(os.environ['PROJECTS'],'20230113_QumPy')
sys.path.append(QumPyPath)
from Circuit.Circuit import Circuit


#  inital state 
import sympy
from sympy import *

e1 = symbols('e_1',real=True)
e2 = symbols('e_2',real=True)

Psi0 = [0,1,0,0]

# S = [[1/sqrt(2),1/sqrt(2)],[1/sqrt(2),-1/sqrt(2)]]
t= symbols('theta',real=True)

S = [[ cos(t) , sin(t)],[ -sin(t), -cos(t)]]


Sd = [[conjugate(S[0][0]),conjugate(S[1][0])],
      [conjugate(S[0][1]),conjugate(S[1][1])]]
E = [[e1,0],[0,e2]]
c = Circuit(Nq=2,IsSymbol=True,Psi =Psi0 )


# circuit
c.H(0).CNOT(0,1).Gate_U2(0,Sd).Gate_U2(0,E).Gate_U2(0,S).CNOT(0,1).H(0)




s = 0 
for i in range(len(c.c)):
    s += conjugate(c.c[i]) * Psi0[i]
print(simplify(s))