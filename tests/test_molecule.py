from chempkg.mol import Molecule
from chempkg.atom import *


MOLECULES = [
    ("C5H8O", {C: 5, H: 8, O: 1}),
    ("C21H18F3N5O", {C: 21, H: 18, F: 3, N: 5, O: 1}),
    ("C6H11O6PS", {C: 6, H: 11, O: 6, P: 1, S: 1}),
    ("C6H3ClN2O4", {C: 6, H: 3, Cl: 1, N: 2, O: 4}),
    ("C6H4Cl2O", {C: 6, H: 4, Cl: 2, O: 1}),
    ("C6H4Cl2O", {C: 6, H: 4, Cl: 2, O: 1}),
    ("CH3COOC6H4COOH", {C: 9, H: 8, O: 4}),
]

def test_molecules():

    for mol_name, expected_atoms in MOLECULES:
        mol = Molecule(mol_name)
        assert isinstance(mol.weight, float)

        for at, num in expected_atoms.items():
            assert num == mol.atoms.get(at)
        
    
if __name__ == "__main__":
    test_molecules()
