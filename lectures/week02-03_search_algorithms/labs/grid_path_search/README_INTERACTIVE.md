# 📓 Interactive Lab Sessions
**SE 444: Introduction to AI - Prof. Anis Koubaa**

## 🎯 Quick Start Guide

### **For Students:**
1. **Local Jupyter**: Open `*_interactive.py` files in Jupyter notebook
2. **Google Colab**: Upload and run the interactive Python files
3. **Command Line**: Run `python grid_search_interactive.py` for demo

### **For Instructors:**
- Use interactive files for live demonstrations
- Students can follow along in real-time
- Perfect for step-by-step algorithm walkthroughs

---

## 📁 Interactive Files

### **Grid Path Search** 🗺️
- **File**: `grid_search_interactive.py`
- **Features**: 
  - ✅ BFS, DFS, UCS, A* implementations
  - ✅ Visual grid display with path
  - ✅ Performance comparison table
  - ✅ Works in Jupyter & Colab

### **8-Puzzle Search** 🧩
- **File**: `puzzle_search_interactive.py` 
- **Features**:
  - ✅ BFS, DFS, A* (Manhattan), A* (Misplaced)
  - ✅ Pretty puzzle state display
  - ✅ Solution step visualization
  - ✅ Multiple difficulty levels

---

## 🚀 How to Use in Jupyter

### **Option 1: Copy-Paste Method**
```python
# Copy sections from interactive.py files into Jupyter cells
# Each algorithm can be in its own cell for step-by-step execution
```

### **Option 2: Run as Script**
```python
# In Jupyter cell:
exec(open('grid_search_interactive.py').read())
```

### **Option 3: Google Colab**
1. Upload the `.py` file to Colab
2. Run it as a script or copy sections to cells
3. Modify parameters for different experiments

---

## 🎓 Instructor Demo Tips

### **Live Demonstration Flow:**

#### **1. Setup (2 minutes)**
- Show environment setup
- Explain grid/puzzle representation
- Preview what algorithms we'll compare

#### **2. Algorithm Walkthrough (15 minutes)**
- **BFS**: "Level by level exploration"
- **DFS**: "Go deep, then backtrack"
- **UCS**: "Lowest cost first"
- **A***: "Smart guidance with heuristics"

#### **3. Interactive Comparison (10 minutes)**
- Run algorithms on same problem
- Compare results in real-time
- Discuss why A* is more efficient

#### **4. Student Experiment (8 minutes)**
- Let students create custom grids
- Test their predictions
- Discuss surprising results

### **Key Teaching Points:**
✅ **Visual Learning**: Students see paths being found  
✅ **Performance Analysis**: Compare nodes explored  
✅ **Heuristic Impact**: A* vs UCS dramatic difference  
✅ **Real Applications**: GPS navigation, game AI  

---

## 🔧 Customization Ideas

### **For Advanced Students:**
```python
# Add custom heuristics
def custom_heuristic(pos1, pos2):
    # Your heuristic here
    return your_calculation

# Modify algorithms
def weighted_astar(self, start, goal, weight=1.5):
    # f(n) = g(n) + weight * h(n)
    # Trade optimality for speed
```

### **For Different Problems:**
- **Larger grids**: 10x10, 20x20
- **Different obstacles**: Maze patterns  
- **Weighted edges**: Different movement costs
- **Multiple goals**: Visit all targets

---

## 📊 Expected Student Outcomes

After interactive session, students should understand:

1. **Algorithm Differences**: When to use each algorithm
2. **Heuristic Power**: Why A* outperforms others
3. **Trade-offs**: Optimality vs. efficiency vs. memory
4. **Real Applications**: How these apply to real problems

---

## ⚡ Quick Demo Commands

### **Grid Search:**
```python
# Quick test
python grid_search_interactive.py

# In Jupyter:
from grid_search_interactive import GridSearcher, run_demo
run_demo()
```

### **8-Puzzle:**
```python
# Quick test  
python puzzle_search_interactive.py

# Custom puzzle:
searcher = PuzzleSearcher()
path, stats = searcher.astar_manhattan((8, 1, 2, 0, 4, 3, 7, 6, 5))
searcher.show_solution_steps(path)
```

---

## 🎯 Assessment Integration

### **Lab Report Questions:**
1. **Which algorithm explored fewest nodes? Why?**
2. **Create a grid where DFS fails but A* succeeds**
3. **Compare Manhattan vs Misplaced tiles heuristics**
4. **Explain when you'd use each algorithm in practice**

### **Interactive Exercises:**
- Design custom test cases
- Predict algorithm performance
- Analyze unexpected results
- Propose improvements

---

*These interactive files make complex algorithms accessible and engaging. Students learn by doing, not just reading!* 🚀
