# Riemann Hypothesis

A Python implementation for exploring the Riemann Hypothesis through numerical computation of the Riemann zeta function and its zeros.

## Overview

The **Riemann Hypothesis** is one of the most important unsolved problems in mathematics. It states that all non-trivial zeros of the Riemann zeta function ζ(s) have real part equal to 1/2 (i.e., they lie on the "critical line").

This repository provides tools to:
- Compute the Riemann zeta function for complex arguments
- Find zeros on the critical line numerically
- Verify that zeros lie on the critical line
- Visualize the zeta function and its zeros

## Installation

1. Clone this repository:
```bash
git clone https://github.com/wearemagiclife/riemannhypothesis.git
cd riemannhypothesis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from riemann_hypothesis import RiemannZeta

# Initialize the calculator
rz = RiemannZeta(precision=50)

# Compute zeta at a point
result = rz.zeta(2)  # ζ(2) = π²/6
print(f"ζ(2) = {result}")

# Compute on the critical line
result = rz.zeta_on_critical_line(14.134725)
print(f"ζ(1/2 + 14.134725i) = {result}")

# Find zeros numerically
zeros = rz.find_zeros_on_critical_line(0, 50, num_points=2000)
print(f"Found {len(zeros)} zeros")
```

### Running Examples

```bash
# Basic usage example
python riemann_hypothesis.py

# Example 1: Basic computations
python examples/example_basic.py

# Example 2: Finding and verifying zeros
python examples/example_zeros.py
```

### Creating Visualizations

```bash
# Generate all visualizations
python visualize.py
```

This will create three PNG files:
- `critical_line_zeros.png` - Zeros on the critical line
- `zeta_critical_line.png` - Real and imaginary parts of ζ(1/2 + it)
- `zeta_magnitude.png` - Magnitude of ζ in the complex plane

## Features

### 1. Riemann Zeta Function Computation

The `RiemannZeta` class provides multiple methods for computing ζ(s):

- **`zeta(s)`** - Compute ζ(s) for any complex or real s
- **`zeta_on_critical_line(t)`** - Compute ζ(1/2 + it) on the critical line
- High-precision computation using mpmath library

### 2. Zero Finding

- **`find_zeros_on_critical_line(t_min, t_max, num_points)`** - Find zeros numerically
- Uses the Hardy Z-function for robust zero detection
- Bisection method for precise zero refinement
- **`verify_zero_on_critical_line(t, tol)`** - Verify zeros lie on critical line

### 3. Known Zeros

- **`get_known_zeros(count)`** - Get the first 10 known non-trivial zeros
- Compare numerical results with analytical values

### 4. Visualization Tools

The `visualize.py` module provides:

- **`plot_zeta_magnitude()`** - 2D heatmap of |ζ(s)| in the complex plane
- **`plot_critical_line_zeros()`** - Hardy Z-function and zero locations
- **`plot_zeta_on_critical_line()`** - Real and imaginary parts of ζ(1/2 + it)

## Mathematical Background

### The Riemann Zeta Function

The Riemann zeta function is defined for Re(s) > 1 as:

```
ζ(s) = Σ(n=1 to ∞) 1/n^s
```

It can be analytically continued to the entire complex plane (except s = 1).

### The Riemann Hypothesis

**Statement**: All non-trivial zeros of ζ(s) have real part equal to 1/2.

The first few non-trivial zeros (imaginary parts) are:
- 14.134725...
- 21.022040...
- 25.010858...
- 30.424876...
- 32.935062...

### The Hardy Z-Function

The Hardy Z-function is a real-valued function defined on the critical line:

```
Z(t) = exp(iθ(t)) · ζ(1/2 + it)
```

where θ(t) is the Riemann-Siegel theta function. Zeros of Z(t) correspond to zeros of ζ on the critical line.

## Examples

### Computing Zeta Values

```python
from riemann_hypothesis import RiemannZeta

rz = RiemannZeta()

# Real argument
print(rz.zeta(2))  # π²/6 ≈ 1.6449340668

# Complex argument
print(rz.zeta(0.5 + 14.134725j))  # Near first zero
```

### Finding Zeros

```python
# Find zeros in range [0, 100]
zeros = rz.find_zeros_on_critical_line(0, 100, num_points=5000)

# Verify each zero
for t in zeros:
    is_valid = rz.verify_zero_on_critical_line(t)
    print(f"Zero at t={t:.6f}, valid: {is_valid}")
```

### Visualization

```python
from visualize import plot_critical_line_zeros

# Plot zeros and Hardy Z-function
plot_critical_line_zeros(0, 100, 5000, save_path='zeros.png')
```

## API Reference

### RiemannZeta Class

#### Methods

- **`__init__(precision=50)`** - Initialize with specified decimal precision
- **`zeta(s)`** - Compute ζ(s) for complex or real s
- **`zeta_on_critical_line(t)`** - Compute ζ(1/2 + it)
- **`find_zeros_on_critical_line(t_min, t_max, num_points)`** - Find zeros
- **`verify_zero_on_critical_line(t, tol=1e-6)`** - Verify a zero
- **`get_known_zeros(count)`** - Get first known zeros

## Dependencies

- **numpy** - Numerical computations
- **scipy** - Special functions (zeta for real arguments)
- **matplotlib** - Visualization
- **mpmath** - High-precision arithmetic and special functions

## Performance Notes

- Computing zeros requires significant calculation time
- Higher `num_points` gives more accurate zero locations but takes longer
- Use lower precision for faster computation (e.g., `precision=30`)
- The Hardy Z-function computation is optimized using mpmath's `siegelz`

## References

1. Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Größe"
2. Edwards, H.M. (1974). "Riemann's Zeta Function"
3. Borwein, P. et al. (2008). "The Riemann Hypothesis: A Resource for the Afficionado and Virtuoso Alike"

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

This implementation uses:
- The mpmath library for high-precision computation
- The Hardy Z-function for efficient zero finding
- The Riemann-Siegel formula (via mpmath) for accurate computation
