import numpy as np
import datetime
from src.count_obt import count_obt
from src.R_cal import R
from src.Y_cal import Y
from src.distnt import distnt
def PHInk_c(ifcrystal,cell_a,cell_b,cell_c,obtdictionary ,atom_xyz, kpoint_coe,kpoint, phi_coe, xyzgrid, energylevel):
    bohr = 0.529177
    ####RECIPROCAL LATTICE CONSTANT########
    if ifcrystal ==1:
        volume_factor = np.dot(cell_a,np.cross(cell_b,cell_c))
        reci_a = 2*np.pi*  np.cross(cell_b,cell_c)/volume_factor
        reci_b = 2*np.pi*  np.cross(cell_c,cell_a)/volume_factor
        reci_c = 2*np.pi*  np.cross(cell_a,cell_b)/volume_factor
    #######################################
    if ifcrystal == 0: ##non-periodic
        print("NOCALCULATING ENERGYLEVEL:",energylevel+1)
        obtinfo = count_obt(atom_xyz)
        PHI = 0
        for i in range(len(atom_xyz)):
            o_i = sum(obtinfo[:i])
            atom_pvector = np.array(  [float(atom_xyz[i][1]), float(atom_xyz[i][2]), float(atom_xyz[i][3])     ]      ) / bohr
            d_M = distnt(xyzgrid, atom_pvector)
            if obtinfo[i] == 1:
                phi = phi_coe[energylevel][o_i] * R(obtdictionary['Hs'],d_M) * Y(xyzgrid,atom_pvector,0,0)
                PHI += phi
            elif obtinfo[i] == 4:
                elementtype = atom_xyz[i][0]
                Rp = R(obtdictionary[elementtype+'p'],d_M)
                phi = phi_coe[energylevel][o_i] * R(obtdictionary[elementtype+'s'],d_M) * Y(xyzgrid,atom_pvector,0,0)
                phi += phi_coe[energylevel][o_i+1] * Rp * Y(xyzgrid,atom_pvector,0,1)
                phi += phi_coe[energylevel][o_i+2] * Rp * Y(xyzgrid,atom_pvector,1,1) 
                phi += phi_coe[energylevel][o_i+3] * Rp * Y(xyzgrid,atom_pvector,-1,1)
                PHI += phi
            elif obtinfor[i] == 9:
                PHI=PHI
    else:
        #atom_position_list =[]
        #for i in range(len(atom_xyz)):
        #    atom_position_list.append(np.array([float(atom_xyz[i][1]),float(atom_xyz[i][2]),float(atom_xyz[i][3])])/bohr)
        #atom_position_list = np.array(atom_position_list)
        atom_position_list = np.array([ [float(arr[1]),float(arr[2]),float(arr[3])] for arr in atom_xyz    ])
        d_M_list = np.array( [distnt(xyzgrid, arr) for arr in atom_position_list])

        print("CALCULATING KPOINT:",kpoint,"ENERGYLEVEL:",energylevel+1)
        k_vector = kpoint[0]*reci_a + kpoint[1]*reci_b + kpoint[2]*reci_c
        PHI = 0
        obtinfo = count_obt(atom_xyz)
        for i in range(len(atom_xyz)):
            o_i = sum(obtinfo[:i])
            atom_pvector = np.array(  [float(atom_xyz[i][1]), float(atom_xyz[i][2]), float(atom_xyz[i][3])     ]      )/bohr
            for ii in range(-1,2):
                for jj in range(-1,2):
                    for kk in range(-1,2):
                        Atom_pvector = atom_pvector + ii*cell_a + jj*cell_b +kk*cell_c
                        d_M = distnt(xyzgrid, Atom_pvector)
                        BLOCH = np.exp(1j*np.dot(xyzgrid,k_vector))  / np.exp(1j * np.dot(k_vector, Atom_pvector))                        
                        if obtinfo[i] == 1:
                            phi = phi_coe[energylevel][o_i] * R(obtdictionary['Hs'],d_M) * Y(xyzgrid,Atom_pvector,0,0)           *BLOCH
                            PHI += kpoint_coe * phi
                        elif obtinfo[i] == 4:
                            elementtype = atom_xyz[i][0]
                            Rp = R(obtdictionary[elementtype+'p'],d_M)
                            phi = phi_coe[energylevel][o_i] * R(obtdictionary[elementtype+'s'],d_M) * Y(xyzgrid,Atom_pvector,0,0)         *BLOCH
                            phi += phi_coe[energylevel][o_i+1] * Rp * Y(xyzgrid,Atom_pvector,0,1)	  *BLOCH
                            phi += phi_coe[energylevel][o_i+2] * Rp * Y(xyzgrid,Atom_pvector,1,1)	  *BLOCH
                            phi += phi_coe[energylevel][o_i+3] * Rp * Y(xyzgrid,Atom_pvector,-1,1)	  *BLOCH
                            PHI += kpoint_coe * phi
                        elif obtinfo[i] == 9:
                            PHI=PHI
            
    return PHI
