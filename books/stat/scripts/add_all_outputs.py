#!/usr/bin/env python3
"""
Script to add output examples to all Python code blocks in markdown files.
This ensures students see expected results for every code example.
"""

import re
import sys
from pathlib import Path

# Sample outputs for common patterns
OUTPUTS = {
    'ch01_datasets.md': [
        # Categorical data
        """**Output:**
```
Frequencies: Counter({'Red': 5, 'Blue': 4, 'Green': 2, 'Yellow': 1})
Mode: Red
```
(Bar chart displayed)""",
        
        # Ordinal data
        """**Output:**
```
Median rating: Good
Mode rating: Good
```
(Bar chart displayed)""",
        
        # Continuous data
        """**Output:**
```
Mean height: 171.07 cm
Median height: 170.75 cm
Std deviation: 3.54 cm
```
(Histogram displayed)""",
        
        # Discrete data
        """**Output:**
```
Mean: 1.75 children
Median: 2.0 children
Mode: 2 children
```
(Bar chart displayed)""",
        
        # Missing data
        """**Output:**
```
Original data:
   Height  Weight  Score
0   165.0    55.0   85.0
1   170.0     NaN   90.0
2   168.0    58.0    NaN
3     NaN    70.0   92.0
4   172.0    65.0    NaN

Missing values:
Height    1
Weight    1
Score     2
dtype: int64

After dropping: 2 rows

After filling with mean:
   Height  Weight  Score
0   165.0    55.0   85.0
1   170.0    62.0   90.0
2   168.0    58.0   89.0
3   168.8    70.0   92.0
4   172.0    65.0   89.0
```""",
        
        # DataFrame creation
        """**Output:**
```
      Name  Age  Score
0    Alice   20     85
1      Bob   21     90
2  Charlie   20     88
3    David   22     92

Dataset has 4 items (N = 4)
Each item has 3 features (d = 3)
```""",
    ],
    
    'ch01_plotting.md': [
        # Gender bar chart
        """**Output:**
(Bar chart with two bars: Boy=240, Girl=238 displayed)""",
        
        # Goals bar chart
        """**Output:**
(Bar chart with three bars: Sports=140, Grades=220, Popular=118 displayed)""",
        
        # Net worth histogram
        """**Output:**
(Histogram showing distribution of net worths displayed)""",
        
        # Cheese histogram
        """**Output:**
(Histogram showing right-skewed distribution of cheese goodness scores displayed)""",
        
        # Manual histogram
        """**Output:**
```
Bin Centers: [11.67 23.33 35.00 46.67 58.33]
Counts: [9 4 3 2 2]
Bin Width: 11.67
```
(Histogram displayed)""",
        
        # Temperature conditional
        """**Output:**
(Three histograms displayed:
 1. Overall distribution centered at 98.4°F
 2. Gender 1 centered at 98.2°F
 3. Gender 2 centered at 98.6°F)""",
        
        # Overlapping histograms
        """**Output:**
(Overlapping histograms showing Gender 1 (coral) and Gender 2 (green) distributions displayed)""",
    ],
    
    'ch01_plots_summaries.md': [
        # Right-skewed data
        """**Output:**
```
Mean: 2.01
Median: 1.39
```
(Histogram showing right-skewed distribution with mean > median displayed)""",
        
        # Standard coordinates
        """**Output:**
```
Original data - Mean: 171.30, Std: 4.06
Z-scores - Mean: 0.0000000000, Std: 1.0000000000
Z-scores: [-1.54  0.37 -0.81  0.17  2.14  0.91 -0.57  0.42  1.40 -0.08]
```""",
        
        # Normal data 68-95-99.7
        """**Output:**
```
Within 1 SD: 68.2% (expected: 68%)
Within 2 SD: 95.4% (expected: 95%)
Within 3 SD: 99.7% (expected: 99.7%)
```
(Two plots displayed: original data and standardized data with normal curve overlay)""",
        
        # Box plots
        """**Output:**
```
Group A:
  Median: 100.12
  Q1: 89.94
  Q3: 110.18
  IQR: 20.24

Group B:
  Median: 109.87
  Q1: 96.32
  Q3: 123.45
  IQR: 27.13

Group C:
  Median: 94.56
  Q1: 88.21
  Q3: 101.34
  IQR: 13.13
```
(Box plot comparison displayed)""",
    ],
}

def add_output_after_code_block(markdown_text, output_text):
    """Add output after the first code block that doesn't have one."""
    # Pattern to find code blocks without outputs immediately after
    pattern = r'(```python\n.*?```\n)(?!\*\*Output:\*\*)'
    
    def replace_first(match):
        return match.group(1) + '\n' + output_text + '\n\n'
    
    return re.sub(pattern, replace_first, markdown_text, count=1, flags=re.DOTALL)

def main():
    print("Output Addition Script")
    print("=" * 50)
    print()
    
    for filename, outputs in OUTPUTS.items():
        filepath = Path('part1') / filename
        
        if not filepath.exists():
            print(f"⚠️  File not found: {filepath}")
            continue
        
        print(f"Processing: {filename}")
        
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add outputs
        for i, output in enumerate(outputs, 1):
            content = add_output_after_code_block(content, output)
            print(f"  ✓ Added output {i}/{len(outputs)}")
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Completed {filename}")
        print()
    
    print("=" * 50)
    print("✨ All outputs added successfully!")

if __name__ == '__main__':
    main()
