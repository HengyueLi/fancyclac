#!/sr/bin/env python3 


###  2023-05-05

import sympy


class DecomposeU:
    
    @staticmethod
    def getU(U,i,j):
        # i <= j 
        # for a given U, use the i-th row to zerolized i-th row
        D,D = U.shape
        R = sympy.zeros(D, D) 
        for k in range(D):
            if k not in [i,j]:
                R[k,k] = 1
        a = U[i,i]
        b = U[j,i]
        ad = a.conjugate()
        bd = b.conjugate()
        norm = sympy.sqrt(  a*ad + b*bd )
        u11 = ad / norm
        u12 = bd / norm
        u21 = b / norm
        u22 = -a / norm
        R[i,i] = u11
        R[i,j] = u12
        R[j,i] = u21
        R[j,j] = u22
        return sympy.simplify(R)
    
    @classmethod
    def fullDecompose(cls,M):
        r = []
        D,D = M.shape
        Rm = M
        for i in range(0,D-1):
            for j in range(i+1,D):
                u = cls.getU(Rm,i,j)
                r.append(u)
                Rm = u * Rm
        return [sympy.simplify(m.conjugate().transpose()) for m in r] + [sympy.simplify(Rm)]
                
                
            
    
    
    @staticmethod
    def isUnitary(M):
        Md = sympy.conjugate(M).transpose()
        r = sympy.simplify( M * Md )
        D,D = r.shape
        c = 0
        for i in range(D):
            for j in range(D):
                if i == j:
                    e = r[i,j] - 1
                else:
                    e = r[i,j]
                c += e * sympy.conjugate(e)
        return c == 0
                
        
        
        
        
        
i = sympy.I
h = i**2**2 / 2
U = sympy.Matrix([
    [h,h,h,h],
    [h,h*i,-h,-i*h],
    [h,-h,h,-h],
    [h,-i*h,-h,i*h],
])



r = DecomposeU.fullDecompose(U)

sympy.simplify(r[0]*r[1]*r[2]*r[3]*r[4]*r[5]*r[6])

