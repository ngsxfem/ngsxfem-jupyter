import scipy.sparse as sp
import matplotlib.pylab as plt
from xfem import *
from ngsolve.webgui import Draw

def ShowPattern(A,precision=-1,binarize=False):
    rows_all,cols_all,vals_all = A.COO()
    # fes = a.space
    # if testspace == None:
    #     testspace = fes
    for i,(r,c,v) in enumerate(zip(rows_all,cols_all,vals_all)):
        vals_all[i] = abs(vals_all[i])
        if binarize and vals_all[i] > precision:
            vals_all[i] = 1.0
        #         if testspace.CouplingType(r) == COUPLING_TYPE.WIREBASKET_DOF and fes.CouplingType(c) == COUPLING_TYPE.WIREBASKET_DOF:
        #         elif testspace.CouplingType(r) == COUPLING_TYPE.WIREBASKET_DOF or fes.CouplingType(c) == COUPLING_TYPE.WIREBASKET_DOF:
        #             vals_all[i] = 6/7
        #         elif testspace.CouplingType(r) == COUPLING_TYPE.INTERFACE_DOF and fes.CouplingType(c) == COUPLING_TYPE.INTERFACE_DOF:
        #             vals_all[i] = 5/7
        #         elif testspace.CouplingType(r) == COUPLING_TYPE.INTERFACE_DOF or fes.CouplingType(c) == COUPLING_TYPE.INTERFACE_DOF:
        #             vals_all[i] = 4/7
        #         elif testspace.CouplingType(r) == COUPLING_TYPE.LOCAL_DOF or fes.CouplingType(c) == COUPLING_TYPE.LOCAL_DOF:
        #             vals_all[i] = 3/7
        #         elif testspace.CouplingType(r) == COUPLING_TYPE.HIDDEN_DOF and fes.CouplingType(c) == COUPLING_TYPE.HIDDEN_DOF:
        #             vals_all[i] = 2/7
        #         elif testspace.CouplingType(r) == COUPLING_TYPE.HIDDEN_DOF or fes.CouplingType(c) == COUPLING_TYPE.HIDDEN_DOF:
        #             vals_all[i] = 1/7
        #         else:
        #             vals_all[i] = 0.0
    minval = 0
    maxval = max(vals_all)
    A_all = sp.csr_matrix((vals_all,(rows_all,cols_all)),shape=(A.height,A.width))
    plt.figure(figsize=(4,4*A.width/A.width))
    plt.imshow(A_all.todense(),interpolation='none',cmap='jet',vmin=minval,vmax=maxval)
    plt.show()   
