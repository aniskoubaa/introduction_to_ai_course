# 🧩 8-Puzzle Search Lab
*Solve sliding puzzles using intelligent search algorithms*

## What You'll Learn
Compare BFS and A* algorithms with different heuristics for solving the classic 8-puzzle.

## 🎯 The Puzzle
Slide numbered tiles to reach the goal configuration:

```
Start:               Goal:
┌───┬───┬───┐       ┌───┬───┬───┐
│ 1 │ 2 │ 3 │       │ 1 │ 2 │ 3 │
├───┼───┼───┤       ├───┼───┼───┤
│ 4 │   │ 6 │  →    │ 4 │ 5 │ 6 │
├───┼───┼───┤       ├───┼───┼───┤
│ 7 │ 5 │ 8 │       │ 7 │ 8 │   │
└───┴───┴───┘       └───┴───┴───┘
```

## 🚀 How to Use
1. **Open** `puzzle_search_lab.ipynb` in Jupyter or Google Colab
2. **Run each cell** step by step  
3. **Watch** algorithms solve puzzles and compare performance
4. **Try** different puzzle configurations

## 🔍 Algorithms Implemented
- **BFS**: Finds optimal solution, explores many states
- **A* (Manhattan)**: Uses Manhattan distance heuristic, very efficient  
- **A* (Misplaced)**: Uses misplaced tiles heuristic, less efficient than Manhattan

## 📋 What You'll See
The notebook includes:
- **Multiple test puzzles**: Easy, medium, and challenging configurations
- **Beautiful puzzle display**: Visual grid with numbered tiles
- **Performance comparison**: Solution length, nodes explored, time taken  
- **Heuristic comparison**: See how different heuristics affect efficiency

## 💡 Key Questions  
After running the lab, ask yourself:
1. **Which algorithm solved puzzles fastest?**
2. **How do the two heuristics compare?**
3. **Why is Manhattan distance better than misplaced tiles?**
4. **When would you use BFS vs A*?**

## 🎯 Learning Goals
- Understand heuristic search advantages
- Compare different heuristic functions
- See the power of informed search
- Practice state space problem solving

## 🔤 Heuristics Explained
- **Manhattan Distance**: Sum of |current_row - goal_row| + |current_col - goal_col| for each tile
- **Misplaced Tiles**: Count of tiles not in correct positions

---
*The 8-puzzle shows why smart algorithms matter - A* can solve in seconds what takes BFS much longer!*
