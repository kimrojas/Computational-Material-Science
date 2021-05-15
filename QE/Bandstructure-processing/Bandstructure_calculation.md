## Band Structure Calculation

This is a step-by-step guide in doing a band structure calculation. For this guide, I used MoS2. The sample input files are in the corresponding folder. I also added comments on the input files.


**Required:**
 - Quantum espresso (serial/parallel)
 - XCRYSDEN
 - matplotlib

### Relaxation

1. Make sure you have your desired structure. You can use xcrysden to view the structure of the atoms on your input.
2. Run the command ```pw.x -in mos2_0_relax.in > mos2_0_relax.out```



### scf calculation

3. On the **mos2_0_relax.out** output file, you will get the final coordinates, like the one you see below.
```
Begin final coordinates
     new unit-cell volume =    888.34771 a.u.^3 (   131.63955 Ang^3 )
     density =      2.01919 g/cm^3

CELL_PARAMETERS (alat=  6.01701403)
   0.999769978   0.000000000   0.000000000
  -0.499884989   0.865826199   0.000000000
   0.000000000   0.000000000   4.710956589

ATOMIC_POSITIONS (angstrom)
Mo            0.0000000000        0.0000000000        7.0635563422
S             1.5916667979        0.9189495730        8.6258544907
S             1.5916667979        0.9189495730        5.5012581671
End final coordinates
```
4. Multiple the alat value to v1(1) to get the new lattice parameter (a) . In this case, we have
```
6.01701403 Bohr * 0.999769978 Bohr = 6.0156299844 Bohr
```

***NOTE:*** 
In my input, I used A (not celldm(1)), so I needed to convert the new lattice vector to Angstrom. 
</br> 6.0156299844 Bohr = 3.1833343 Angstrom

7. Use the new lattice parameter *A* (or celldm(1)) for the succeeding calculations.
8. Run the command ``` pw.x -in mos2_1_scf.in > mos2_1_scf.out ``` . (See sample input file in the bands folder)

### nscf calculation
9. Run the command ``` pw.x -in mos2_2_nscf.in > mos2_2_nscf.out ``` . (See sample input file in the bands folder)

***NOTE:*** 
 - Make sure you increase the K_POINTS in your nscf calculation.
 - The input file is the same as the scf calculation input file. **The only parameter you need to change is the K_POINTS.**

### pw.x bands calculationk
10. Using xcrysden, open any of your previous input files (relaxation, scf, nscf). Go to Tools then click k-path selection.
11. Draw the k-path you want to calculate. You will see the corresponding coordinates on the right panel.
12. Run the command ``` pw.x -in mos2_3_pwbands.in > mos2_3_pwbands.out ``` . (See input file in the bands folder)
 
### bands.x calculation
13. Run the command ``` bands.x -in mos2_4_bands.in > mos2_4_bands.out ```.  (See input file in the bands folder)

### Plotting

14. Use the sample code **bands.ipynb** (see plotting folder). Edit the code to appropriately suite your need.
 
***NOTE:*** 
Make sure to change the values needed, like the Fermi Energy, based on your own calculation.
