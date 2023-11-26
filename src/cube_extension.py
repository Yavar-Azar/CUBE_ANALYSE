import numpy as np
from ase.io.cube import read_cube_data


class CubeDataReader:
    def __init__(self, cube_file):
        """Initialize the CubeDataReader instance from a cube file.

        Args:
            cube_file (str): Path to the cube file.
        """
        self._load_cube_data(cube_file)

    def _load_cube_data(self, cube_file):
        """Load cube data and perform validation."""
        data, atoms = read_cube_data(cube_file)

        self._validate_cube_data(data, atoms)
        self._initialize_attributes(data, atoms)

    def _validate_cube_data(self, data, atoms):
        """Validate the consistency and validity of the cube data."""
        if len(data.shape) != 3:
            raise ValueError("Invalid data shape")

        if len(atoms) > 0:
            raise ValueError("There is no atom")

    def _initialize_attributes(self, data, atoms):
        """Initialize instance attributes from the cube data."""
        self.natoms = len(atoms)
        self.orthorhombic = atoms.cell.orthorhombic
        self.atomic_positions = atoms.get_positions()
        self.chemical_symbols = atoms.get_chemical_symbols()
        self.grid_shape = data.shape
        self.cell = atoms.cell

    @property
    def diff_vol(self):
        """Calculate the difference in volume between the unit cell and the grid volume."""
        a, b, c = self.cell.lengths
        volume_diff = np.prod(self.grid_shape) * (a * b * c) - np.prod(self.cell)
        return volume_diff

    def display_info(self):
        """Display information about the cube data."""
        print(f"Number of atoms: {self.natoms}")
        print(f"Orthorhombic cell: {self.orthorhombic}")
        print(f"Grid shape: {self.grid_shape}")
        print(f"Cell lengths: {self.cell.lengths}")
        print(f"Difference in volume: {self.diff_vol}")

