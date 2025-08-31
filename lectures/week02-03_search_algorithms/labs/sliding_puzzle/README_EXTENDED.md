# 🧩 8-Puzzle Search Lab - Extended Guide
*Comprehensive guide to solving state space problems using heuristic search algorithms*

---

## 📚 **Overview**

The 8-puzzle is a classic problem in artificial intelligence that demonstrates the power of heuristic search. This lab explores how different search algorithms and heuristic functions can dramatically affect problem-solving efficiency in complex state spaces.

### **Learning Objectives**
- Understand state space representation for combinatorial problems
- Implement and compare BFS and A* with different heuristics
- Analyze the impact of heuristic quality on search performance
- Gain experience with admissible heuristic design
- Explore the exponential nature of uninformed search

---

## 🗂️ **File Structure & Relationship**

### **Main Files**
- **`puzzle_search_lab.ipynb`** - Interactive Jupyter notebook with complete implementations
- **`puzzle_search.py`** - Standalone Python file with TODO sections for learning
- **`README.md`** - Quick start guide for students
- **`README_EXTENDED.md`** - This comprehensive guide
- **`questions.md`** - Practice problems and theoretical exercises

### **File Relationships**

#### **📓 Notebook vs 📄 Python File**

| Aspect | `puzzle_search_lab.ipynb` | `puzzle_search.py` |
|--------|-------------------------|------------------|
| **Purpose** | Interactive demo & instructor tool | Student coding exercise |
| **Implementation** | Complete, ready-to-run | Has TODO sections to complete |
| **Best for** | Understanding algorithms, visualizations | Learning through implementation |
| **Algorithms** | BFS, A* (Manhattan), A* (Misplaced) | BFS, DFS, A* (both heuristics) |
| **Output** | Beautiful puzzle display, step-by-step | Command-line text output |
| **Structure** | Cells with explanations | Class-based structure |

**When to use each:**
- **Notebook**: For quick experimentation, algorithm comparison, and visual learning
- **Python file**: For detailed implementation practice and understanding algorithm mechanics

---

## 🎯 **Problem Definition**

### **The 8-Puzzle**
The 8-puzzle consists of a 3×3 grid with 8 numbered tiles and one empty space. The goal is to rearrange tiles by sliding them into the empty space to reach a target configuration.

```
Initial State:        Goal State:
┌───┬───┬───┐        ┌───┬───┬───┐
│ 1 │ 2 │ 3 │        │ 1 │ 2 │ 3 │
├───┼───┼───┤        ├───┼───┼───┤
│ 4 │   │ 6 │   →    │ 4 │ 5 │ 6 │
├───┼───┼───┤        ├───┼───┼───┤
│ 7 │ 5 │ 8 │        │ 7 │ 8 │   │
└───┴───┴───┘        └───┴───┴───┘
```

### **State Space Characteristics**
- **State Representation**: Tuple of 9 elements, e.g., `(1, 2, 3, 4, 0, 6, 7, 5, 8)`
- **State Space Size**: 9! = 362,880 possible configurations
- **Solvable States**: Only half (~181,440) are actually reachable from any given state
- **Branching Factor**: 2-4 neighbors per state (depending on empty space position)
- **Goal State**: `(1, 2, 3, 4, 5, 6, 7, 8, 0)` where 0 represents empty space

### **Move Generation**
Only the empty space can "move" by swapping with adjacent tiles:
```python
def get_neighbors(self, state):
    neighbors = []
    empty_idx = state.index(0)  # Find empty space
    empty_row, empty_col = empty_idx // 3, empty_idx % 3
    
    # Try moving empty space in 4 directions
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[empty_idx], new_state[new_idx] = new_state[new_idx], new_state[empty_idx]
            neighbors.append(tuple(new_state))
    
    return neighbors
```

---

## 🔍 **Algorithm Details**

### **1. Breadth-First Search (BFS)**
```python
def bfs(self, initial_state):
    if initial_state == self.goal_state:
        return [initial_state], {'path_length': 0, 'nodes_explored': 1}
    
    queue = deque([initial_state])
    visited = {initial_state}
    parent = {initial_state: None}
    
    while queue:
        current = queue.popleft()
        self.nodes_explored += 1
        
        for neighbor in self.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                
                if neighbor == self.goal_state:
                    return self.reconstruct_path(parent, initial_state, neighbor)
                
                queue.append(neighbor)
    
    return None  # No solution found
```

**Key Properties:**
- **Guarantees**: Finds shortest solution (minimum moves)
- **Completeness**: Always finds solution if one exists
- **Memory Usage**: Exponential - stores all states at current depth
- **Performance**: Explores every state at depths 1, 2, ..., d before finding solution at depth d+1

### **2. A* with Manhattan Distance Heuristic**
```python
def astar_manhattan(self, initial_state):
    h_initial = self.manhattan_distance(initial_state)
    pq = [(h_initial, 0, initial_state)]  # (f_cost, g_cost, state)
    g_costs = {initial_state: 0}
    parent = {initial_state: None}
    visited = set()
    
    while pq:
        f_cost, g_cost, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        
        if current == self.goal_state:
            return self.reconstruct_path(parent, initial_state, current)
        
        for neighbor in self.get_neighbors(current):
            tentative_g = g_cost + 1
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                parent[neighbor] = current
                h_cost = self.manhattan_distance(neighbor)
                f_cost = tentative_g + h_cost
                heapq.heappush(pq, (f_cost, tentative_g, neighbor))
    
    return None
```

**Manhattan Distance Heuristic:**
```python
def manhattan_distance(self, state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:  # Skip empty space
            current_row, current_col = i // 3, i % 3
            goal_idx = self.goal_state.index(tile)
            goal_row, goal_col = goal_idx // 3, goal_idx % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance
```

**Properties:**
- **Admissible**: Never overestimates actual moves needed
- **Informative**: Provides good guidance toward goal
- **Calculation**: Sum of Manhattan distances for all tiles

### **3. A* with Misplaced Tiles Heuristic**
```python
def astar_misplaced(self, initial_state):
    # Similar structure to Manhattan distance A*
    # But uses misplaced_tiles() for heuristic calculation
    pass

def misplaced_tiles(self, state):
    count = 0
    for i, tile in enumerate(state):
        if tile != 0 and tile != self.goal_state[i]:
            count += 1
    return count
```

**Misplaced Tiles Heuristic:**
- **Admissible**: Each misplaced tile needs at least 1 move
- **Less Informed**: Doesn't consider how far tiles are from their goals
- **Simpler**: Easy to understand and compute

---

## 🧪 **Test Cases & Expected Results**

### **Test Case 1: Easy (2 moves)**
```python
initial_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Visual representation:
# Initial:    Goal:
# 1 2 3      1 2 3
# 4 5 6  →   4 5 6
# 7   8      7 8
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Time (ms) | Solution Found |
|-----------|-------------|----------------|-----------|----------------|
| BFS | 2 | ~10-15 | <1 | ✅ Yes |
| A* (Manhattan) | 2 | ~5-8 | <1 | ✅ Yes |
| A* (Misplaced) | 2 | ~6-10 | <1 | ✅ Yes |

**Solution Path:**
1. `(1,2,3,4,5,6,7,0,8)` - Initial state
2. `(1,2,3,4,5,6,7,8,0)` - Move 8 right
3. Goal reached!

### **Test Case 2: Medium (4 moves)**
```python
initial_state = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Visual representation:
# Initial:    Goal:
# 1 2 3      1 2 3
# 4   6  →   4 5 6
# 7 5 8      7 8
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Time (ms) | Efficiency |
|-----------|-------------|----------------|-----------|------------|
| BFS | 4 | ~50-80 | 1-5 | Slow but optimal |
| A* (Manhattan) | 4 | ~15-25 | <1 | Very efficient |
| A* (Misplaced) | 4 | ~25-35 | <1 | Moderately efficient |

### **Test Case 3: Hard (14+ moves)**
```python
initial_state = (8, 1, 2, 0, 4, 3, 7, 6, 5)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Visual representation:
# Initial:    Goal:
# 8 1 2      1 2 3
#   4 3  →   4 5 6
# 7 6 5      7 8
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Time (ms) | Scalability |
|-----------|-------------|----------------|-----------|-------------|
| BFS | 14-16 | ~10,000-50,000 | 100-1000 | Poor - exponential |
| A* (Manhattan) | 14-16 | ~100-500 | 5-20 | Excellent |
| A* (Misplaced) | 14-16 | ~500-2000 | 20-50 | Good |

### **Test Case 4: Very Hard (20+ moves)**
```python
initial_state = (5, 4, 0, 6, 1, 8, 7, 3, 2)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
```

**Expected Results:**
| Algorithm | Path Length | Nodes Explored | Time (ms) | Feasibility |
|-----------|-------------|----------------|-----------|-------------|
| BFS | 20+ | >100,000 | >5000 | Impractical |
| A* (Manhattan) | 20+ | ~1,000-5,000 | 50-200 | Feasible |
| A* (Misplaced) | 20+ | ~5,000-20,000 | 200-800 | Challenging |

---

## 📊 **Performance Analysis**

### **Heuristic Quality Comparison**

| Metric | No Heuristic (BFS) | Misplaced Tiles | Manhattan Distance |
|--------|-------------------|-----------------|-------------------|
| **Admissible** | N/A | ✅ Yes | ✅ Yes |
| **Informative** | None | Low | High |
| **Node Reduction** | 1× (baseline) | ~5-10× | ~20-50× |
| **Computation Cost** | None | O(1) | O(1) |
| **Best for** | Guaranteed optimal | Simple problems | Complex problems |

### **Branching Factor Analysis**
The empty space position affects the number of possible moves:

| Empty Space Position | Possible Moves | Examples |
|---------------------|----------------|----------|
| Corner | 2 | Positions 0, 2, 6, 8 |
| Edge | 3 | Positions 1, 3, 5, 7 |
| Center | 4 | Position 4 |

**Average Branching Factor**: ~3.2

### **State Space Explosion**
```
Depth 0: 1 state
Depth 1: ~3 states
Depth 2: ~9 states  
Depth 3: ~27 states
Depth d: ~3^d states
```

**BFS Memory Usage:**
- Depth 10: ~59,000 states
- Depth 15: ~14,000,000 states  
- Depth 20: ~3,500,000,000 states (impractical)

**A* with Manhattan Distance:**
- Explores orders of magnitude fewer states
- Makes deeper searches feasible
- Maintains optimality guarantee

---

## 🧠 **Key Concepts**

### **Admissible Heuristics**
A heuristic h(n) is admissible if it never overestimates the actual cost to reach the goal.

**Why Manhattan Distance is Admissible:**
- Each tile must move at least its Manhattan distance to reach its goal
- Tiles cannot "jump over" each other, so this is a lower bound
- Sum of individual lower bounds is a lower bound for the whole puzzle

**Why Misplaced Tiles is Admissible:**
- Each misplaced tile requires at least one move to correct
- This underestimates because multiple tiles might need multiple moves

### **Heuristic Dominance**
Heuristic h₁ dominates h₂ if h₁(n) ≥ h₂(n) for all n, and both are admissible.

**Manhattan Distance dominates Misplaced Tiles:**
- Manhattan distance ≥ Misplaced tiles for any state
- Manhattan distance is more informative
- A* with Manhattan distance typically explores fewer nodes

### **The Importance of Heuristics**
```python
# Example state analysis
state = (2, 1, 3, 4, 5, 6, 7, 8, 0)

# Misplaced tiles: Only tile 2 and 1 are misplaced = 2
# Manhattan distance: |0-1| + |1-0| = 2 (for tiles 2 and 1)

# In this case, both give the same value, but Manhattan 
# distance is more precise in general
```

---

## 🎓 **Educational Exercises**

### **Manual Problem Solving**
1. **Hand Solve**: Solve the easy test case manually, counting your moves
2. **Strategy Analysis**: What strategy did you use? Was it optimal?
3. **State Counting**: How many different states did you consider?

### **Algorithm Tracing**
1. **BFS Trace**: Trace BFS on paper for the easy test case
2. **Heuristic Calculation**: Calculate both heuristics for several states
3. **A* Trace**: Trace A* with Manhattan distance heuristic

### **Experimental Analysis**
1. **Performance Testing**: Run algorithms on increasingly difficult puzzles
2. **Heuristic Comparison**: Compare node exploration between heuristics
3. **Memory Analysis**: Monitor memory usage during BFS vs A*

### **Implementation Challenges**
1. **New Heuristics**: Design and test custom heuristic functions
2. **Bidirectional Search**: Implement search from both start and goal
3. **Iterative Deepening A***: Implement memory-efficient variant
4. **15-Puzzle**: Scale up to the 4×4 version (much harder!)

---

## 🤔 **Deep Thinking Questions**

### **Theoretical Questions**
1. **Why is the 8-puzzle state space finite but the search tree potentially infinite?**
2. **Under what conditions would DFS outperform BFS for the 8-puzzle?**
3. **Can you design a better heuristic than Manhattan distance for this problem?**
4. **How would the algorithms perform on the 15-puzzle (4×4 grid)?**

### **Practical Questions**
1. **When would you choose BFS over A* despite the performance difference?**
2. **How could you modify A* to find multiple solutions?**
3. **What trade-offs exist between heuristic computation time and search efficiency?**

### **Analysis Questions**
1. **Why does the performance difference between algorithms become more dramatic as puzzle difficulty increases?**
2. **How does the quality of the initial heuristic estimate correlate with total search efficiency?**
3. **What patterns do you notice in the states that A* explores vs those that BFS explores?**

---

## 🚀 **Getting Started**

### **Recommended Learning Path**

#### **Phase 1: Understanding (30 minutes)**
1. Read this guide's problem definition and algorithm sections
2. Open `puzzle_search_lab.ipynb` 
3. Run the setup cells and examine the puzzle visualization
4. Try solving an easy puzzle manually

#### **Phase 2: Experimentation (45 minutes)**  
1. Run all algorithms on easy and medium test cases
2. Compare the results and understand the differences
3. Try modifying the test cases to see how performance changes
4. Experiment with custom puzzle configurations

#### **Phase 3: Implementation (60 minutes)**
1. Open `puzzle_search.py` 
2. Complete the TODO sections for BFS and A* algorithms
3. Implement both heuristic functions carefully
4. Test your implementations against the notebook solutions

#### **Phase 4: Analysis (30 minutes)**
1. Answer the deep thinking questions
2. Try the implementation challenges
3. Reflect on what you learned about heuristic search

---

## 🔗 **Additional Resources**

### **Academic References**
- Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A Formal Basis for the Heuristic Determination of Minimum Cost Paths. IEEE Transactions on Systems Science and Cybernetics, 4(2), 100-107.
- Russell, S., & Norvig, P. (2020). Artificial Intelligence: A Modern Approach (4th ed.). Chapter 3: Solving Problems by Searching.

### **Online Resources**
- [8-Puzzle Online Solver](https://deniz.co/8-puzzle-solver/) - Interactive puzzle solver
- [A* Algorithm Visualization](https://qiao.github.io/PathFinding.js/visual/) - Visual demonstration
- [15-Puzzle History](https://www.britannica.com/topic/15-puzzle) - Historical context

### **Extensions to Explore**
- **N-Puzzle Variants**: 15-puzzle, 24-puzzle, sliding puzzle variations
- **Other State Space Problems**: Tower of Hanoi, Water Jug Problem, Missionaries and Cannibals
- **Advanced Search Algorithms**: IDA*, SMA*, bidirectional search

---

*This extended guide provides a comprehensive foundation for understanding both the 8-puzzle problem and heuristic search algorithms. Use it as a reference while implementing, experimenting, and analyzing these powerful AI techniques.*
