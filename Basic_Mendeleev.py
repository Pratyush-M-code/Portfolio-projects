# Starting out with learning the periodic table of elements using mendeleev library in python.
import mendeleev
import pandas as pd
import numpy as np
import mendeleev


# Basic Prerequsites
website = "https://mendeleev.readthedocs.io"
print ("info from,", website)
from mendeleev import element #helps with calling differnt elements

# Calling an element
Ar = element("Ar") # Calling from atomic symbol
C = element("Carbon") # Calling from name
Mn = element(25) # Calling from atomic Number
H, O, Si = element(["H","Oxygen",14])

# Basic data
print(Ar.atomic_number) # Atomic number
print(C.name) # Name
print(Mn.symbol)
print(H.oxistates) # Most common Oxidation states returned as a LIST
print(O.ionenergies) # The ionenergies returns a dictionary with ionization energies in eV as values and degrees of ionization as keys
print(Si.ionenergies[1]) # Also presented to you in a list!
print(O.zeff())                    # default method
print(O.zeff(method='slater'))     # explicitly ask for Slater's rules