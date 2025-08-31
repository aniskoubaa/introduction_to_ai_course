# 🗺️ Grid Path Search Lab - Extended Guide
*Comprehensive guide to implementing and understanding search algorithms for 2D grid navigation*

---

## 📚 **Overview**

This lab provides hands-on experience with four fundamental search algorithms applied to pathfinding in 2D grids. You'll explore the trade-offs between optimality, efficiency, and memory usage while solving maze navigation problems.

### **Learning Objectives**
- Understand the differences between uninformed and informed search
- Implement BFS, DFS, UCS, and A* algorithms
- Compare algorithm performance on various grid configurations
- Analyze the impact of heuristics on search efficiency
- Gain practical experience with data structures (queues, stacks, priority queues)

---

## 🗂️ **File Structure & Relationship**

### **Main Files**
- **`grid_search_lab.ipynb`** - Interactive Jupyter notebook with complete implementations
- **`grid_search.py`** - Standalone Python file with TODO sections for learning
- **`README.md`** - Quick start guide for students
- **`README_EXTENDED.md`** - This comprehensive guide
- **`questions.md`** - Practice problems and theoretical exercises

### **File Relationships**

#### **📓 Notebook vs 📄 Python File**

| Aspect | `grid_search_lab.ipynb` | `grid_search.py` |
|--------|-------------------------|------------------|
| **Purpose** | Interactive demo & instructor tool | Student coding exercise |
| **Implementation** | Complete, ready-to-run | Has TODO sections to complete |
| **Best for** | Understanding algorithms, demos | Learning by implementing |
| **Output** | Visual, step-by-step results | Command-line testing |
| **Structure** | Cells with explanations | Monolithic class structure |

**When to use each:**
- **Notebook**: For quick experimentation, visualization, and understanding how algorithms work
- **Python file**: For in-depth learning through implementation, suitable for assignments

---

## 🎯 **Problem Definition**

### **Grid Representation**
```python
# 0 = passable cell (cost = 1)
# 1 = obstacle (impassable)
grid = [
    [0, 0, 0, 0, 0],  # S . . . G
    [1, 1, 0, 1, 0],  # █ █ . █ .
    [1, 0, 0, 0, 0],  # █ . . . .
    [1, 0, 1, 1, 0],  # █ . █ █ .
    [0, 0, 0, 0, 0]   # . . . . .
]
```

### **State Space**
- **State**: Position (row, col) in the grid
- **Initial State**: Start position, e.g., (0, 0)
- **Goal State**: Target position, e.g., (0, 4)
- **Actions**: Move up, down, left, right (4-connected)
- **Path Cost**: Number of steps (each step costs 1)

---

## 🔍 **Algorithm Details**

### **1. Breadth-First Search (BFS)**
```python
def bfs(self, start, goal):
    queue = deque([start])      # FIFO queue
    visited = {start}           # Avoid revisiting states
    parent = {start: None}      # For path reconstruction
    
    while queue:
        current = queue.popleft()  # Explore oldest node first
        
        if current == goal:
            return self.reconstruct_path(parent, start, goal)
        
        for neighbor in self.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return None  # No path found
```

**Key Properties:**
- **Completeness**: Always finds solution if one exists
- **Optimality**: Guarantees shortest path (minimum steps)
- **Time Complexity**: O(b^d) where b=branching factor, d=depth
- **Space Complexity**: O(b^d) - stores all nodes at current level
- **Best for**: Finding shortest path in unweighted graphs

### **2. Depth-First Search (DFS)**
```python
def dfs(self, start, goal, max_depth=50):
    stack = [(start, 0)]        # LIFO stack with depth tracking
    visited = {start}           # Avoid cycles
    parent = {start: None}      # For path reconstruction
    
    while stack:
        current, depth = stack.pop()  # Explore newest node first
        
        if current == goal:
            return self.reconstruct_path(parent, start, goal)
        
        if depth < max_depth:  # Prevent infinite search
            for neighbor in reversed(self.get_neighbors(current)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append((neighbor, depth + 1))
    
    return None  # No path found or depth limit reached
```

**Key Properties:**
- **Completeness**: Complete with depth limit, incomplete without
- **Optimality**: Does NOT guarantee shortest path
- **Time Complexity**: O(b^m) where m=maximum depth
- **Space Complexity**: O(bm) - only stores current path
- **Best for**: Memory-constrained environments, when any solution suffices

### **3. Uniform-Cost Search (UCS)**
```python
def ucs(self, start, goal):
    pq = [(0, start)]           # Priority queue: (cost, position)
    costs = {start: 0}          # Best known cost to each state
    parent = {start: None}      # For path reconstruction
    visited = set()             # Processed states
    
    while pq:
        current_cost, current = heapq.heappop(pq)
        
        if current in visited:
            continue  # Skip if already processed optimally
        
        visited.add(current)
        
        if current == goal:
            return self.reconstruct_path(parent, start, goal)
        
        for neighbor in self.get_neighbors(current):
            new_cost = current_cost + 1  # Each step costs 1
            
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))
    
    return None  # No path found
```

**Key Properties:**
- **Completeness**: Always finds solution if one exists
- **Optimality**: Guarantees lowest-cost path
- **Time/Space Complexity**: O(b^(C*/ε)) where C*=optimal cost, ε=minimum cost
- **Best for**: Weighted graphs where step costs vary

### **4. A* Search**
```python
def astar(self, start, goal):
    h_start = self.manhattan_distance(start, goal)
    pq = [(h_start, 0, start)]  # Priority queue: (f_cost, g_cost, position)
    g_costs = {start: 0}        # Actual cost from start
    parent = {start: None}      # For path reconstruction
    visited = set()             # Processed states
    
    while pq:
        f_cost, g_cost, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == goal:
            return self.reconstruct_path(parent, start, goal)
        
        for neighbor in self.get_neighbors(current):
            tentative_g = g_cost + 1
            
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                parent[neighbor] = current
                h_cost = self.manhattan_distance(neighbor, goal)
                f_cost = tentative_g + h_cost
                heapq.heappush(pq, (f_cost, tentative_g, neighbor))
    
    return None  # No path found
```

**Key Properties:**
- **Evaluation Function**: f(n) = g(n) + h(n)
  - g(n) = actual cost from start to n
  - h(n) = heuristic cost from n to goal
- **Heuristic**: Manhattan distance |x₁-x₂| + |y₁-y₂|
- **Admissibility**: Heuristic never overestimates actual cost
- **Optimality**: Guaranteed if heuristic is admissible
- **Efficiency**: Often explores far fewer nodes than BFS/UCS
- **Best for**: Optimal pathfinding with guidance toward goal

---

## 🧪 **Test Cases & Expected Results**

### **Test Case 1: Simple 3×3 Grid**
```python
simple_grid = [
    [0, 0, 0],    # S . G
    [0, 0, 0],    # . . .
    [0, 0, 0]     # . . .
]
start = (0, 0)
goal = (2, 2)
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Optimal Path |
|-----------|-------------|----------------|--------------|
| BFS       | 4           | ~8-10          | ✅ Yes       |
| DFS       | 4-8         | ~6-12          | ❌ Maybe     |
| UCS       | 4           | ~8-10          | ✅ Yes       |
| A*        | 4           | ~5-7           | ✅ Yes       |

**Optimal Path**: `[(0,0), (0,1), (1,1), (2,1), (2,2)]` or similar 4-step path

### **Test Case 2: 5×5 Maze**
```python
maze_grid = [
    [0, 0, 0, 0, 0],    # S . . . G
    [1, 1, 0, 1, 0],    # █ █ . █ .
    [1, 0, 0, 0, 0],    # █ . . . .
    [1, 0, 1, 1, 0],    # █ . █ █ .
    [0, 0, 0, 0, 0]     # . . . . .
]
start = (0, 0)
goal = (0, 4)
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Time (ms) |
|-----------|-------------|----------------|-----------|
| BFS       | 4           | ~15-20         | ~1-2      |
| DFS       | 4-12        | ~10-25         | ~1-2      |
| UCS       | 4           | ~15-20         | ~1-2      |
| A*        | 4           | ~8-12          | ~1-2      |

**Optimal Path**: `[(0,0), (0,1), (0,2), (0,3), (0,4)]`

### **Test Case 3: Complex Maze with Multiple Paths**
```python
complex_grid = [
    [0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0]
]
start = (0, 0)
goal = (6, 6)
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Performance |
|-----------|-------------|----------------|-------------|
| BFS       | 12          | ~40-50         | Slow but optimal |
| DFS       | 12-30       | ~20-60         | Fast but suboptimal |
| UCS       | 12          | ~40-50         | Slow but optimal |
| A*        | 12          | ~20-30         | Fast and optimal |

---

## 📊 **Performance Analysis**

### **Algorithm Comparison Matrix**

| Criteria | BFS | DFS | UCS | A* |
|----------|-----|-----|-----|-----|
| **Completeness** | ✅ Yes | ❌ No* | ✅ Yes | ✅ Yes |
| **Optimality** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes** |
| **Time Complexity** | O(b^d) | O(b^m) | O(b^C*) | O(b^d) |
| **Space Complexity** | O(b^d) | O(bm) | O(b^C*) | O(b^d) |
| **Memory Usage** | High | Low | High | High |
| **Speed on Grids** | Medium | Fast | Medium | Very Fast |

*With depth limit  
**If heuristic is admissible

### **When to Use Each Algorithm**

1. **BFS**: When you need the shortest path and can afford memory usage
2. **DFS**: When memory is limited and any solution is acceptable
3. **UCS**: When step costs vary and you need optimal cost
4. **A***: When you need optimal paths efficiently and have a good heuristic

---

## 🧠 **Key Concepts**

### **Heuristic Functions**
A heuristic function h(n) estimates the cost from node n to the goal.

**Manhattan Distance for Grids:**
```python
def manhattan_distance(self, pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
```

**Properties:**
- **Admissible**: Never overestimates true cost (required for A* optimality)
- **Consistent**: h(n) ≤ cost(n,n') + h(n') for every neighbor n'
- **Informative**: Closer estimates lead to better performance

### **Search Tree vs State Graph**
- **Search Tree**: Shows the exploration process, can have duplicate states
- **State Graph**: Shows unique states and their connections
- **Visited Set**: Prevents exploring same state multiple times

### **Path Reconstruction**
```python
def reconstruct_path(self, parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    return path
```

---

## 🎓 **Educational Exercises**

### **Hands-on Activities**
1. **Manual Tracing**: Trace BFS and A* by hand on a small grid
2. **Algorithm Modification**: Implement diagonal movement (8-connected grid)
3. **Heuristic Design**: Create and test different heuristic functions
4. **Performance Testing**: Run algorithms on increasingly complex mazes

### **Analysis Questions**
1. Why does A* typically explore fewer nodes than BFS?
2. When might DFS find a better path than expected?
3. How does the heuristic quality affect A* performance?
4. What happens if the heuristic overestimates (non-admissible)?

### **Implementation Challenges**
1. Add diagonal movement with cost √2
2. Implement iterative deepening search (IDAS)
3. Create animated path visualization
4. Handle grids with variable terrain costs

---

## 🚀 **Getting Started**

### **Option 1: Interactive Learning (Recommended)**
1. Open `grid_search_lab.ipynb` in Jupyter or Google Colab
2. Run each cell and observe the algorithm behavior
3. Modify test cases and see how performance changes
4. Experiment with different grid configurations

### **Option 2: Implementation Practice**
1. Open `grid_search.py` in your preferred IDE
2. Complete the TODO sections for each algorithm
3. Run the file to test your implementations
4. Compare your results with the notebook solutions

### **Option 3: Theoretical Study**
1. Read this extended guide thoroughly
2. Work through the manual tracing exercises
3. Answer the analysis questions
4. Study the performance comparison charts

---

## 🔗 **Additional Resources**

- **Textbook**: "Artificial Intelligence: A Modern Approach" by Russell & Norvig
- **Online Visualizer**: [PathFinding.js](https://qiao.github.io/PathFinding.js/visual/)
- **Algorithm Animations**: [VisuAlgo Graph Traversal](https://visualgo.net/en/dfsbfs)
- **Academic Papers**: A* algorithm original paper by Hart, Nilsson & Raphael (1968)

---

*This comprehensive guide provides both theoretical understanding and practical implementation details for search algorithms in grid pathfinding. Use it as a reference while working through the exercises and experiments.*
