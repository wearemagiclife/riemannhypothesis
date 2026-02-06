"""
Tests for the Riemann Hypothesis implementation.
"""

import unittest
import numpy as np
from riemann_hypothesis import RiemannZeta, compute_zeta_grid


class TestRiemannZeta(unittest.TestCase):
    """Test cases for the RiemannZeta class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.rz = RiemannZeta(precision=30)
    
    def test_zeta_at_2(self):
        """Test ζ(2) = π²/6."""
        result = self.rz.zeta(2)
        expected = np.pi**2 / 6
        self.assertAlmostEqual(result.real, expected, places=5)
    
    def test_zeta_at_4(self):
        """Test ζ(4) = π⁴/90."""
        result = self.rz.zeta(4)
        expected = np.pi**4 / 90
        self.assertAlmostEqual(result.real, expected, places=5)
    
    def test_zeta_complex(self):
        """Test that zeta returns complex values."""
        result = self.rz.zeta(0.5 + 10j)
        self.assertIsInstance(result, complex)
    
    def test_known_zeros(self):
        """Test that known zeros are returned correctly."""
        zeros = self.rz.get_known_zeros(5)
        self.assertEqual(len(zeros), 5)
        self.assertAlmostEqual(zeros[0], 14.134725, places=5)
        self.assertAlmostEqual(zeros[1], 21.022040, places=5)
    
    def test_verify_known_zero(self):
        """Test verification of a known zero."""
        # First known zero
        t = 14.134725
        is_valid = self.rz.verify_zero_on_critical_line(t, tol=1e-3)
        self.assertTrue(is_valid)
    
    def test_zeta_on_critical_line(self):
        """Test computation on critical line."""
        result = self.rz.zeta_on_critical_line(0)
        self.assertIsInstance(result, complex)
        # ζ(1/2) is approximately -1.460...
        self.assertAlmostEqual(result.real, -1.460, places=2)
    
    def test_find_zeros(self):
        """Test finding zeros numerically."""
        zeros = self.rz.find_zeros_on_critical_line(10, 25, num_points=1000)
        # Should find at least the zeros at ~14.13 and ~21.02
        self.assertGreater(len(zeros), 0)
        # First zero should be near 14.134725
        if len(zeros) > 0:
            self.assertLess(abs(zeros[0] - 14.134725), 0.5)
    
    def test_hardy_z_at_zero(self):
        """Test Hardy Z-function at a known zero."""
        t = 14.134725
        z_val = self.rz._hardy_z(t)
        # Should be close to 0
        self.assertLess(abs(z_val), 0.01)


class TestComputeZetaGrid(unittest.TestCase):
    """Test cases for grid computation."""
    
    def test_compute_grid(self):
        """Test computing zeta on a grid."""
        real_grid, imag_grid, zeta_mag = compute_zeta_grid(
            -1, 2, -10, 10, resolution=10
        )
        
        # Check shapes
        self.assertEqual(real_grid.shape, (10, 10))
        self.assertEqual(imag_grid.shape, (10, 10))
        self.assertEqual(zeta_mag.shape, (10, 10))
        
        # Check that magnitudes are non-negative where finite
        finite_vals = zeta_mag[~np.isnan(zeta_mag)]
        self.assertTrue(np.all(finite_vals >= 0))


def run_tests():
    """Run all tests."""
    print("Running Riemann Hypothesis Tests")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestRiemannZeta))
    suite.addTests(loader.loadTestsFromTestCase(TestComputeZetaGrid))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"Tests failed: {len(result.failures)} failures, {len(result.errors)} errors")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
