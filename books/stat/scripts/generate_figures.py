#!/usr/bin/env python3
"""
Generate figures for Probability and Statistics textbook
Creates all plots referenced in Part 1 chapters
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 11

# Create output directories
IMAGE_DIR = Path('../images')
PART1_DIR = IMAGE_DIR / 'part1'
PART2_DIR = IMAGE_DIR / 'part2'

for dir_path in [IMAGE_DIR, PART1_DIR, PART2_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

print("Generating figures for Part 1...")

# ============================================================================
# Chapter 1: Plotting Data
# ============================================================================

# Figure 1.1: Bar charts for student dataset
def generate_fig_1_1():
    """Bar charts showing gender and goals distribution"""
    # Simulated student data based on Chase and Danner study
    np.random.seed(42)
    n_students = 478
    
    # Gender distribution (roughly equal)
    genders = ['Boy', 'Girl']
    gender_counts = [240, 238]
    
    # Goals distribution
    goals = ['Sports', 'Grades', 'Popular']
    goal_counts = [140, 220, 118]  # More value grades
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gender bar chart
    ax1.bar(genders, gender_counts, color=['#4472C4', '#ED7D31'], alpha=0.8, edgecolor='black')
    ax1.set_ylabel('Number of children')
    ax1.set_title('Number of children of each gender', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 300)
    ax1.grid(axis='y', alpha=0.3)
    
    # Goals bar chart
    ax2.bar(goals, goal_counts, color=['#A5A5A5', '#FFC000', '#70AD47'], alpha=0.8, edgecolor='black')
    ax2.set_ylabel('Number of children')
    ax2.set_title('Number of children choosing each goal', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 250)
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig-bar-charts.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-bar-charts.png")

# Figure 1.2: Histograms for net worth and cheese scores
def generate_fig_1_2():
    """Histograms of net worth and cheese goodness scores"""
    # Net worth data (in $100,000s)
    net_worth = [1.00360, 1.09770, 0.96860, 0.97860, 1.08930, 
                 1.24330, 1.01300, 1.12710, 1.06740, 1.20170]
    
    # Cheese scores
    cheese_scores = [12.3, 20.9, 39.0, 47.9, 5.6, 25.9, 37.3, 21.9, 18.1, 21.0,
                     34.9, 57.2, 0.7, 25.9, 54.9, 40.9, 15.9, 6.4, 18.0, 38.9]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Net worth histogram
    ax1.hist(net_worth, bins=5, color='#4472C4', alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Net worth (in $100,000s)')
    ax1.set_ylabel('Number of data items')
    ax1.set_title('Histogram of net worth for 10 individuals', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)
    
    # Cheese scores histogram
    ax2.hist(cheese_scores, bins=6, range=(0, 60), color='#ED7D31', alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Cheese goodness score')
    ax2.set_ylabel('Number of data items')
    ax2.set_title('Histogram of cheese goodness score for 20 cheeses', fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig-histograms.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-histograms.png")

# Figure 1.3: Conditional histograms for body temperature
def generate_fig_1_3():
    """Body temperature histograms by gender"""
    np.random.seed(42)
    
    # Simulated body temperature data
    gender1_temp = np.random.normal(98.2, 0.6, 65)  # Slightly cooler
    gender2_temp = np.random.normal(98.6, 0.6, 65)  # Slightly warmer
    all_temp = np.concatenate([gender1_temp, gender2_temp])
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 10))
    
    # All temperatures
    axes[0].hist(all_temp, bins=15, range=(96, 101), color='#4472C4', alpha=0.7, edgecolor='black')
    axes[0].set_xlabel('Temperature (°F)')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Histogram of body temperatures', fontsize=12, fontweight='bold')
    axes[0].axvline(98.4, color='red', linestyle='--', linewidth=2, label='98.4°F')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    # Gender 1
    axes[1].hist(gender1_temp, bins=15, range=(96, 101), color='#ED7D31', alpha=0.7, edgecolor='black')
    axes[1].set_xlabel('Temperature (°F)')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('Gender 1 body temperatures', fontsize=12, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    # Gender 2
    axes[2].hist(gender2_temp, bins=15, range=(96, 101), color='#70AD47', alpha=0.7, edgecolor='black')
    axes[2].set_xlabel('Temperature (°F)')
    axes[2].set_ylabel('Frequency')
    axes[2].set_title('Gender 2 body temperatures', fontsize=12, fontweight='bold')
    axes[2].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig-conditional-histograms.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-conditional-histograms.png")

# Figure: Box plots demonstration
def generate_boxplot_figure():
    """Generate box plot examples"""
    np.random.seed(42)
    
    # Sample data for box plots
    data1 = np.random.normal(100, 15, 100)
    data2 = np.random.normal(110, 10, 100)
    data3 = np.random.normal(95, 20, 100)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    box_data = [data1, data2, data3]
    bp = ax.boxplot(box_data, labels=['Dataset A', 'Dataset B', 'Dataset C'],
                    patch_artist=True, notch=True)
    
    # Color the boxes
    colors = ['#4472C4', '#ED7D31', '#70AD47']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax.set_ylabel('Value')
    ax.set_title('Box Plots Comparing Three Datasets', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig-boxplots.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-boxplots.png")

# ============================================================================
# Chapter 2: Scatter plots and correlation
# ============================================================================

def generate_scatter_plots():
    """Generate scatter plot examples showing correlation"""
    np.random.seed(42)
    n = 100
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Strong positive correlation
    x1 = np.random.randn(n)
    y1 = 2 * x1 + np.random.randn(n) * 0.5
    axes[0, 0].scatter(x1, y1, alpha=0.6, color='#4472C4')
    axes[0, 0].set_title(f'Strong Positive Correlation\n(r ≈ {np.corrcoef(x1, y1)[0,1]:.2f})', fontweight='bold')
    axes[0, 0].set_xlabel('Variable X')
    axes[0, 0].set_ylabel('Variable Y')
    axes[0, 0].grid(alpha=0.3)
    
    # Strong negative correlation
    x2 = np.random.randn(n)
    y2 = -2 * x2 + np.random.randn(n) * 0.5
    axes[0, 1].scatter(x2, y2, alpha=0.6, color='#ED7D31')
    axes[0, 1].set_title(f'Strong Negative Correlation\n(r ≈ {np.corrcoef(x2, y2)[0,1]:.2f})', fontweight='bold')
    axes[0, 1].set_xlabel('Variable X')
    axes[0, 1].set_ylabel('Variable Y')
    axes[0, 1].grid(alpha=0.3)
    
    # Weak correlation
    x3 = np.random.randn(n)
    y3 = 0.3 * x3 + np.random.randn(n) * 2
    axes[1, 0].scatter(x3, y3, alpha=0.6, color='#70AD47')
    axes[1, 0].set_title(f'Weak Correlation\n(r ≈ {np.corrcoef(x3, y3)[0,1]:.2f})', fontweight='bold')
    axes[1, 0].set_xlabel('Variable X')
    axes[1, 0].set_ylabel('Variable Y')
    axes[1, 0].grid(alpha=0.3)
    
    # No correlation
    x4 = np.random.randn(n)
    y4 = np.random.randn(n)
    axes[1, 1].scatter(x4, y4, alpha=0.6, color='#A5A5A5')
    axes[1, 1].set_title(f'No Correlation\n(r ≈ {np.corrcoef(x4, y4)[0,1]:.2f})', fontweight='bold')
    axes[1, 1].set_xlabel('Variable X')
    axes[1, 1].set_ylabel('Variable Y')
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig-scatter-correlation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-scatter-correlation.png")

# ============================================================================
# Part 2: Probability figures
# ============================================================================

def generate_probability_tree():
    """Generate a simple probability tree diagram"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Probability Tree: Coin Flip Experiment', 
            ha='center', fontsize=14, fontweight='bold')
    
    # Root
    ax.plot([5, 3], [8, 6], 'k-', linewidth=2)
    ax.plot([5, 7], [8, 6], 'k-', linewidth=2)
    
    # Labels
    ax.text(5, 8.3, 'Start', ha='center', fontsize=11, 
            bbox=dict(boxstyle='round', facecolor='lightgray'))
    ax.text(3.5, 7, 'H\n(p=0.5)', ha='center', fontsize=10)
    ax.text(6.5, 7, 'T\n(p=0.5)', ha='center', fontsize=10)
    
    # Leaves
    ax.text(3, 5.7, 'Heads', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='#4472C4', alpha=0.3))
    ax.text(7, 5.7, 'Tails', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='#ED7D31', alpha=0.3))
    
    plt.tight_layout()
    plt.savefig(PART2_DIR / 'fig-probability-tree.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-probability-tree.png")

def generate_normal_distribution():
    """Generate normal distribution curves"""
    x = np.linspace(-4, 4, 1000)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Standard normal
    y = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
    ax.plot(x, y, linewidth=2.5, color='#4472C4', label='μ=0, σ=1')
    ax.fill_between(x, y, alpha=0.3, color='#4472C4')
    
    # Mark standard deviations
    for i in range(-3, 4):
        ax.axvline(i, color='gray', linestyle='--', alpha=0.5, linewidth=1)
        if i != 0:
            ax.text(i, 0.02, f'{i}σ', ha='center', fontsize=9)
    
    ax.set_xlabel('Standard Deviations from Mean', fontsize=11)
    ax.set_ylabel('Probability Density', fontsize=11)
    ax.set_title('Standard Normal Distribution', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 0.45)
    
    plt.tight_layout()
    plt.savefig(PART2_DIR / 'fig-normal-distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Generated fig-normal-distribution.png")

# ============================================================================
# Main execution
# ============================================================================

if __name__ == '__main__':
    print("="*60)
    print("Generating figures for Probability and Statistics textbook")
    print("="*60)
    
    # Part 1 figures
    print("\n[Part 1: Describing Datasets]")
    generate_fig_1_1()
    generate_fig_1_2()
    generate_fig_1_3()
    generate_boxplot_figure()
    generate_scatter_plots()
    
    # Part 2 figures
    print("\n[Part 2: Probability]")
    generate_probability_tree()
    generate_normal_distribution()
    
    print("\n" + "="*60)
    print(f"✓ All figures generated successfully!")
    print(f"✓ Images saved to: {IMAGE_DIR.absolute()}")
    print("="*60)
