# Grid Path Search - Practice Questions

## 🧠 **Theoretical Questions**

### **1. Algorithm Understanding**
1. **BFS vs DFS**: In a 5×5 grid with no obstacles, will BFS and DFS always find paths of the same length? Why or why not?

2. **Optimality**: Which algorithms guarantee finding the shortest path? Explain why.

3. **Memory Usage**: Which algorithm uses more memory, BFS or DFS? Explain with examples.

4. **Heuristic Admissibility**: Why is Manhattan distance an admissible heuristic for grid pathfinding?

### **2. Trace Execution**
Given this 4×4 grid:
```
S . █ .
. . █ .
. █ . .
. . . G
```
Start: (0,0), Goal: (3,3)

**Questions:**
1. Trace BFS step by step. In what order are positions explored?
2. What path does DFS find if it explores neighbors in the order: Up, Right, Down, Left?
3. Calculate f(n) = g(n) + h(n) for A* at position (1,1).

### **3. Performance Analysis**
For a 10×10 grid with 20% obstacles:
1. **Estimate** how many nodes each algorithm might explore
2. **Predict** which algorithm will be fastest and why
3. **Consider** what happens if the goal is unreachable

### **4. Heuristic Design**
1. **Manhattan Distance**: Calculate the Manhattan distance from (2,1) to (5,4)
2. **Alternative Heuristics**: Propose a different admissible heuristic for grid pathfinding
3. **Heuristic Comparison**: Why might Manhattan distance be better than "number of obstacles between current position and goal"?

## 💻 **Programming Challenges**

### **Challenge 1: Algorithm Modification**
Modify the BFS algorithm to:
- Find ALL shortest paths (not just one)
- Count how many optimal paths exist
- Return the path that makes the fewest turns

### **Challenge 2: Custom Grid**
Create a test case where:
- DFS finds a much longer path than BFS
- A* explores significantly fewer nodes than UCS
- There are multiple optimal paths

### **Challenge 3: Enhanced Visualization**
Add features to show:
- Order of node exploration (numbered)
- Different colors for different algorithms
- Animation of the search process

### **Challenge 4: Diagonal Movement**
Modify the algorithms to allow diagonal movement:
- Update neighbor generation
- Adjust costs (diagonal = √2, straight = 1)
- Update the heuristic function

## 🎯 **Hands-On Exercises**

### **Exercise 1: Manual Tracing**
Using the simple 3×3 grid from the code:
```
S . G
. . .
. . .
```

1. **Hand-trace BFS**: Write down the queue contents at each step
2. **Hand-trace DFS**: Write down the stack contents at each step
3. **Hand-trace A***: Calculate f, g, h values for each node explored

### **Exercise 2: Grid Design**
Design a 5×5 grid where:
- BFS explores exactly 8 nodes to find the goal
- DFS gets stuck and needs to backtrack at least twice
- A* finds the goal in fewer than 5 node explorations

### **Exercise 3: Performance Testing**
Create test grids and measure:
- Average nodes explored by each algorithm
- Time taken for grids of different sizes
- Memory usage differences

### **Exercise 4: Corner Cases**
Test your implementation with:
- Start position same as goal position
- Goal position surrounded by obstacles
- No path exists to goal
- Very large grids (20×20 or bigger)

## 🔍 **Debugging Challenges**

### **Common Bugs to Find and Fix**
Your algorithms might have these bugs. Can you identify and fix them?

1. **Infinite Loop**: Algorithm runs forever
2. **Suboptimal Path**: BFS returns non-optimal path
3. **Memory Error**: A* uses too much memory
4. **Wrong Heuristic**: A* doesn't find optimal path

### **Test Cases for Debugging**
```python
# Bug Test Grid 1: Should expose infinite loop bugs
bug_grid_1 = [
    [0, 0, 0],
    [0, 1, 0], 
    [0, 0, 0]
]

# Bug Test Grid 2: Should expose heuristic bugs
bug_grid_2 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
```

## 📊 **Analysis Questions**

### **Algorithm Comparison**
After running your implementations, answer:

1. **Efficiency**: Rank algorithms by number of nodes explored (best to worst)
2. **Speed**: Rank algorithms by execution time
3. **Memory**: Rank algorithms by memory usage
4. **Reliability**: Which algorithm is most likely to find a solution?

### **When to Use Which Algorithm?**
Provide scenarios where each algorithm is the best choice:
- **BFS**: When is it the best option?
- **DFS**: In what situations would you choose it?
- **UCS**: When does it outperform BFS?
- **A***: What makes it superior to other algorithms?

### **Real-World Applications**
How would these algorithms apply to:
- GPS navigation systems
- Robot path planning
- Video game AI
- Network routing

---

## 📝 **Submission Questions**
*Answer these questions in your lab report:*

1. **Implementation Reflection**: What was the most challenging part to implement? Why?

2. **Algorithm Insights**: Which algorithm surprised you the most in terms of performance? Explain.

3. **Optimization Ideas**: How could you make your implementations faster or use less memory?

4. **Extension Concepts**: What additional features would make this more realistic for robot navigation?

---

*Remember: The goal is understanding, not just getting the right answer. Explain your reasoning for each response!*
