"""
Visualization tools for the Riemann Hypothesis.

This module provides functions to visualize the Riemann zeta function
and its zeros.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from riemann_hypothesis import RiemannZeta, compute_zeta_grid


def plot_zeta_magnitude(
    real_min: float = -1,
    real_max: float = 2,
    imag_min: float = -30,
    imag_max: float = 30,
    resolution: int = 200,
    save_path: str = None
):
    """
    Plot the magnitude of the zeta function in the complex plane.
    
    Args:
        real_min: Minimum real part
        real_max: Maximum real part
        imag_min: Minimum imaginary part
        imag_max: Maximum imaginary part
        resolution: Grid resolution
        save_path: Path to save the figure (optional)
    """
    print(f"Computing zeta function on grid ({resolution}x{resolution})...")
    real_grid, imag_grid, zeta_magnitude = compute_zeta_grid(
        real_min, real_max, imag_min, imag_max, resolution
    )
    
    print("Creating plot...")
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Use log scale for better visualization
    zeta_magnitude_log = np.log10(np.clip(zeta_magnitude, 1e-10, None))
    
    im = ax.contourf(
        real_grid, imag_grid, zeta_magnitude_log,
        levels=50, cmap='viridis'
    )
    
    # Draw the critical line
    ax.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='Critical Line (Re=1/2)')
    
    ax.set_xlabel('Real Part', fontsize=12)
    ax.set_ylabel('Imaginary Part', fontsize=12)
    ax.set_title('Magnitude of Riemann Zeta Function (log scale)', fontsize=14)
    ax.legend()
    
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('log₁₀(|ζ(s)|)', fontsize=11)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Figure saved to {save_path}")
    else:
        plt.show()
    
    plt.close()


def plot_critical_line_zeros(
    t_min: float = 0,
    t_max: float = 100,
    num_points: int = 5000,
    save_path: str = None
):
    """
    Plot the zeros of the zeta function on the critical line.
    
    Args:
        t_min: Minimum t value
        t_max: Maximum t value
        num_points: Number of points to sample
        save_path: Path to save the figure (optional)
    """
    rz = RiemannZeta(precision=30)
    
    print(f"Computing Hardy Z-function on [{t_min}, {t_max}]...")
    t_values = np.linspace(t_min, t_max, num_points)
    z_values = [rz._hardy_z(t) for t in t_values]
    
    print("Finding zeros...")
    zeros = rz.find_zeros_on_critical_line(t_min, t_max, num_points)
    
    print(f"Found {len(zeros)} zeros")
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot Z(t)
    ax1.plot(t_values, z_values, 'b-', linewidth=0.5, label='Z(t)')
    ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax1.scatter(zeros, [0]*len(zeros), color='red', s=30, zorder=5, label='Zeros')
    ax1.set_xlabel('t', fontsize=12)
    ax1.set_ylabel('Z(t)', fontsize=12)
    ax1.set_title('Hardy Z-function on Critical Line', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot zero distribution
    if len(zeros) > 0:
        ax2.scatter(zeros, [0.5]*len(zeros), color='red', s=50, alpha=0.6)
        ax2.set_xlabel('t (Imaginary part of zero)', fontsize=12)
        ax2.set_ylabel('')
        ax2.set_title(f'Distribution of {len(zeros)} Zeros on Critical Line', fontsize=14)
        ax2.set_ylim([0, 1])
        ax2.set_yticks([])
        ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Figure saved to {save_path}")
    else:
        plt.show()
    
    plt.close()


def plot_zeta_on_critical_line(
    t_min: float = 0,
    t_max: float = 50,
    num_points: int = 1000,
    save_path: str = None
):
    """
    Plot the real and imaginary parts of ζ(1/2 + it).
    
    Args:
        t_min: Minimum t value
        t_max: Maximum t value  
        num_points: Number of points to sample
        save_path: Path to save the figure (optional)
    """
    rz = RiemannZeta(precision=30)
    
    print(f"Computing ζ(1/2 + it) on [{t_min}, {t_max}]...")
    t_values = np.linspace(t_min, t_max, num_points)
    zeta_values = [rz.zeta_on_critical_line(t) for t in t_values]
    
    real_parts = [z.real for z in zeta_values]
    imag_parts = [z.imag for z in zeta_values]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Real part
    ax1.plot(t_values, real_parts, 'b-', linewidth=1)
    ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax1.set_xlabel('t', fontsize=12)
    ax1.set_ylabel('Re(ζ(1/2 + it))', fontsize=12)
    ax1.set_title('Real Part of Zeta on Critical Line', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    # Imaginary part
    ax2.plot(t_values, imag_parts, 'r-', linewidth=1)
    ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5, alpha=0.3)
    ax2.set_xlabel('t', fontsize=12)
    ax2.set_ylabel('Im(ζ(1/2 + it))', fontsize=12)
    ax2.set_title('Imaginary Part of Zeta on Critical Line', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Figure saved to {save_path}")
    else:
        plt.show()
    
    plt.close()


def main():
    """Generate various visualizations."""
    print("=" * 60)
    print("Riemann Hypothesis Visualizations")
    print("=" * 60)
    
    # Plot zeros on critical line
    print("\n1. Plotting zeros on critical line...")
    plot_critical_line_zeros(0, 100, 5000, 'critical_line_zeros.png')
    
    # Plot zeta on critical line
    print("\n2. Plotting ζ(1/2 + it)...")
    plot_zeta_on_critical_line(0, 50, 1000, 'zeta_critical_line.png')
    
    # Plot magnitude in complex plane
    print("\n3. Plotting magnitude in complex plane...")
    plot_zeta_magnitude(-1, 2, -30, 30, 150, 'zeta_magnitude.png')
    
    print("\n" + "=" * 60)
    print("Visualizations complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
