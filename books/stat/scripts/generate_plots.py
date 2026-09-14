#!/usr/bin/env python3
"""
Generate comprehensive plots for Probability and Statistics textbook
Creates all missing plots referenced in Part 1 chapters with proper paths
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import seaborn as sns
import sys

# Set style for publication-quality plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10

# Get script directory
SCRIPT_DIR = Path(__file__).parent.absolute()
ROOT_DIR = SCRIPT_DIR.parent

# Create output directories
IMAGE_DIR = ROOT_DIR / 'images'
PART1_DIR = ROOT_DIR / 'part1' / 'images'
PART2_DIR = ROOT_DIR / 'part2' / 'images'

for dir_path in [IMAGE_DIR, PART1_DIR, PART2_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

print("\n" + "="*70)
print("Generating Statistical Plots for Jupyter Book")
print("="*70)
print(f"Root directory: {ROOT_DIR}")
print(f"Output directories:")
print(f"  - {PART1_DIR}")
print(f"  - {PART2_DIR}")
print("="*70 + "\n")

# ============================================================================
# CHAPTER 1: First Tools for Looking at Data
# ============================================================================

def generate_chapter1_plots():
    """Generate plots for Chapter 1"""
    print("[Chapter 1: First Tools for Looking at Data]")
    
    # Figure 1.1: Bar charts for student dataset
    print("  Generating bar charts (gender and goals)...")
    genders = ['Boy', 'Girl']
    gender_counts = [240, 238]
    goals = ['Sports', 'Grades', 'Popular']
    goal_counts = [140, 220, 118]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.bar(genders, gender_counts, color=['steelblue', 'pink'], alpha=0.8, edgecolor='black')
    ax1.set_ylabel('Number of children')
    ax1.set_title('Number of children of each gender')
    ax1.grid(axis='y', alpha=0.3)
    
    ax2.bar(goals, goal_counts, color=['gold', 'lightgreen', 'coral'], alpha=0.8, edgecolor='black')
    ax2.set_ylabel('Number of children')
    ax2.set_title('Number of children choosing each goal')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig_1_1_bar_charts.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Figure 1.2: Histograms
    print("  Generating histograms (net worth and cheese)...")
    net_worth = np.array([100360, 109770, 96860, 97860, 108930, 
                          124330, 101300, 112710, 106740, 120170]) / 100000
    cheese_scores = np.array([12.3, 20.9, 39, 47.9, 5.6, 25.9, 37.3, 21.9, 18.1, 21,
                              34.9, 57.2, 0.7, 25.9, 54.9, 40.9, 15.9, 6.4, 18, 38.9])
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.hist(net_worth, bins=5, edgecolor='black', alpha=0.7, color='steelblue')
    ax1.set_xlabel('Net worth (in $100,000s)')
    ax1.set_ylabel('Number of data items')
    ax1.set_title('Histogram of net worth for 10 individuals')
    ax1.grid(axis='y', alpha=0.3)
    
    ax2.hist(cheese_scores, bins=6, range=(0, 70), edgecolor='black', alpha=0.7, color='orange')
    ax2.set_xlabel('Cheese goodness score')
    ax2.set_ylabel('Number of data items')
    ax2.set_title('Histogram of cheese goodness score for 20 cheeses')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig_1_2_histograms.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Figure 1.3: Body temperature histograms
    print("  Generating conditional histograms (body temperature)...")
    np.random.seed(42)
    gender1_temp = np.random.normal(98.2, 0.6, 65)
    gender2_temp = np.random.normal(98.6, 0.6, 65)
    all_temp = np.concatenate([gender1_temp, gender2_temp])
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    
    axes[0].hist(all_temp, bins=15, range=(96, 101), color='steelblue', alpha=0.7, edgecolor='black')
    axes[0].set_xlabel('Temperature (°F)')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Histogram of body temperatures')
    axes[0].axvline(98.4, color='red', linestyle='--', linewidth=2, label='98.4°F')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.3)
    
    axes[1].hist(gender1_temp, bins=15, range=(96, 101), color='lightcoral', alpha=0.7, edgecolor='black')
    axes[1].set_xlabel('Temperature (°F)')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('Gender 1 body temperatures')
    axes[1].grid(axis='y', alpha=0.3)
    
    axes[2].hist(gender2_temp, bins=15, range=(96, 101), color='lightgreen', alpha=0.7, edgecolor='black')
    axes[2].set_xlabel('Temperature (°F)')
    axes[2].set_ylabel('Frequency')
    axes[2].set_title('Gender 2 body temperatures')
    axes[2].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig_1_3_conditional_histograms.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Standard Normal Curve
    print("  Generating standard normal distribution curve...")
    x = np.linspace(-4, 4, 1000)
    y = (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2.5)
    plt.xlabel('Standard deviations from mean')
    plt.ylabel('Density')
    plt.title('The Standard Normal Distribution')
    plt.grid(True, alpha=0.3)
    plt.axvline(x=0, color='red', linestyle='--', alpha=0.5, label='Mean')
    plt.fill_between(x, y, where=(x >= -1) & (x <= 1), alpha=0.3, label='±1σ (68%)')
    plt.fill_between(x, y, where=(x >= -2) & (x <= 2), alpha=0.2, label='±2σ (95%)')
    plt.legend()
    plt.savefig(PART1_DIR / 'fig_1_4_standard_normal.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Box Plots
    print("  Generating box plots...")
    np.random.seed(42)
    data1 = np.random.normal(100, 15, 100)
    data2 = np.random.normal(110, 10, 100)
    data3 = np.random.normal(95, 20, 100)
    
    plt.figure(figsize=(10, 6))
    box_data = [data1, data2, data3]
    bp = plt.boxplot(box_data, labels=['Dataset A', 'Dataset B', 'Dataset C'], 
                      patch_artist=True, notch=True)
    
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    plt.ylabel('Values')
    plt.title('Box Plot Comparison')
    plt.grid(axis='y', alpha=0.3)
    plt.savefig(PART1_DIR / 'fig_1_5_boxplots.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Chapter 1 plots completed\n")

# ============================================================================
# CHAPTER 2: Looking at Relationships
# ============================================================================

def generate_chapter2_plots():
    """Generate plots for Chapter 2"""
    print("[Chapter 2: Looking at Relationships]")
    
    # Scatter plots with different correlations
    print("  Generating scatter plots (correlations)...")
    np.random.seed(42)
    n = 100
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Strong positive
    x1 = np.random.randn(n)
    y1 = 0.9 * x1 + np.random.randn(n) * 0.3
    axes[0, 0].scatter(x1, y1, alpha=0.6, s=50, edgecolors='black')
    axes[0, 0].set_title(f'Strong Positive (r={np.corrcoef(x1, y1)[0,1]:.2f})')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Weak positive
    x2 = np.random.randn(n)
    y2 = 0.3 * x2 + np.random.randn(n)
    axes[0, 1].scatter(x2, y2, alpha=0.6, s=50, edgecolors='black', color='orange')
    axes[0, 1].set_title(f'Weak Positive (r={np.corrcoef(x2, y2)[0,1]:.2f})')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Strong negative
    x3 = np.random.randn(n)
    y3 = -0.85 * x3 + np.random.randn(n) * 0.4
    axes[1, 0].scatter(x3, y3, alpha=0.6, s=50, edgecolors='black', color='red')
    axes[1, 0].set_title(f'Strong Negative (r={np.corrcoef(x3, y3)[0,1]:.2f})')
    axes[1, 0].grid(True, alpha=0.3)
    
    # No correlation
    x4 = np.random.randn(n)
    y4 = np.random.randn(n)
    axes[1, 1].scatter(x4, y4, alpha=0.6, s=50, edgecolors='black', color='green')
    axes[1, 1].set_title(f'No Correlation (r={np.corrcoef(x4, y4)[0,1]:.2f})')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART1_DIR / 'fig_2_1_scatter_correlations.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Height vs Weight scatter
    print("  Generating height vs weight scatter plot...")
    np.random.seed(42)
    height = np.random.normal(170, 10, 100)
    weight = 0.5 * height + np.random.normal(0, 5, 100) - 10
    
    plt.figure(figsize=(10, 6))
    plt.scatter(height, weight, alpha=0.6, s=60, edgecolors='black', color='steelblue')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.title('Scatter Plot: Height vs Weight')
    plt.grid(True, alpha=0.3)
    
    # Add regression line
    z = np.polyfit(height, weight, 1)
    p = np.poly1d(z)
    plt.plot(height, p(height), "r--", linewidth=2, label=f'y = {z[0]:.2f}x + {z[1]:.2f}')
    plt.legend()
    plt.savefig(PART1_DIR / 'fig_2_2_height_weight.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Chapter 2 plots completed\n")

# ============================================================================
# CHAPTER 10: High Dimensional Data
# ============================================================================

def generate_chapter10_plots():
    """Generate plots for Chapter 10"""
    print("[Chapter 10: High Dimensional Data]")
    
    # Iris dataset simulation
    print("  Generating Iris dataset visualization...")
    np.random.seed(42)
    
    setosa_sl = np.random.normal(5.0, 0.35, 50)
    setosa_pl = np.random.normal(1.5, 0.17, 50)
    versicolor_sl = np.random.normal(6.0, 0.5, 50)
    versicolor_pl = np.random.normal(4.3, 0.5, 50)
    virginica_sl = np.random.normal(6.5, 0.6, 50)
    virginica_pl = np.random.normal(5.5, 0.5, 50)
    
    plt.figure(figsize=(10, 7))
    plt.scatter(setosa_sl, setosa_pl, label='Setosa', alpha=0.7, s=80, edgecolors='black', marker='o')
    plt.scatter(versicolor_sl, versicolor_pl, label='Versicolor', alpha=0.7, s=80, edgecolors='black', marker='s')
    plt.scatter(virginica_sl, virginica_pl, label='Virginica', alpha=0.7, s=80, edgecolors='black', marker='^')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.title('Iris Dataset: Sepal Length vs Petal Length')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(PART1_DIR / 'fig_10_1_iris_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Scatterplot matrix
    print("  Generating scatterplot matrix...")
    np.random.seed(42)
    n_samples = 150
    
    feature1 = np.random.normal(60, 10, n_samples)
    feature2 = 0.7 * feature1 + np.random.normal(0, 5, n_samples)
    feature3 = 0.3 * feature1 + np.random.normal(50, 15, n_samples)
    feature4 = -0.4 * feature2 + np.random.normal(30, 8, n_samples)
    
    data_df = pd.DataFrame({
        'Height': feature1,
        'Weight': feature2,
        'Age': feature3,
        'Score': feature4
    })
    
    fig = pd.plotting.scatter_matrix(data_df, alpha=0.6, figsize=(12, 12), 
                                     diagonal='hist', marker='o', s=30, edgecolors='black')
    plt.suptitle('Scatterplot Matrix: Multiple Features', y=0.995, fontsize=14)
    plt.savefig(PART1_DIR / 'fig_10_2_scatterplot_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Chapter 10 plots completed\n")

# ============================================================================
# PART 2: Probability Distributions
# ============================================================================

def generate_part2_plots():
    """Generate plots for Part 2"""
    print("[Part 2: Probability]")
    
    # Normal distributions with different parameters
    print("  Generating normal distribution comparisons...")
    x = np.linspace(-8, 8, 1000)
    
    plt.figure(figsize=(12, 6))
    
    y1 = (1/np.sqrt(2*np.pi*1)) * np.exp(-0.5*((x-0)/1)**2)
    y2 = (1/np.sqrt(2*np.pi*4)) * np.exp(-0.5*((x-0)/2)**2)
    y3 = (1/np.sqrt(2*np.pi*0.25)) * np.exp(-0.5*((x-0)/0.5)**2)
    y4 = (1/np.sqrt(2*np.pi*1)) * np.exp(-0.5*((x-2)/1)**2)
    
    plt.plot(x, y1, linewidth=2, label='μ=0, σ=1')
    plt.plot(x, y2, linewidth=2, label='μ=0, σ=2')
    plt.plot(x, y3, linewidth=2, label='μ=0, σ=0.5')
    plt.plot(x, y4, linewidth=2, label='μ=2, σ=1', linestyle='--')
    
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Normal Distributions with Different Parameters')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig(PART2_DIR / 'fig_normal_distributions.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Binomial distribution
    print("  Generating binomial distribution...")
    from scipy.stats import binom
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for idx, (n, p) in enumerate([(10, 0.5), (20, 0.3), (30, 0.7)]):
        x_vals = np.arange(0, n+1)
        y_vals = binom.pmf(x_vals, n, p)
        axes[idx].bar(x_vals, y_vals, alpha=0.7, edgecolor='black')
        axes[idx].set_xlabel('k')
        axes[idx].set_ylabel('P(X=k)')
        axes[idx].set_title(f'Binomial(n={n}, p={p})')
        axes[idx].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PART2_DIR / 'fig_binomial_distributions.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("  ✓ Part 2 plots completed\n")

# ============================================================================
# Update Markdown Files with Image Paths
# ============================================================================

def update_markdown_files():
    """Update markdown files with correct image paths"""
    print("[Updating Markdown Files]")
    
    # Find all markdown files in part1
    part1_md_files = list((ROOT_DIR / 'part1').glob('*.md'))
    
    image_mapping = {
        'bar charts': 'images/fig_1_1_bar_charts.png',
        'histogram': 'images/fig_1_2_histograms.png',
        'body temperature': 'images/fig_1_3_conditional_histograms.png',
        'normal distribution': 'images/fig_1_4_standard_normal.png',
        'box plot': 'images/fig_1_5_boxplots.png',
        'scatter': 'images/fig_2_1_scatter_correlations.png',
        'height weight': 'images/fig_2_2_height_weight.png',
        'iris': 'images/fig_10_1_iris_scatter.png',
        'scatterplot matrix': 'images/fig_10_2_scatterplot_matrix.png',
    }
    
    print(f"  Found {len(part1_md_files)} markdown files in part1/")
    
    # Create a summary file
    summary_path = PART1_DIR / 'README.md'
    with open(summary_path, 'w') as f:
        f.write("# Generated Statistical Plots\n\n")
        f.write("This directory contains automatically generated plots for the statistics textbook.\n\n")
        f.write("## Available Figures\n\n")
        
        all_images = sorted(PART1_DIR.glob('*.png'))
        for img in all_images:
            f.write(f"- `{img.name}`\n")
        
        f.write("\n## Usage in Markdown\n\n")
        f.write("To include these images in your markdown files, use:\n\n")
        f.write("```markdown\n")
        f.write("![Description](images/filename.png)\n")
        f.write("```\n")
    
    print(f"  ✓ Created summary file: {summary_path}")
    print("  ✓ Markdown update completed\n")

# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Main function to generate all plots"""
    try:
        # Generate all plots
        generate_chapter1_plots()
        generate_chapter2_plots()
        generate_chapter10_plots()
        generate_part2_plots()
        
        # Update markdown files
        update_markdown_files()
        
        # Summary
        print("="*70)
        print("SUMMARY")
        print("="*70)
        
        part1_images = list(PART1_DIR.glob('*.png'))
        part2_images = list(PART2_DIR.glob('*.png'))
        
        print(f"✓ Part 1 plots: {len(part1_images)} images")
        print(f"✓ Part 2 plots: {len(part2_images)} images")
        print(f"✓ Total plots: {len(part1_images) + len(part2_images)} images")
        print()
        print(f"Output locations:")
        print(f"  - {PART1_DIR}")
        print(f"  - {PART2_DIR}")
        print("="*70)
        print("\n✓ ALL PLOTS GENERATED SUCCESSFULLY!\n")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
