# Week 2-3: Search Algorithms

## 📚 Module Overview

This two-week module provides a comprehensive introduction to search algorithms in AI, covering both uninformed and informed search strategies. Students will learn to formulate problems as search problems and implement various algorithms to solve them efficiently.

---

## 🎯 Learning Objectives

By the end of this module, students should be able to:
- Formulate problems as search problems (state space, actions, goal test)
- Understand and implement uninformed search algorithms (BFS, DFS, UCS)
- Understand and implement informed search algorithms (Greedy, A*)
- Design and evaluate heuristic functions
- Analyze time and space complexity of search algorithms
- Apply appropriate search algorithms to different problem domains

---

## 📅 Two-Week Schedule

### **Week 2: Uninformed Search**
| **Session** | **Topic** | **Activities** |
|-------------|-----------|----------------|
| **Lecture 1** | Problem Formulation | State spaces, search trees, search graphs |
| **Lecture 2** | BFS, DFS, UCS | Algorithm implementation and analysis |
| **Lab** | Search Coding | Implement basic search algorithms |

### **Week 3: Informed Search**  
| **Session** | **Topic** | **Activities** |
|-------------|-----------|----------------|
| **Lecture 1** | Greedy & A* Search | Best-first search strategies |
| **Lecture 2** | Heuristics | Heuristic design and evaluation |
| **Lab** | A* Implementation | Advanced search algorithms |
| **Quiz** | Search Algorithms | Assessment covering all search topics |

---

## 📁 Folder Contents

### 📊 **slides/**
- `01_problem_formulation.pdf` - Search problem definition and representation
- `02_uninformed_search_bfs_dfs.pdf` - Breadth-first and depth-first search
- `03_uniform_cost_search.pdf` - Cost-based uninformed search
- `04_informed_search_greedy_astar.pdf` - Heuristic-guided search
- `05_heuristics.pdf` - Heuristic design and properties

### 💻 **labs/**
- **`week02_uninformed_search/`**
  - `bfs_dfs_implementation.md` - Basic search algorithm lab
  - `code/` - Starter code for uninformed search
- **`week03_informed_search/`**
  - `astar_implementation.md` - A* algorithm lab
  - `code/` - Starter code for informed search

### 📝 **exercises/**
- `search_problems_uninformed.md` - BFS, DFS, UCS practice problems
- `search_problems_informed.md` - Greedy and A* exercises
- `heuristic_design_exercises.md` - Creating and evaluating heuristics

### ✅ **solutions/**
- `lab_solutions_week02.md` - Uninformed search lab solutions
- `lab_solutions_week03.md` - Informed search lab solutions
- `exercise_solutions.md` - All exercise solutions with explanations

### 📖 **resources/**
- `search_visualization_tools.md` - Tools for visualizing search algorithms
- `additional_algorithms.md` - Other search variants (IDS, bidirectional)
- `demos/` - Interactive search demonstrations

---

## 📖 Required Readings

- Russell & Norvig, Ch 3: Solving Problems by Searching
- Russell & Norvig, Ch 4: Beyond Classical Search (selected sections)

---

## 🎯 Key Algorithms Covered

### **Uninformed Search**
- **Breadth-First Search (BFS)** - Optimal for unweighted graphs
- **Depth-First Search (DFS)** - Memory efficient but not optimal  
- **Uniform Cost Search (UCS)** - Optimal for weighted graphs

### **Informed Search**
- **Greedy Best-First** - Fast but not optimal
- **A* Search** - Optimal with admissible heuristics
- **Heuristic Functions** - Manhattan distance, Euclidean distance, etc.

---

## 🔧 Implementation Focus

- **Problem Representation**: State spaces, successor functions
- **Algorithm Efficiency**: Time/space complexity analysis
- **Heuristic Design**: Admissibility and consistency
- **Real Applications**: Path finding, puzzle solving, planning

---

## 📊 Assessment

- **Assignment 1**: Search algorithm implementation (released Week 2)
- **Quiz 1**: Comprehensive search assessment (Week 3)
- **Lab Activities**: Hands-on coding exercises both weeks

---

*This module forms the foundation for many AI techniques. Mastery of search algorithms is essential for understanding planning, game playing, and constraint satisfaction.*
