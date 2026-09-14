# Images Directory

This directory contains all figures and images used in the Probability and Statistics textbook.

## Structure

```
images/
├── part1/          # Figures for Part I (Describing Datasets)
│   ├── fig-bar-charts.png
│   ├── fig-histograms.png
│   ├── fig-conditional-histograms.png
│   ├── fig-boxplots.png
│   └── fig-scatter-correlation.png
│
└── part2/          # Figures for Part II (Probability)
    ├── fig-probability-tree.png
    └── fig-normal-distribution.png
```

## Generating Figures

To regenerate all figures:

```bash
cd scripts
python generate_figures.py
```

Requirements:
- Python 3.7+
- matplotlib
- numpy
- pandas
- seaborn

## Image Guidelines

- **Format**: PNG with 300 DPI
- **Size**: Typically 800-1200px wide
- **Colors**: Use consistent color palette
- **Labels**: Clear axis labels and titles
- **Style**: Clean, academic style with grid

## Adding New Images

1. Generate the image using Python or other tools
2. Save to appropriate subdirectory (part1/, part2/, etc.)
3. Use descriptive filenames (e.g., `fig-chapter-topic.png`)
4. Reference in markdown with relative path:
   ```markdown
   ```{figure} ../images/part1/fig-name.png
   :name: fig-name
   :width: 80%
   
   Caption describing the figure
   ```
   ```

## Image Sources

- **Generated**: Python scripts using matplotlib/seaborn
- **Data sources**: Cited in respective chapters
- **License**: Educational use under textbook license
