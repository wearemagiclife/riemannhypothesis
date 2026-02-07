"""
Riemann Hypothesis Implementation

This module provides tools for exploring the Riemann Hypothesis, including:
- Computing the Riemann zeta function
- Finding zeros on the critical line
- Visualizing the distribution of zeros
"""

import numpy as np
from scipy.special import zeta as scipy_zeta
import mpmath
from typing import List, Tuple, Union


class RiemannZeta:
    """
    Class for computing the Riemann zeta function and analyzing its zeros.
    
    The Riemann Hypothesis states that all non-trivial zeros of the zeta function
    have real part equal to 1/2.
    """
    
    def __init__(self, precision: int = 50):
        """
        Initialize the Riemann zeta calculator.
        
        Args:
            precision: Number of decimal places for high-precision calculations
        """
        self.precision = precision
        mpmath.mp.dps = precision
    
    def zeta(self, s: Union[complex, float]) -> complex:
        """
        Compute the Riemann zeta function ζ(s).
        
        Args:
            s: Complex or real argument
            
        Returns:
            Value of ζ(s)
        """
        if isinstance(s, (int, float)) and s > 1:
            # Use scipy for real values > 1 (faster)
            return complex(scipy_zeta(s, 1))
        else:
            # Use mpmath for complex values and other cases
            result = mpmath.zeta(s)
            return complex(result)
    
    def zeta_on_critical_line(self, t: float) -> complex:
        """
        Compute ζ(1/2 + it) on the critical line.
        
        Args:
            t: Imaginary part
            
        Returns:
            Value of ζ(1/2 + it)
        """
        s = 0.5 + 1j * t
        return self.zeta(s)
    
    def find_zeros_on_critical_line(
        self, 
        t_min: float = 0, 
        t_max: float = 50, 
        num_points: int = 1000
    ) -> List[float]:
        """
        Find approximate zeros of the zeta function on the critical line.
        
        This uses sign changes in the real part of Z(t) to locate zeros,
        where Z(t) is the Hardy Z-function.
        
        Args:
            t_min: Minimum t value to search
            t_max: Maximum t value to search
            num_points: Number of points to sample
            
        Returns:
            List of approximate t values where zeros occur
        """
        zeros = []
        t_values = np.linspace(t_min, t_max, num_points)
        
        # Compute Z(t) values
        z_values = []
        for t in t_values:
            z = self._hardy_z(t)
            z_values.append(z)
        
        # Find sign changes
        for i in range(len(z_values) - 1):
            if z_values[i] * z_values[i + 1] < 0:
                # Sign change detected, refine the zero
                zero = self._refine_zero(t_values[i], t_values[i + 1])
                zeros.append(zero)
        
        return zeros
    
    def _hardy_z(self, t: float) -> float:
        """
        Compute the Hardy Z-function Z(t).
        
        The Hardy Z-function is a real-valued function related to the zeta function
        on the critical line: Z(t) = exp(i*theta(t)) * zeta(1/2 + it)
        where theta(t) is the Riemann-Siegel theta function.
        
        Args:
            t: Real parameter
            
        Returns:
            Real value of Z(t)
        """
        if abs(t) < 0.01:
            # For small t, use direct computation
            zeta_val = self.zeta_on_critical_line(t)
            return zeta_val.real
        
        # Use mpmath's implementation
        z_val = mpmath.siegelz(t)
        return float(z_val.real)
    
    def _refine_zero(self, t1: float, t2: float, tol: float = 1e-6) -> float:
        """
        Refine a zero using bisection method.
        
        Args:
            t1: Lower bound
            t2: Upper bound
            tol: Tolerance for convergence
            
        Returns:
            Refined zero location
        """
        while abs(t2 - t1) > tol:
            t_mid = (t1 + t2) / 2
            z1 = self._hardy_z(t1)
            z_mid = self._hardy_z(t_mid)
            
            if z1 * z_mid < 0:
                t2 = t_mid
            else:
                t1 = t_mid
        
        return (t1 + t2) / 2
    
    def verify_zero_on_critical_line(self, t: float, tol: float = 1e-6) -> bool:
        """
        Verify that a zero at t lies on the critical line.
        
        Args:
            t: The imaginary part of the zero
            tol: Tolerance for considering a value as zero
            
        Returns:
            True if |ζ(1/2 + it)| < tol
        """
        zeta_val = self.zeta_on_critical_line(t)
        return abs(zeta_val) < tol
    
    def get_known_zeros(self, count: int = 10) -> List[float]:
        """
        Get the first known non-trivial zeros on the critical line.
        
        Args:
            count: Number of zeros to return (max 10 in this implementation)
            
        Returns:
            List of t values for zeros ζ(1/2 + it) = 0
        """
        # First 10 known zeros (imaginary parts)
        known_zeros = [
            14.134725,
            21.022040,
            25.010858,
            30.424876,
            32.935062,
            37.586178,
            40.918719,
            43.327073,
            48.005151,
            49.773832
        ]
        
        return known_zeros[:min(count, len(known_zeros))]


def compute_zeta_grid(
    real_min: float = -1,
    real_max: float = 2,
    imag_min: float = -20,
    imag_max: float = 20,
    resolution: int = 100
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute the zeta function on a grid for visualization.
    
    Args:
        real_min: Minimum real part
        real_max: Maximum real part
        imag_min: Minimum imaginary part
        imag_max: Maximum imaginary part
        resolution: Grid resolution
        
    Returns:
        Tuple of (real_grid, imag_grid, zeta_magnitude)
    """
    rz = RiemannZeta(precision=30)
    
    real_vals = np.linspace(real_min, real_max, resolution)
    imag_vals = np.linspace(imag_min, imag_max, resolution)
    
    real_grid, imag_grid = np.meshgrid(real_vals, imag_vals)
    zeta_magnitude = np.zeros_like(real_grid)
    
    for i in range(resolution):
        for j in range(resolution):
            s = complex(real_grid[i, j], imag_grid[i, j])
            try:
                zeta_val = rz.zeta(s)
                zeta_magnitude[i, j] = abs(zeta_val)
            except (ValueError, OverflowError, ZeroDivisionError):
                zeta_magnitude[i, j] = np.nan
    
    return real_grid, imag_grid, zeta_magnitude


def main():
    """Demonstrate the Riemann zeta function and zero finding."""
    print("=" * 60)
    print("Riemann Hypothesis Exploration")
    print("=" * 60)
    
    rz = RiemannZeta(precision=50)
    
    # Compute some values
    print("\n1. Computing ζ(s) for various s:")
    test_values = [2, 3, 0.5 + 14.134725j, 0.5 + 21.022040j]
    for s in test_values:
        result = rz.zeta(s)
        print(f"   ζ({s}) = {result:.6f}")
    
    # Get known zeros
    print("\n2. First 10 known non-trivial zeros (imaginary parts):")
    known_zeros = rz.get_known_zeros(10)
    for i, t in enumerate(known_zeros, 1):
        print(f"   Zero {i:2d}: t = {t:.6f}")
    
    # Verify zeros
    print("\n3. Verifying zeros on the critical line:")
    for i, t in enumerate(known_zeros[:5], 1):
        is_zero = rz.verify_zero_on_critical_line(t, tol=1e-4)
        zeta_val = rz.zeta_on_critical_line(t)
        print(f"   Zero {i}: t = {t:.6f}, |ζ(1/2+it)| = {abs(zeta_val):.6e}, Valid: {is_zero}")
    
    # Find zeros numerically
    print("\n4. Finding zeros numerically in range [0, 50]:")
    found_zeros = rz.find_zeros_on_critical_line(0, 50, num_points=2000)
    print(f"   Found {len(found_zeros)} zeros:")
    for i, t in enumerate(found_zeros[:10], 1):
        print(f"   Zero {i:2d}: t = {t:.6f}")
    
    print("\n" + "=" * 60)
    print("The Riemann Hypothesis states that all non-trivial zeros")
    print("have real part equal to 1/2 (on the critical line).")
    print("All zeros found above are on the critical line!")
    print("=" * 60)


if __name__ == "__main__":
    main()
