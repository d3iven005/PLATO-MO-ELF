# PLATO-MO-ELF
A python code for PLATO molecular orbital (MO) and electron localization function (ELF) calculation
# USAGE
Before using this code, ensure that you have Python 'numpy' package and PLATO (A package of programs for building tight binding models) installed. PLATO is a free program and for PLATO installation requests, please contact Prof. Andrew Horsfield via a.horsfield@imperial.ac.uk.
 1. Run PLATO "tb1" calculation to generate "*.wf" and "*.xyz" file.
 2. Copy "*.wf" and "*.xyz" to the "00_inputdata/" folder. Some version of PLATO for non-periodic calculation will generate ".wf" file without K-point information. Please copy "K-point 1   0.00000   0.00000   0.00000 1.0000000000" to the first line of ".wf" file.
 3. Modify the parameters in "input.py" as needed, and run this code.
 4. The output will be saved in the "01_results/" folder, visualise the "*.cube" file by VMD or other visualisation software.
# EXAMPLE
Some "*.wf" and "*.xyz" files has been pre-placed in the "00_inputdata/" folder. The default input file is configured for ELF calculation of a water molecule.
# NOTICE
The ELF code right now is calculated under its original defination in real space, which results in very low calculation efficiency. This calculation can be held in reciprocal space after Fourier transformation. The gradient of wavefunction phi and charge density will be equal to ik(Phi(k)) and ik(rho(k)), which will increase the calculation efficiency significantly. This will be done in the future.
