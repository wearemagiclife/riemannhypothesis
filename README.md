# riemannhypothesis
Riemann Hypothesis

## Phi Function Visualization

This repository contains an implementation of the truncated kernel function Phi_N(x) and its derivative, along with visualization code.

### Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the visualization script:

```bash
python riemann_phi.py
```

This will:
- Compute Phi_N(x) for x in [-10, 10]
- Generate a plot showing the function
- Display the minimum value of the function
- Save the plot as `phi_plot.png`

### Functions

- `Phi(x, N=100)`: Computes the truncated kernel Phi_N(x)
- `dPhi(x, N=100)`: Computes the derivative of Phi_N(x)
