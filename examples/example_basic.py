"""
Example 1: Basic usage of the Riemann zeta function.

This example demonstrates:
- Computing zeta values at various points
- Evaluating on the critical line
- Checking known zeros
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from riemann_hypothesis import RiemannZeta


def main():
    # Initialize the calculator
    rz = RiemannZeta(precision=50)
    
    print("Example 1: Basic Zeta Function Usage")
    print("=" * 60)
    
    # Compute zeta at real values
    print("\n1. Computing ζ(s) for real s > 1:")
    for s in [2, 3, 4, 5]:
        result = rz.zeta(s)
        print(f"   ζ({s}) = {result.real:.10f}")
    
    # Note: ζ(2) = π²/6 ≈ 1.6449340668
    print(f"\n   Known: ζ(2) = π²/6 ≈ {(3.14159265359**2)/6:.10f}")
    
    # Compute zeta at complex values
    print("\n2. Computing ζ(s) for complex s:")
    test_points = [
        1 + 2j,
        0.5 + 10j,
        0.5 + 14.134725j,  # Near first zero
        2 + 5j
    ]
    
    for s in test_points:
        result = rz.zeta(s)
        print(f"   ζ({s}) = {result:.6f}")
    
    # Evaluate on critical line
    print("\n3. Evaluating on the critical line (Re(s) = 1/2):")
    for t in [0, 5, 10, 15, 20]:
        result = rz.zeta_on_critical_line(t)
        print(f"   ζ(1/2 + {t}i) = {result:.6f}")
    
    # Check known zeros
    print("\n4. Checking known zeros:")
    known_zeros = rz.get_known_zeros(5)
    for i, t in enumerate(known_zeros, 1):
        zeta_val = rz.zeta_on_critical_line(t)
        print(f"   Zero {i}: t = {t:.6f}")
        print(f"            ζ(1/2 + it) = {zeta_val:.6e}")
        print(f"            |ζ(1/2 + it)| = {abs(zeta_val):.6e}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
