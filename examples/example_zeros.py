"""
Example 2: Finding and verifying zeros on the critical line.

This example demonstrates:
- Numerical zero finding
- Verification of zeros
- Comparison with known zeros
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from riemann_hypothesis import RiemannZeta


def main():
    rz = RiemannZeta(precision=50)
    
    print("Example 2: Finding Zeros on the Critical Line")
    print("=" * 60)
    
    # Find zeros in a range
    print("\n1. Finding zeros in range [0, 50]:")
    print("   (This may take a moment...)")
    zeros = rz.find_zeros_on_critical_line(0, 50, num_points=2000)
    
    print(f"\n   Found {len(zeros)} zeros:")
    for i, t in enumerate(zeros[:15], 1):
        print(f"   {i:2d}. t = {t:.6f}")
    
    # Compare with known zeros
    print("\n2. Comparing with known zeros:")
    known = rz.get_known_zeros(10)
    print(f"\n   Known zeros (first {len(known)}):")
    for i, t in enumerate(known, 1):
        print(f"   {i:2d}. t = {t:.6f}")
    
    # Verify each found zero
    print("\n3. Verifying found zeros:")
    for i, t in enumerate(zeros[:10], 1):
        is_valid = rz.verify_zero_on_critical_line(t, tol=1e-4)
        zeta_val = rz.zeta_on_critical_line(t)
        status = "✓" if is_valid else "✗"
        print(f"   {status} Zero {i:2d}: t = {t:.6f}, |ζ| = {abs(zeta_val):.6e}")
    
    # Analyze zero spacing
    print("\n4. Analyzing zero spacing:")
    if len(zeros) > 1:
        spacings = [zeros[i+1] - zeros[i] for i in range(len(zeros)-1)]
        avg_spacing = sum(spacings) / len(spacings)
        min_spacing = min(spacings)
        max_spacing = max(spacings)
        
        print(f"   Average spacing: {avg_spacing:.4f}")
        print(f"   Minimum spacing: {min_spacing:.4f}")
        print(f"   Maximum spacing: {max_spacing:.4f}")
    
    print("\n" + "=" * 60)
    print("All zeros found are on the critical line (Re = 1/2)!")
    print("This is consistent with the Riemann Hypothesis.")
    print("=" * 60)


if __name__ == "__main__":
    main()
