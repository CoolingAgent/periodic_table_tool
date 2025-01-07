class Element:
    def __init__(self, name, symbol, atomic_number, mass, group, period, category, electronegativity, electron_shells, valence_electrons):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.mass = mass
        self.group = group
        self.period = period
        self.category = category
        self.electronegativity = electronegativity
        self.electron_shells = electron_shells
        self.valence_electrons = valence_electrons



print(" The periodic table:")
elements = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "", ""],
    ["", "", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "", ""]
]

# Print the periodic table
for row in elements:
    row_str = ""
    for element in row:
        if element == "":
            row_str += "|   "
        else:
            row_str += "|{} ".format(element.ljust(2))
    row_str += "|"
    print(row_str)
    print("|---" * 18 + "|")


# Dictionary representing the periodic table
periodic_table = {
"H": Element("Hydrogen", "H", 1, 1.008, 1, 1, "Non-metal", 2.20, "1s", 1),
    "He": Element("Helium", "He", 2, 4.002602, 18, 1, "Noble gas", None, "1s", 2),
    "Li": Element("Lithium", "Li", 3, 6.94, 1, 2, "Alkali metal", 0.98, "2s", 1),
    "Be": Element("Beryllium", "Be", 4, 9.0121831, 2, 2, "Alkaline earth metal", 1.57, "2s", 2),
    "B": Element("Boron", "B", 5, 10.81, 13, 2, "Metalloid", 2.04, "2s2 2p", 3),
    "C": Element("Carbon", "C", 6, 12.011, 14, 2, "Non-metal", 2.55, "2s2 2p", 4),
    "N": Element("Nitrogen", "N", 7, 14.007, 15, 2, "Non-metal", 3.04, "2s2 2p", 5),
    "O": Element("Oxygen", "O", 8, 15.999, 16, 2, "Non-metal", 3.44, "2s2 2p", 6),
    "F": Element("Fluorine", "F", 9, 18.998403163, 17, 2, "Non-metal", 3.98, "2s2 2p", 7),
    "Ne": Element("Neon", "Ne", 10, 20.1797, 18, 2, "Noble gas", None, "2s2 2p", 8),
    "Na": Element("Sodium", "Na", 11, 22.98976928, 1, 3, "Alkali metal", 0.93, "3s", 1),
    "Mg": Element("Magnesium", "Mg", 12, 24.305, 2, 3, "Alkaline earth metal", 1.31, "3s", 2),
    "Al": Element("Aluminum", "Al", 13, 26.9815385, 13, 3, "Metal", 1.61, "3s2 3p", 3),
    "Si": Element("Silicon", "Si", 14, 28.085, 14, 3, "Metalloid", 1.90, "3s2 3p", 4),
    "P": Element("Phosphorus", "P", 15, 30.973761998, 15, 3, "Non-metal", 2.19, "3s2 3p", 5),
    "S": Element("Sulfur", "S", 16, 32.06, 16, 3, "Non-metal", 2.58, "3s2 3p", 6),
    "Cl": Element("Chlorine", "Cl", 17, 35.45, 17, 3, "Non-metal", 3.16, "3s2 3p", 7),
    "Ar": Element("Argon", "Ar", 18, 39.9481, 18, 3, "Noble gas", None, "3s2 3p", 8),
    "K": Element("Potassium", "K", 19, 39.0983, 1, 4, "Alkali metal", 0.82, "4s", 1),
    "Ca": Element("Calcium", "Ca", 20, 40.078, 2, 4, "Alkaline earth metal", 1.00, "4s", 2),
    "Sc": Element("Scandium", "Sc", 21, 44.955908, 3, 4, "Transition metal", 1.36, "4s2 3d", 3),
    "Ti": Element("Titanium", "Ti", 22, 47.867, 4, 4, "Transition metal", 1.54, "4s2 3d", 4),
    "V": Element("Vanadium", "V", 23, 50.9415, 5, 4, "Transition metal", 1.63, "4s2 3d", 5),
    "Cr": Element("Chromium", "Cr", 24, 51.9961, 6, 4, "Transition metal", 1.66, "4s1 3d", 6),
    "Mn": Element("Manganese", "Mn", 25, 54.938044, 7, 4, "Transition metal", 1.55, "4s2 3d", 7),
    "Fe": Element("Iron", "Fe", 26, 55.845, 8, 4, "Transition metal", 1.83, "4s2 3d", 8),
    "Co": Element("Cobalt", "Co", 27, 58.933194, 9, 4, "Transition metal", 1.88, "4s2 3d", 9),
    "Ni": Element("Nickel", "Ni", 28, 58.6934, 10, 4, "Transition metal", 1.91, "4s2 3d", 10),
    "Cu": Element("Copper", "Cu", 29, 63.546, 11, 4, "Transition metal", 1.90, "4s1 3d", 11),
    "Zn": Element("Zinc", "Zn", 30, 65.38, 12, 4, "Transition metal", 1.65, "4s2 3d", 12),
    "Ga": Element("Gallium", "Ga", 31, 69.723, 13, 4, "Metal", 1.81, "4s2 3d 4p", 13),
    "Ge": Element("Germanium", "Ge", 32, 72.630, 14, 4, "Metalloid", 2.01, "4s2 3d 4p", 14),
    "As": Element("Arsenic", "As", 33, 74.921595, 15, 4, "Metalloid", 2.18, "4s2 3d 4p", 15),
    "Se": Element("Selenium", "Se", 34, 78.971, 16, 4, "Non-metal", 2.55, "4s2 3d 4p", 16),
    "Br": Element("Bromine", "Br", 35, 79.904, 17, 4, "Non-metal", 2.96, "4s2 3d 4p", 17),
    "Kr": Element("Krypton", "Kr", 36, 83.7982, 18, 4, "Noble gas", None, "4s2 3d 4p", 18),
    "Rb": Element("Rubidium", "Rb", 37, 85.4678, 1, 5, "Alkali metal", 0.82, "5s", 1),
    "Sr": Element("Strontium", "Sr", 38, 87.62, 2, 5, "Alkaline earth metal", 0.95, "5s", 2),
    "Y": Element("Yttrium", "Y", 39, 88.90584, 3, 5, "Transition metal", 1.22, "5s2 4d", 3),
    "Zr": Element("Zirconium", "Zr", 40, 91.224, 4, 5, "Transition metal", 1.33, "5s2 4d", 4),
    "Nb": Element("Niobium", "Nb", 41, 92.90637, 5, 5, "Transition metal", 1.6, "5s1 4d", 5),
    "Mo": Element("Molybdenum", "Mo", 42, 95.95, 6, 5, "Transition metal", 2.16, "5s1 4d", 6),
    "Tc": Element("Technetium", "Tc", 43, 98, 7, 5, "Transition metal", 1.9, "5s2 4d", 7),
    "Ru": Element("Ruthenium", "Ru", 44, 101.07, 8, 5, "Transition metal", 2.2, "5s1 4d", 8),
    "Rh": Element("Rhodium", "Rh", 45, 102.90550, 9, 5, "Transition metal", 2.28, "5s1 4d", 9),
    "Pd": Element("Palladium", "Pd", 46, 106.42, 10, 5, "Transition metal", 2.2, "5s1 4d", 10),
    "Ag": Element("Silver", "Ag", 47, 107.8682, 11, 5, "Transition metal", 1.93, "5s1 4d", 11),
    "Cd": Element("Cadmium", "Cd", 48, 112.414, 12, 5, "Transition metal", 1.69, "5s2 4d", 12),
    "In": Element("Indium", "In", 49, 114.818, 13, 5, "Metal", 1.78, "5s2 4d 5p", 13),
    "Sn": Element("Tin", "Sn", 50, 118.710, 14, 5, "Metal", 1.96, "5s2 4d 5p", 14),
    "Sb": Element("Antimony", "Sb", 51, 121.760, 15, 5, "Metalloid", 2.05, "5s2 4d 5p", 15),
    "Te": Element("Tellurium", "Te", 52, 127.60, 16, 5, "Metalloid", 2.1, "5s2 4d 5p", 16),
    "I": Element("Iodine", "I", 53, 126.90447, 17, 5, "Non-metal", 2.66, "5s2 4d 5p", 17),
    "Xe": Element("Xenon", "Xe", 54, 131.2936, 18, 5, "Noble gas", None, "5s2 4d 5p", 18),
    "Cs": Element("Cesium", "Cs", 55, 132.90545196, 1, 6, "Alkali metal", 0.79, "6s", 1),
    "Ba": Element("Barium", "Ba", 56, 137.327, 2, 6, "Alkaline earth metal", 0.89, "6s", 2),
    "La": Element("Lanthanum", "La", 57, 138.90547, 3, 6, "Lanthanide", 1.10, "6s2 5d", None),
    "Ce": Element("Cerium", "Ce", 58, 140.116, 19, 6, "Lanthanide", 1.12, "6s2 5d", None),
    "Pr": Element("Praseodymium", "Pr", 59, 140.90766, 20, 6, "Lanthanide", 1.13, "6s2 5d", None),
    "Nd": Element("Neodymium", "Nd", 60, 144.242, 21, 6, "Lanthanide", 1.14, "6s2 5d", None),
    "Pm": Element("Promethium", "Pm", 61, 145, 22, 6, "Lanthanide", 0.0, "6s2 5d", None),
    "Sm": Element("Samarium", "Sm", 62, 150.36, 23, 6, "Lanthanide", 1.17, "6s2 5d", None),
    "Eu": Element("Europium", "Eu", 63, 151.964, 24, 6, "Lanthanide", 0.0, "6s2 5d", None),
    "Gd": Element("Gadolinium", "Gd", 64, 157.25, 25, 6, "Lanthanide", 1.20, "6s2 5d", None),
    "Tb": Element("Terbium", "Tb", 65, 158.92535, 26, 6, "Lanthanide", 1.20, "6s2 5d", None),
    "Dy": Element("Dysprosium", "Dy", 66, 162.500, 27, 6, "Lanthanide", 1.22, "6s2 5d", None),
    "Ho": Element("Holmium", "Ho", 67, 164.93033, 28, 6, "Lanthanide", 1.23, "6s2 5d", None),
    "Er": Element("Erbium", "Er", 68, 167.259, 29, 6, "Lanthanide", 1.24, "6s2 5d", None),
    "Tm": Element("Thulium", "Tm", 69, 168.93422, 30, 6, "Lanthanide", 1.25, "6s2 5d", None),
    "Yb": Element("Ytterbium", "Yb", 70, 173.045, 31, 6, "Lanthanide", 1.1, "6s2 5d", None),
    "Lu": Element("Lutetium", "Lu", 71, 174.9668, 32, 6, "Lanthanide", 1.27, "6s2 5d", None),
    "Hf": Element("Hafnium", "Hf", 72, 178.49, 4, 6, "Transition metal", 1.3, "6s2 5d", 4),
    "Ta": Element("Tantalum", "Ta", 73, 180.94788, 5, 6, "Transition metal", 1.5, "6s2 5d", 5),
    "W": Element("Tungsten", "W", 74, 183.84, 6, 6, "Transition metal", 2.36, "6s2 5d", 6),
    "Re": Element("Rhenium", "Re", 75, 186.207, 7, 6, "Transition metal", 1.9, "6s2 5d", 7),
    "Os": Element("Osmium", "Os", 76, 190.23, 8, 6, "Transition metal", 2.2, "6s2 5d", 8),
    "Ir": Element("Iridium", "Ir", 77, 192.217, 9, 6, "Transition metal", 2.2, "6s2 5d", 9),
    "Pt": Element("Platinum", "Pt", 78, 195.084, 10, 6, "Transition metal", 2.28, "6s1 5d", 10),
    "Au": Element("Gold", "Au", 79, 196.966569, 11, 6, "Transition metal", 2.54, "6s1 5d", 11),
    "Hg": Element("Mercury", "Hg", 80, 200.592, 12, 6, "Transition metal", 2.00, "6s2 5d", 12),
    "Tl": Element("Thallium", "Tl", 81, 204.38, 13, 6, "Metal", 2.04, "6s2 5d 6p", 13),
    "Pb": Element("Lead", "Pb", 82, 207.2, 14, 6, "Metal", 2.33, "6s2 5d 6p", 14),
    "Bi": Element("Bismuth", "Bi", 83, 208.98040, 15, 6, "Metal", 2.02, "6s2 5d 6p", 15),
    "Po": Element("Polonium", "Po", 84, 209, 16, 6, "Metalloid", 2.0, "6s2 5d 6p", 16),
    "At": Element("Astatine", "At", 85, 210, 17, 6, "Metalloid", 2.2, "6s2 5d 6p", 17),
    "Rn": Element("Radon", "Rn", 86, 222, 18, 6, "Noble gas", None, "6s2 5d 6p", 18),
    "Fr": Element("Francium", "Fr", 87, 223, 1, 7, "Alkali metal", None, "7s", 1),
    "Ra": Element("Radium", "Ra", 88, 226, 2, 7, "Alkaline earth metal", None, "7s", 2),
    "Ac": Element("Actinium", "Ac", 89, 227, 3, 7, "Actinide", None, "7s2 6d", None),
    "Th": Element("Thorium", "Th", 90, 232.0377, 3, 7, "Actinide", None, "7s2 6d", None),
    "Pa": Element("Protactinium", "Pa", 91, 231.03588, 3, 7, "Actinide", None, "7s2 6d", None),
    "U": Element("Uranium", "U", 92, 238.02891, 3, 7, "Actinide", None, "7s2 6d", None),
    "Np": Element("Neptunium", "Np", 93, 237, 3, 7, "Actinide", None, "7s2 6d", None),
    "Pu": Element("Plutonium", "Pu", 94, 244, 3, 7, "Actinide", None, "7s2 6d", None),
    "Am": Element("Americium", "Am", 95, 243, 3, 7, "Actinide", None, "7s2 6d", None),
    "Cm": Element("Curium", "Cm", 96, 247, 3, 7, "Actinide", None, "7s2 6d", None),
    "Bk": Element("Berkelium", "Bk", 97, 247, 3, 7, "Actinide", None, "7s2 6d", None),
    "Cf": Element("Californium", "Cf", 98, 251, 3, 7, "Actinide", None, "7s2 6d", None),
    "Es": Element("Einsteinium", "Es", 99, 252, 3, 7, "Actinide", None, "7s2 6d", None),
    "Fm": Element("Fermium", "Fm", 100, 257, 3, 7, "Actinide", None, "7s2 6d", None),
    "Md": Element("Mendelevium", "Md", 101, 258, 3, 7, "Actinide", None, "7s2 6d", None),
    "No": Element("Nobelium", "No", 102, 259, 3, 7, "Actinide", None, "7s2 6d", None),
    "Lr": Element("Lawrencium", "Lr", 103, 266, 3, 7, "Actinide", None, "7s2 6d", None),
    "Rf": Element("Rutherfordium", "Rf", 104, 267, 4, 7, "Transition metal", None, "7s2 6d", None),
    "Db": Element("Dubnium", "Db", 105, 268, 5, 7, "Transition metal", None, "7s2 6d", None),
    "Sg": Element("Seaborgium", "Sg", 106, 269, 6, 7, "Transition metal", None, "7s2 6d", None),
    "Bh": Element("Bohrium", "Bh", 107, 270, 7, 7, "Transition metal", None, "7s2 6d", None),
    "Hs": Element("Hassium", "Hs", 108, 269, 8, 7, "Transition metal", None, "7s2 6d", None),
    "Mt": Element("Meitnerium", "Mt", 109, 278, 9, 7, "Unknown", None, "7s2 6d", None),
    "Ds": Element("Darmstadtium", "Ds", 110, 281, 10, 7, "Unknown", None, "7s2 6d", None),
    "Rg": Element("Roentgenium", "Rg", 111, 282, 11, 7, "Unknown", None, "7s2 6d", None),
    "Cn": Element("Copernicium", "Cn", 112, 285, 12, 7, "Transition metal", None, "7s2 6d", None),
    "Nh": Element("Nihonium", "Nh", 113, 286, 13, 7, "Unknown", None, "7s2 6d", None),
    "Fl": Element("Flerovium", "Fl", 114, 289, 14, 7, "Unknown", None, "7s2 6d", None),
    "Mc": Element("Moscovium", "Mc", 115, 290, 15, 7, "Unknown", None, "7s2 6d", None),
    "Lv": Element("Livermorium", "Lv", 116, 293, 16, 7, "Unknown", None, "7s2 6d", None),
    "Ts": Element("Tennessine", "Ts", 117, 294, 17, 7, "Unknown", None, "7s2 6d", None),
    "Og": Element("Oganesson", "Og", 118, 294, 18, 7, "Unknown", None, "7s2 6d", None),
}

def get_element_info(symbol):
    element = periodic_table.get(symbol)
    if element:
        return (element.name, element.atomic_number, element.mass, element.group, element.period, element.category, element.electronegativity, element.electron_shells, element.valence_electrons)
    else:
        return 

def main():
    print("Welcome to the Periodic Table!")
    print("Enter an element symbol to get information (e.g., H for Hydrogen)")
    symbol = input("Element Symbol: ").capitalize()
    element_info = get_element_info(symbol)
    if element_info:
        name, atomic_number, mass, group, period, category, electronegativity, electron_shells, valence_electrons = element_info
        print(f"Name: {name}")
        print(f"Atomic Number: {atomic_number}")
        print(f"Atomic Mass: {mass}")
        print(f"Group: {group}")
        print(f"Period: {period}")
        print(f"Category: {category}")
        print(f"Electronegativity: {electronegativity}")
        print(f"Electron Shells: {electron_shells}")
        print(f"Valence Electrons: {valence_electrons}")
    else:
        print("Element not found in the periodic table.")

if __name__ == "__main__":
    main()
