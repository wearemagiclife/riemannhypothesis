import numpy as np
import matplotlib.pyplot as plt


def Phi(x, N=100):
    """
    Compute the truncated kernel Phi_N(x).
    
    Parameters:
    -----------
    x : float
        Input value
    N : int
        Number of terms in the summation (default=100)
    
    Returns:
    --------
    float
        Value of Phi_N(x)
    """
    total = 0
    for n in range(1, N+1):
        decay = np.exp(-np.pi * n**2 * np.exp(2 * x))
        total += decay
    return 2 * total


def dPhi(x, N=100):
    """
    Compute the derivative of the truncated kernel Phi_N(x).
    
    Parameters:
    -----------
    x : float
        Input value
    N : int
        Number of terms in the summation (default=100)
    
    Returns:
    --------
    float
        Value of dPhi_N/dx(x)
    """
    total = 0
    for n in range(1, N+1):
        term1 = 2 * np.pi**2 * n**4 * np.exp(4.5 * x)
        term2 = 3 * np.pi * n**2 * np.exp(2.5 * x)
        decay = np.exp(-np.pi * n**2 * np.exp(2 * x))
        total += (term1 - term2) * decay
    return 2 * total


# Generate data for plotting
x_vals = np.linspace(-10, 10, 1000)
phi_vals = np.array([Phi(x) for x in x_vals])

# Create the plot
plt.figure()
plt.plot(x_vals, phi_vals, label='Phi(x)')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title("Plot truncated kernel Phi_N(x)")
plt.xlabel('x')
plt.ylabel('Phi_N(x)')
plt.legend()
plt.grid(True, alpha=0.3)

# Print minimum value
print("Minimum value of Phi_N(x):", np.min(phi_vals))

# Save the plot
plt.savefig('phi_plot.png', dpi=150, bbox_inches='tight')
print("Plot saved to phi_plot.png")

# Show the plot
plt.show()
