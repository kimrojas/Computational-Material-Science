#!/usr/bin/env python3
import sys
from tqdm import tqdm
from time import sleep
import subprocess  as sp

py=sp.check_output("which python3", shell=True).strip().decode('ascii')
ver=sp.check_output("python -V", shell=True).strip().decode('ascii')
print("PYTHON: ", py)
print(ver)




# --------------------------------------------------------------------------------------------------
def help ():
    print (f"""
usage: {sys.argv[0]} [-h] -i INPUT [-o OUTPUT]

Expands the unit cell in the x,y, and z direction thus creating a supercell. 
** Follow file formatting carefully. 

Options:
    -h, --help      show this help message and exit
    -i, --input     Input file (default: input.txt)
    -o, --output    Output file (default: output.txt)

Required File Format:

<n_a>        <n_b>        <n_c>

<cell_a1>    <cell_a2>    <cell_a3>
<cell_b1>    <cell_b2>    <cell_b3>
<cell_c1>    <cell_c2>    <cell_c3>

A   1.0     2.0     3.0
B   3.0     2.0     1.0
.   .       .       .
.   .       .       .
.   .       .       .
Z   4.0     5.0     6.0
    """)
    sys.exit()
# --------------------------------------------------------------------------------------------------

def cell_f(x):
    return [round(x, 11) for x in list(map(float, x))]

def assign_dat(t_dat, l_dat):
    if t_dat is 'ntimes': return (map(float, l_dat))
    if t_dat is 'cell': return cell_f(l_dat[0]),cell_f(l_dat[1]), cell_f(l_dat[2])
    if t_dat is 'pos': 
        label = str(l_dat[0])
        coord = list(map(float, l_dat[1:]))
        return list((label, coord[0], coord[1], coord[2]))

def calc_cell(n, c):
    return [n*x for x in c]

def calc_pos(na, nb, nc, ca, cb, cc, plist):
    pos = []
    for atm in plist:
        for k in range(int(nc)):
            for j in range(int(nb)):
                for i in range(int(na)):            
                    x = round(atm[1] + i*ca[0] + j*cb[0] + k*cc[0], 11)
                    y = round(atm[2] + i*ca[1] + j*cb[1] + k*cc[1], 11)
                    z = round(atm[3] + i*ca[2] + j*cb[2] + k*cc[2], 11)
                    pos.append ([atm[0], x,y,z])
    return pos 

def main():
    # DEFAULTS
    inp_f = "input.txt"
    out_f = "output.txt"

    # Arguments
    opt, args = sys.argv[1::2], sys.argv[2::2]
    if any(i in opt for i in ['-h', '--help']): help()
        
    for i in range(len(opt)):
        if opt[i] in ['-i', '--input']: inp_f = args[i]
        if opt[i] in ['-o', '--output']: out_f = args[i]

    # Read data

    inp_data = open(inp_f, 'r')
    Lines = inp_data.read().splitlines()

    ## Separate elements with empty line filter
 
    input_list = []
    for line in tqdm(Lines, desc="Reading {}".format(inp_f), ascii=True, ncols=100):
        line_s = line.split()
        if list(line_s) != []: input_list.append(line_s)
    inp_data.close()

    # Assign values
    na,nb,nc = assign_dat('ntimes', input_list[0])
    ca, cb, cc = assign_dat('cell', input_list[1:4])
    p_list=[]
    for i in tqdm(input_list[4:], desc="Processing data", ascii=True, ncols=100): 
        p_list.append(assign_dat('pos', i))

    # Calculate cell parameter
    A,B,C = calc_cell(na,ca),calc_cell(nb,cb), calc_cell(nc,cc)

    # Calculate Atom positions
    pos = calc_pos(na, nb, nc, ca, cb, cc, p_list)

    # Write to output
    f = open(out_f, 'w')
    f.write("CELL_PARAMETERS (angstrom)\n")
    f.write("%17.11f %17.11f %17.11f\n" % (A[0], A[1], A[2])) 
    f.write("%17.11f %17.11f %17.11f\n" % (B[0], B[1], B[2])) 
    f.write("%17.11f %17.11f %17.11f\n" % (C[0], C[1], C[2])) 
    f.write("\n")
    f.write("ATOMIC_POSITIONS (angstrom)\n")
    string_ = "%5s %17.11f %17.11f %17.11f\n"
    for i in tqdm(pos, desc="Writing to {}".format(out_f), ascii=True, ncols=100): 
        f.write ( string_ % (i[0],i[1], i[2], i[3])); sleep(0.05)
    f.close()

# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    
