#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:58:46 2020

@author: juferoga
"""
import numpy as np

# ========================================= #
# Inicializando el problema de optimización #
# ========================================= #

"""
design for
min z(x) = ct*x
s.t
Ax <= b
x >= 0
"""


# ===================================== #
# Analizando la matriz de restricciones #
# ===================================== #

def check(A,b,c):
    """Check the matrix.
    Con la matriz ingresada se checkea la matriz
    """
    
    a2 = np.zeros((1, len(A[0,:])), dtype=np.float64)
    a3 = np.zeros((1, len(A[0,:])), dtype=np.float64)
    B = np.zeros((len(b), len(b)), dtype=np.float64)
    for i in range(len(B[0,:])):
        B[i,i] = 1
    
    # Variables basicas
    x = list(np.zeros(len(b), dtype=np.int))
    
    for i in range(len(A[:,0])):
        for j in range(len(A[0,:])):
            
            if A[i,j] == 1:
                a2[0,:] = A[i,:]
                a2[0,j] = 0                
                if (a2 == a3).all():
                    x[j] = i+1
    
    for i in range (len(x)):
        
        if x[i] == 0:
            A = np.vstack((A, B[:,i]))
            x[i] = len(A[:,0])
    
    A = np.transpose(A)
    d = np.zeros(len(A[0,:]) - len(c))
    c = np.hstack((c,d))
    B,D,a = basica(A,x)
    
    return A,B,D,c,x

# ============================ #
# Construir Basica y No basica #
# ============================ #
    
def basica(A,x):
    
    """ Crea la matriz con las variables basicas.
    Con la matriz ingresada crea la matrix de variables basicas
    """
    
    B = np.zeros((len(A[:,0]), len(A[:,0])), dtype=np.float64)    
    D = np.zeros((len(A[:,0]), len(A[0,:])-len(A[:,0])), dtype=np.float64)
    a = list(np.zeros(len(A[0,:]), dtype=np.int))

    for i in range (len(a)):
        
        a[i] = i+1
    
    for i in range (len(x)):
        
        a.remove(x[i])
        B[:,i] = A[:,x[i]-1]
    
    for i in range(len(a)):
                  
        D[:,i] = A[:,a[i]-1]

    return B,D,a

# =================================== #
# Revisar El vector de costo relativo #
# =================================== #

def cost_vector(B,D,c,x,a):
    
    cb = np.zeros(len(B[:,0]))
    cd = np.zeros(len(D[0,:]))
    
    for i in range (len(x)):
        
        cb[i] = c[x[i]-1]
    
    for i in range (len(a)):
        
        cd[i] = c[a[i]-1]
         
    else:
        pi = np.dot(cb, np.linalg.inv(B))
        cd_ = cd - pi.dot(D)            
    
    return cd_

# ============ #
# Primera Fase #
# ============ #

def phase1(A,b,c,equ):
   
    
    """Realizaciòn fase 1.
    Le damos un procesamiento a la matriz
    con base en la primera fase del metodo simplex.
    """
    
    # Variables artificiales
    ar = list(np.zeros(len(equ), dtype=int))
    A1 = np.vstack((A.T, c)).T
    equ = np.hstack((equ, '='))
    b1 = np.hstack((b, 0))
    cr = np.zeros(len(c), dtype=np.float64)

    B = np.zeros((len(equ), len(equ)), dtype=np.float64)
    for i in range(len(B[0,:])):
        B[i,i] = 1
        
    for i in range (len(equ)):
        
        if equ[i] == '=':
            a1 = np.delete(A1, i, axis=1)
            
            w = 0
            for j in range (len(a1[:,0])):
                if (a1[j,:] == 0).all():
                    w = 1
            if w == 0:
                A1 = np.vstack((A1, B[:,i]))
                cr = np.hstack((cr, 1))
    
    cr[len(cr)-1] = 0
    j = 0
    for i in range (len(cr)):
        if cr[i] == 1:
            ar[j] = i+1
            j += 1                   
    
    A1,B,D,cr,x = check(A1,b1,cr)
    B,D,a = basica(A1,x)
    cd_ = cost_vector(B,D,cr,x,a)
            
    contador_iter = 0

    if np.linalg.det(B) == 0:
        print("No existe solucion factible")
        
    else:
        b_ = np.dot(np.linalg.inv(B), b1)

        if min(cd_) >= 0:
    
            x = x
            np.asarray
        else:
            while list(set(x) & set(ar)) != []:
        
                for i in range (len(cd_)):
                    
                    if cd_[i] == min(cd_):
                        if cd_[i] < 0:
                            enter = a[i]
                
                a_ = np.dot(np.linalg.inv(B), A1[:,enter-1])
            
                if max(a_) <= 0:
                    print("El problema no tiene limites.")
                    x = [0]
                    break
                    
                if contador_iter >= 50:
                    x = [0]
                    print("Iterativo")
                    break
        
                else:
                    contador_iter = contador_iter + 1
                    print("Iteración Fase 1", contador_iter)
                    
                    nz = np.zeros(len(a_), dtype = int)
                    b_ = np.delete(b_, len(b_)-1)
                    a_ = np.delete(a_, len(a_)-1)
                    for i in range (len(a_)):
                        if a_[i] > 0:
                            nz[i] = i + 1
                            nz2 = np.nonzero(nz)
                            nz2 = nz2[0]
                            a2 = np.zeros(len(nz2))
                            b2 = np.zeros(len(nz2))
                                    
                    for i in range (len(a2)):
                                        
                        a2[i] = a_[nz[nz2[i]] - 1]
                        b2[i] = b_[nz[nz2[i]] - 1]
                        
                    for i in range (len(a_)):
                                        
                        if a_[i] > 0:
                            if b_[i]/a_[i] == min(b2/a2):
                                salga = i
                        
                    x[salga] = enter                    
                    B,D,a = basica(A1,x)
                    b_ = np.dot(np.linalg.inv(B), b1)
                    cd_ = cost_vector(B,D,cr,x,a)
    
    A = np.transpose(A)
    x.remove(x[len(x)-1])
    B,D,a = basica(A,x)
    
    return A,B,D,c,x

# ======================= #
# Método simplex revisado #
# ======================= #
    
def rev_simplex(a_,b_,cd_,a,x):
   
    """Revisión Simplex.
    Le damos un procesamiento a la matriz
    con base en el método simplex.
    """
    for i in range (len(cd_)):
                    
        if cd_[i] == min(cd_):
            if cd_[i] < 0:
                enter = a[i]    
                
    nz = np.zeros(len(a_), dtype = int)
    for i in range (len(a_)):
        if a_[i] > 0:
            nz[i] = i + 1
            nz2 = np.nonzero(nz)
            nz2 = nz2[0]
            a2 = np.zeros(len(nz2))
            b2 = np.zeros(len(nz2))
                    
    for i in range (len(a2)):
                        
        a2[i] = a_[nz[nz2[i]] - 1]
        b2[i] = b_[nz[nz2[i]] - 1]
        
    for i in range (len(a_)):
                        
        if a_[i] > 0:
            if b_[i]/a_[i] == min(b2/a2):
                salga = i
        
    x[salga] = enter
        
    return x

# =========================== #
# Revised Dual Simplex Method #
# =========================== #
    
def rev_dual(A,B,D,b,c,a,x):
    
    """Aqui revisamos Simplex dual.
    Le damos un procesamiento a la matriz
    con base en el método simplex dual.
    """
    b_ = np.dot(np.linalg.inv(B), b)
    contador_iter = 0
    
    while min(b_) < 0:
        contador_iter = contador_iter + 1
        print("Iteracion", contador_iter)
        
        bp = np.dot(np.linalg.inv(B), D)
        bp1 = np.zeros(len(bp[0]))
        
        if (bp >= 0).all():
            print("No hay solución factible")
            x = [0]
            break

        else:
            for i in range (len(b_)):
                        
                if b_[i] == min(b_):
                    if b_[i] < 0:
                        bp1 = bp[i]
            
            cb = np.zeros(len(B[:,0]))
            cd = np.zeros(len(D[0,:]))
        
            for i in range (len(x)):
            
                cb[i] = c[x[i]-1]
        
            for i in range (len(a)):
            
                cd[i] = c[a[i]-1]
                
            zc = np.dot(cb.dot(np.linalg.inv(B)), D) - cd
            
            ng = np.zeros(len(bp1), dtype = int)
            for i in range (len(bp1)):
                if bp1[i] < 0:
                    ng[i] = i + 1
                    ng2 = np.nonzero(ng)
                    ng2 = ng2[0]
                    zc2 = np.zeros(len(ng2))
                    bp2 = np.zeros(len(ng2))
    
            for i in range (len(bp2)):
                            
                zc2[i] = zc[ng[ng2[i]] - 1]
                bp2[i] = bp1[ng[ng2[i]] - 1]
            
            for i in range (len(bp1)):
                            
                if bp1[i] < 0:
                    if abs(zc[i]/bp1[i]) == min(abs(zc2/bp2)):
                        enter = a[i]
            
            for i in range (len(b_)):
                        
                if b_[i] == min(b_):
                    if b_[i] < 0:
                        salga = i
            
            x[salga] = enter
            if len(x) > len(set(x)):
                print("No hay solución factible")
                x = [0]
                break
            B,D,a = basica(A,x)
            b_ = np.dot(np.linalg.inv(B), b)
        
    return B,D,a,x

# ==================================== #
# solucionar Problema de Optimización  #
# ==================================== #
    
def solver(A,B,D,a,b,x,c):
    
    """Solucionador del problema de otimzacón.
    
    Verifica con varios metodos la solucion si
    se puede con otra solucion se realiza, de lo
    contrario sigue con los metodos consecuentes
    """
    contador_iter = 0

    if np.linalg.det(B) == 0:
        print("No hay solucion factible")
        
    else:
        b_ = np.dot(np.linalg.inv(B), b)
                  
        if min(b_) < 0:
                    
            # ================================ #
            # Revisando el método Simplex Dual #
            # ================================ #
                        
            B,D,a,x = rev_dual(A,B,D,b,c,a,x)
                    
        else:
            
            # ============================ #
            # Revisando el método Simplex  #
            # ============================ #
            cd_ = cost_vector(B,D,c,x,a)
            
            if min(cd_) >= 0:
    
                x = x
            
            else:
                while min(cd_) < 0:
        
                    for i in range (len(cd_)):
                    
                        if cd_[i] == min(cd_):
                            if cd_[i] < 0:
                                enter = a[i]
                
                    a_ = np.dot(np.linalg.inv(B), A[:,enter-1])
            
                    if max(a_) <= 0:
                        print("Problema sin limites")
                        x = [0]
                        break
                    
                    if contador_iter >= 50:
                         x = [0]
                         print("Iterativo")
                         break
        
                    else:
                        contador_iter = contador_iter + 1
                        print("Iteracion", contador_iter)
                  
                        x = rev_simplex(a_,b_,cd_,a,x)
                        B,D,a = basica(A,x)
                        b_ = np.dot(np.linalg.inv(B), b)
                        cd_ = cost_vector(B,D,c,x,a)

    return B,D,a,x
    
# ================ #
# Solucion Optima  #
# ================ #

def s_optima(x,c,B,b):
    
    """Encuentra la solucion otima.
    Con la matriz ingresada se busca despues de realizar la
    solucion, se busca el valor mínimo de la función.
    """
    if x == [0]:
        opti_x = []
        z = []
        
    else:    
        opti_x = np.zeros(len(c))
        cb = np.zeros(len(x))
        cv = np.dot(np.linalg.inv(B), b)
        
        for i in range (len(x)):
            
            opti_x[x[i]-1] = cv[i]
            cb[i] = c[x[i]-1]
            
        z = np.dot(cb, cv)
    
    return opti_x,z    

# ======================================== #
# Solucionando el Problema de Optimización #
# ======================================== #
    
"""
# Test
A = np.transpose(np.asarray([[5,-4,13,-2,1],[1,-1,5,-1,1]], dtype=np.float64))
c = np.asarray([3,-1,-7,3,1], dtype=np.float64)
b = np.asarray([20,8], dtype=np.float64)
equ = np.asarray(['=','='], dtype=np.str)
"""
def main(c,b,equ,A):
    # ingreso de variables la vaiable opti no se tinen en cuenta
    # los splits se realizan cuando encuentre espacios en blanco
    c = np.array([float(n) for n in c.split()])
    b = np.array([float(n) for n in b.split()])
    equ = np.array([str(n) for n in equ.split()])
    # los organiza y coloca en una matriz en este caso la matriz a la que le daremos solución
    A = [float(n) for n in A.split()]
    # realiza un redimencionamiento de la matriz con las longitudes de los vectores que adquirimos
    A = np.array(A).reshape((len(c), len(b)), order='F')
    # imprimimos la matriz para verificar que este bn
    print(A.T)
    #"""
    if (equ == '=').any():
        A,B,D,c,x = phase1(A,b,c,equ)
    else:
        A,B,D,c,x = check(A,b,c)

    B,D,a = basica(A,x)

    B,D,a,x = solver(A,B,D,a,b,x,c)
    opti_x,z = s_optima(x,c,B,b)

    return opti_x,z
    
