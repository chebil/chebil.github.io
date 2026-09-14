# Artificial Intelligence: A Textbook - Interactive Jupyter Book

[![Jupyter Book](https://img.shields.io/badge/Jupyter-Book-orange)](https://jupyterbook.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green)](LICENSE)
[![Labs Complete](https://img.shields.io/badge/Labs-13%2F13%20Complete-brightgreen)](ENHANCEMENT_SUMMARY.md)

A comprehensive, hands-on interactive textbook for Artificial Intelligence with theory, implementation, and **complete lab exercises** for all 13 chapters.

**Instructor**: Dr. Khalil Chebil  
**Institution**: Prince Sattam bin Abdulaziz University (PSAU)  
**Course Repository**: [AI-course-book](https://github.com/chebil/AI-course-book)  
**Lecture Slides**: [AI-slides](https://github.com/chebil/AI-slides)

---

## ✨ What's New - December 2025

### ✅ Phase 2 COMPLETED!

**All 13 Lab Notebooks Now Available!**
- ✅ **13/13 chapters** have comprehensive lab exercises
- ✅ **130+ hands-on exercises** across all topics
- ✅ **Progressive difficulty** from beginner to advanced
- ✅ **Complete coverage**: Deductive AI → ML → Integration

### 🎓 Lab Notebook Features

Each lab includes:
- 📋 Clear learning objectives
- 💻 5-6 progressive exercises
- 🔧 Skeleton code with TODO markers
- ✅ Test cases for validation
- 📊 Performance benchmarking tools
- 🎨 Visualization templates
- 🏆 Challenge problems for advanced students
- 💬 Discussion questions
- 📝 Deliverables checklist

---

## 📚 Complete Book Structure

### Part I: Deductive Reasoning (Chapters 1-5)

| Chapter | Theory | Implementation | Lab | Key Topics |
|---------|--------|----------------|-----|------------|
| 1 | ✅ | ✅ | ✅ | **Agent Architectures** |
| 2 | ✅ | ✅ | ✅ | **Search Algorithms** |
| 3 | ✅ | ✅ | ✅ | **Game Playing, Minimax** |
| 4 | ✅ | ✅ | ✅ | **Propositional Logic, SAT** |
| 5 | ✅ | ✅ | ✅ | **FOL, Unification, Prolog** |

**Lab 1**: Simple/Model/Goal/Utility Agents, Learning Agent  
**Lab 2**: BFS, DFS, A*, 8-Puzzle, N-Queens, CSP  
**Lab 3**: Minimax, Alpha-Beta, MCTS, Tournament  
**Lab 4**: Truth Tables, CNF, Resolution, Wumpus World  
**Lab 5**: Unification, Forward/Backward Chaining, Prolog

### Part II: Inductive Learning (Chapters 6-10)

| Chapter | Theory | Implementation | Lab | Key Topics |
|---------|--------|----------------|-----|------------|
| 6 | ✅ | ✅ | ✅ | **Linear/Logistic Regression, Decision Trees** |
| 7 | ✅ | ✅ | ✅ | **Neural Networks, Backpropagation** |
| 8 | ✅ | ✅ | ✅ | **CNNs, RNNs, Transformers** |
| 9 | ✅ | ✅ | ✅ | **Clustering, PCA, Autoencoders** |
| 10 | ✅ | ✅ | ✅ | **Q-Learning, DQN, Policy Gradients** |

**Lab 6**: Gradient Descent, Cross-Validation, Real Datasets  
**Lab 7**: Neural Net from Scratch, PyTorch, MNIST  
**Lab 8**: CNN (CIFAR-10), RNN, LSTM, Attention  
**Lab 9**: K-Means, Hierarchical, DBSCAN, VAE  
**Lab 10**: Tabular Q-Learning, DQN, REINFORCE, CartPole

### Part III: Integration (Chapters 11-13)

| Chapter | Theory | Implementation | Lab | Key Topics |
|---------|--------|----------------|-----|------------|
| 11 | ✅ | ✅ | ✅ | **Bayesian Networks, HMMs** |
| 12 | ✅ | ✅ | ✅ | **Knowledge Graphs, TransE** |
| 13 | ✅ | ✅ | ✅ | **Neuro-Symbolic AI, XAI** |

**Lab 11**: Bayesian Networks, Variable Elimination, Gibbs Sampling  
**Lab 12**: KG Construction, Embeddings, Link Prediction  
**Lab 13**: Hybrid AI, Differentiable Logic, Explainable AI

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/chebil/AI-course-book.git
cd AI-course-book

# Install dependencies
pip install -r requirements.txt

# Build the book
jupyter-book build .
```

### Using the Labs

```bash
# Open any lab in Jupyter
jupyter notebook chapters/ch01_introduction_lab.ipynb

# Or use JupyterLab
jupyterlab chapters/
```

### Online Access

1. **GitHub Pages**: Visit the deployed book
2. **Binder**: Click 🚀 rocket icon → "Binder" for live execution
3. **Google Colab**: Click 🚀 rocket icon → "Colab"
4. **Local**: Download and run in your environment

---

## 📖 How to Use This Book

### For Students

**Learning Path (per chapter):**
1. 📚 **Read Theory** notebook for concepts and algorithms
2. 💻 **Study Implementation** notebook for code examples
3. ✍️ **Complete Lab** exercises
   - Start with easy exercises
   - Progress to intermediate
   - Challenge yourself with advanced problems
4. ✅ **Validate** your solutions with test cases
5. 📊 **Compare** your results with benchmarks
6. 💭 **Reflect** on discussion questions

**Estimated Time per Chapter**: 4-6 hours (theory + implementation + lab)

### For Instructors

**Course Structure:**
- **Lectures**: Use theory notebooks + [AI-slides](https://github.com/chebil/AI-slides)
- **Tutorials**: Walk through implementation notebooks
- **Homework**: Assign lab exercises (individual or groups)
- **Projects**: Combine multiple chapters
- **Assessment**: Lab deliverables + final project

**Customization:**
- All materials are open-source
- Fork and modify for your needs
- Add your own exercises
- Integrate with your LMS

---

## 💡 Example Lab Exercise

### From Chapter 2 Lab: Implementing A* Search

```python
def a_star_search(graph, start, goal, heuristic):
    """
    TODO: Implement A* Search
    
    Algorithm:
    1. Initialize priority queue with start node
    2. While queue not empty:
       a. Pop node with lowest f(n) = g(n) + h(n)
       b. If goal reached, return path
       c. Expand neighbors and add to queue
    
    Return: (path, cost, nodes_expanded)
    """
    # YOUR CODE HERE
    pass

# Test on Romania map
path, cost, nodes = a_star_search(
    romania_map, 'Arad', 'Bucharest', h_bucharest
)
print(f"Path: {path}")
print(f"Cost: {cost}")
print(f"Nodes expanded: {nodes}")

# Expected output:
# Path: ['Arad', 'Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']
# Cost: 418
# Nodes expanded: 5
```

---

## 📊 Lab Statistics

### Coverage
- **Total Lab Notebooks**: 13
- **Total Exercises**: 130+
- **Programming Problems**: 65+
- **Challenge Problems**: 13
- **Discussion Questions**: 52+

### Topics Covered

**Algorithms Implemented:**
- Search: BFS, DFS, A*, CSP, Hill Climbing
- Game Playing: Minimax, Alpha-Beta, MCTS
- Logic: Resolution, Unification, Forward/Backward Chaining
- ML: Linear/Logistic Regression, Decision Trees, Neural Networks
- Deep Learning: CNN, RNN, LSTM, Transformers
- Unsupervised: K-Means, PCA, Autoencoders
- RL: Q-Learning, DQN, Policy Gradients
- Advanced: Bayesian Networks, Knowledge Graphs, Hybrid AI

---

## 🎯 Learning Outcomes

After completing this course, students will be able to:

1. **Implement** core AI algorithms from scratch
2. **Apply** AI techniques to real-world problems
3. **Compare** different approaches and analyze trade-offs
4. **Design** complete AI systems
5. **Evaluate** performance using appropriate metrics
6. **Explain** how algorithms work and when to use them
7. **Build** neural networks with modern frameworks
8. **Create** hybrid systems combining multiple AI paradigms

---

## 🛠️ Technology Stack

### Core
- **Jupyter Book**: Interactive book framework
- **MyST Markdown**: Enhanced markdown with directives
- **Python 3.9+**: Programming language

### Libraries Used in Labs
- **NumPy**: Numerical computing
- **Matplotlib**: Visualizations
- **Pandas**: Data analysis
- **Scikit-learn**: ML algorithms
- **PyTorch**: Deep learning
- **NetworkX**: Graph algorithms
- **RDFLib**: Knowledge graphs

### Optional Enhancements
```bash
# Install additional packages for advanced labs
pip install transformers langchain gymnasium rdflib
```

---

## 📚 Reference Textbooks

**Primary**:  
Aggarwal, C. C. (2021). *Artificial Intelligence: A Textbook*. Springer.  
ISBN: 978-3-030-72357-6

**Complementary**:
- Russell & Norvig. *AI: A Modern Approach* (4th ed.)
- Goodfellow et al. *Deep Learning* (MIT Press)
- Sutton & Barto. *Reinforcement Learning* (2nd ed.)

**Resources**:
- Course slides: [AI-slides](https://github.com/chebil/AI-slides)
- Enhancement details: [ENHANCEMENT_SUMMARY.md](ENHANCEMENT_SUMMARY.md)

---

## 🤝 Contributing

We welcome contributions!

**How to contribute:**
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

**Areas for contribution:**
- Additional exercises
- Solution examples
- Improved explanations
- Bug fixes
- New visualizations
- Translations

**Guidelines:**
- Follow existing notebook structure
- Include docstrings and comments
- Add test cases
- Update documentation

---

## 📜 License

This educational material is provided for academic purposes. Please respect the copyright of:
- Original textbook by Charu C. Aggarwal
- Course materials by Dr. Khalil Chebil
- Open-source libraries used

---

## 📧 Contact

**Instructor**: Dr. Khalil Chebil  
**Institution**: Prince Sattam bin Abdulaziz University (PSAU)  
**Email**: khalil.chebil@insat.ucar.tn  
**GitHub**: [@chebil](https://github.com/chebil)

**Questions?**
- Open an [issue](https://github.com/chebil/AI-course-book/issues)
- Start a [discussion](https://github.com/chebil/AI-course-book/discussions)
- Email the instructor

---

## 📈 Project Status

### ✅ Completed (December 2025)

**Phase 1:**
- [x] Repository setup and configuration
- [x] Jupyter Book infrastructure
- [x] 13-chapter structure
- [x] Chapter 2 complete implementation
- [x] Repository cleanup (duplicates removed)

**Phase 2:**
- [x] **All 13 lab notebooks created** ✨
- [x] **130+ exercises implemented**
- [x] Table of contents updated
- [x] Documentation completed
- [x] README finalized

### 🎯 Future Enhancements (Optional)

- [ ] Video tutorials for key concepts
- [ ] Auto-graded assignments (nbgrader)
- [ ] Interactive visualizations (Plotly)
- [ ] Streamlit apps for demonstrations
- [ ] Multilingual support
- [ ] Additional real-world case studies

---

## 🌟 Acknowledgments

**Based on:**
- *Artificial Intelligence: A Textbook* by Charu C. Aggarwal
- Course materials developed at PSAU
- Contributions from students and TAs
- Open-source AI community

**Tools:**
- Jupyter Book framework
- PyTorch and Scikit-learn communities
- GitHub for version control and hosting

---

**Ready to learn AI? Start with [Chapter 1](chapters/ch01_introduction.ipynb)!** 🤖📚  
**Want hands-on practice? Jump to [Chapter 1 Lab](chapters/ch01_introduction_lab.ipynb)!** ✍️💻

---

*Last updated: December 14, 2025*  
*Version: 2.0 - Complete Lab Integration*