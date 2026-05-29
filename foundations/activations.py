import numpy as np
from numpy.typing import NDArray
import math


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        for i in range(len(z)):
            z[i] = round(1 / (1 + math.e ** (-z[i])), 5)
        return z

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        for i in range(len(z)):
            z[i] = max(0,z[i])
        # Formula: max(0, z) element-wise
        return z
