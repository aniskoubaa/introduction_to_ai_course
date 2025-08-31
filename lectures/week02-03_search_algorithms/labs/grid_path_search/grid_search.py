"""
Grid Path Search - Educational Implementation
============================================

This module contains starter code for implementing search algorithms
on a 2D grid. Students should complete the TODO sections.

Author: Prof. Anis Koubaa
Course: SE 444 - Introduction to AI
"""

from collections import deque
import heapq
import time

class GridSearcher:
    """Class for performing search algorithms on 2D grids."""
    
    def __init__(self, grid):
        """
        Initialize the grid searcher.
        
        Args:
            grid: 2D list where 0 = empty, 1 = obstacle
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.nodes_explored = 0
        
    def reset_stats(self):
        """Reset search statistics."""
        self.nodes_explored = 0
    
    def is_valid_position(self, row, col):
        """
        Check if a position is valid and passable.
        
        Args:
            row, col: Position coordinates
            
        Returns:
            bool: True if position is valid and not an obstacle
        """
        # TODO: Implement validation logic
        # Check if position is within grid bounds
        # Check if position is not an obstacle (grid[row][col] != 1)
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.grid[row][col] == 0)
    
    def get_neighbors(self, position):
        """
        Get all valid neighboring positions.
        
        Args:
            position: Tuple (row, col)
            
        Returns:
            List of valid neighboring positions
        """
        row, col = position
        neighbors = []
        
        # TODO: Generate neighbors in 4 directions (up, down, left, right)
        # Directions: up (-1,0), down (1,0), left (0,-1), right (0,1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def manhattan_distance(self, pos1, pos2):
        """
        Calculate Manhattan distance between two positions.
        
        Args:
            pos1, pos2: Tuple positions (row, col)
            
        Returns:
            int: Manhattan distance
        """
        # TODO: Implement Manhattan distance calculation
        # Formula: |x1 - x2| + |y1 - y2|
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def reconstruct_path(self, parent, start, goal):
        """
        Reconstruct path from start to goal using parent pointers.
        
        Args:
            parent: Dictionary mapping child -> parent
            start: Start position
            goal: Goal position
            
        Returns:
            List of positions from start to goal
        """
        path = []
        current = goal
        
        # TODO: Implement path reconstruction
        # Start from goal and follow parent pointers back to start
        while current is not None:
            path.append(current)
            current = parent.get(current)
        
        path.reverse()
        return path
    
    def bfs(self, start, goal):
        """
        Breadth-First Search implementation.
        
        Args:
            start: Starting position (row, col)
            goal: Goal position (row, col)
            
        Returns:
            Tuple (path, stats) where path is list of positions or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement BFS algorithm
        # 1. Initialize queue with start position
        # 2. Keep track of visited positions
        # 3. Keep track of parent pointers for path reconstruction
        # 4. Process nodes level by level until goal is found
        
        queue = deque([start])
        visited = {start}
        parent = {start: None}
        
        while queue:
            current = queue.popleft()
            self.nodes_explored += 1
            
            # Check if goal reached
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                end_time = time.time()
                stats = {
                    'algorithm': 'BFS',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time': end_time - start_time
                }
                return path, stats
            
            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        # No path found
        end_time = time.time()
        stats = {
            'algorithm': 'BFS',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def dfs(self, start, goal, max_depth=50):
        """
        Depth-First Search implementation.
        
        Args:
            start: Starting position (row, col)
            goal: Goal position (row, col)
            max_depth: Maximum search depth to prevent infinite loops
            
        Returns:
            Tuple (path, stats) where path is list of positions or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement DFS algorithm
        # 1. Use a stack (list) for DFS exploration
        # 2. Keep track of visited positions
        # 3. Keep track of parent pointers for path reconstruction
        # 4. Include depth tracking to limit search depth
        
        stack = [(start, 0)]  # (position, depth)
        visited = {start}
        parent = {start: None}
        
        while stack:
            current, depth = stack.pop()
            self.nodes_explored += 1
            
            # Check if goal reached
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                end_time = time.time()
                stats = {
                    'algorithm': 'DFS',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time': end_time - start_time
                }
                return path, stats
            
            # Check depth limit
            if depth >= max_depth:
                continue
            
            # Explore neighbors (in reverse order for consistent behavior)
            neighbors = self.get_neighbors(current)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    stack.append((neighbor, depth + 1))
        
        # No path found
        end_time = time.time()
        stats = {
            'algorithm': 'DFS',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def ucs(self, start, goal):
        """
        Uniform-Cost Search implementation.
        
        Args:
            start: Starting position (row, col)
            goal: Goal position (row, col)
            
        Returns:
            Tuple (path, stats) where path is list of positions or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement UCS algorithm
        # 1. Use a priority queue (heapq) ordered by path cost
        # 2. Keep track of best known cost to each position
        # 3. Keep track of parent pointers for path reconstruction
        # 4. Each step has cost = 1 for this grid problem
        
        priority_queue = [(0, start)]  # (cost, position)
        costs = {start: 0}
        parent = {start: None}
        visited = set()
        
        while priority_queue:
            current_cost, current = heapq.heappop(priority_queue)
            
            # Skip if already processed with better cost
            if current in visited:
                continue
                
            visited.add(current)
            self.nodes_explored += 1
            
            # Check if goal reached
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                end_time = time.time()
                stats = {
                    'algorithm': 'UCS',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time': end_time - start_time
                }
                return path, stats
            
            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                new_cost = current_cost + 1  # Each step costs 1
                
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(priority_queue, (new_cost, neighbor))
        
        # No path found
        end_time = time.time()
        stats = {
            'algorithm': 'UCS',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def astar(self, start, goal):
        """
        A* Search implementation.
        
        Args:
            start: Starting position (row, col)
            goal: Goal position (row, col)
            
        Returns:
            Tuple (path, stats) where path is list of positions or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement A* algorithm
        # 1. Use a priority queue ordered by f(n) = g(n) + h(n)
        # 2. g(n) = actual cost from start
        # 3. h(n) = heuristic cost to goal (Manhattan distance)
        # 4. Keep track of parent pointers for path reconstruction
        
        h_start = self.manhattan_distance(start, goal)
        priority_queue = [(h_start, 0, start)]  # (f_cost, g_cost, position)
        g_costs = {start: 0}
        parent = {start: None}
        visited = set()
        
        while priority_queue:
            f_cost, g_cost, current = heapq.heappop(priority_queue)
            
            # Skip if already processed
            if current in visited:
                continue
                
            visited.add(current)
            self.nodes_explored += 1
            
            # Check if goal reached
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                end_time = time.time()
                stats = {
                    'algorithm': 'A*',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time': end_time - start_time
                }
                return path, stats
            
            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost + 1  # Each step costs 1
                
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    parent[neighbor] = current
                    h_cost = self.manhattan_distance(neighbor, goal)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(priority_queue, (f_cost, tentative_g, neighbor))
        
        # No path found
        end_time = time.time()
        stats = {
            'algorithm': 'A*',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def visualize_grid(self, path=None):
        """
        Print a visual representation of the grid and path.
        
        Args:
            path: List of positions to highlight as path
        """
        print("\nGrid Visualization:")
        print("S = Start, G = Goal, █ = Obstacle, . = Empty, * = Path")
        print()
        
        for row in range(self.rows):
            for col in range(self.cols):
                pos = (row, col)
                if self.grid[row][col] == 1:
                    print("█", end=" ")
                elif path and pos == path[0]:
                    print("S", end=" ")
                elif path and pos == path[-1]:
                    print("G", end=" ")
                elif path and pos in path:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

def test_algorithms():
    """Test all algorithms on sample grids."""
    
    # Simple 3x3 grid with no obstacles
    simple_grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    
    # 5x5 maze grid
    maze_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    test_cases = [
        ("Simple Grid", simple_grid, (0, 0), (2, 2)),
        ("Maze Grid", maze_grid, (0, 0), (0, 4))
    ]
    
    algorithms = ['bfs', 'dfs', 'ucs', 'astar']
    
    for grid_name, grid, start, goal in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing on {grid_name}")
        print(f"Start: {start}, Goal: {goal}")
        print(f"{'='*50}")
        
        searcher = GridSearcher(grid)
        searcher.visualize_grid()
        
        results = []
        for algorithm in algorithms:
            try:
                if algorithm == 'bfs':
                    path, stats = searcher.bfs(start, goal)
                elif algorithm == 'dfs':
                    path, stats = searcher.dfs(start, goal)
                elif algorithm == 'ucs':
                    path, stats = searcher.ucs(start, goal)
                elif algorithm == 'astar':
                    path, stats = searcher.astar(start, goal)
                
                results.append((algorithm.upper(), path, stats))
            except Exception as e:
                print(f"Error in {algorithm}: {e}")
        
        # Display results
        print(f"{'Algorithm':<10} {'Path Length':<12} {'Nodes Explored':<15} {'Time (ms)':<10} {'Found'}")
        print("-" * 65)
        
        for algo, path, stats in results:
            found = "Yes" if path else "No"
            time_ms = f"{stats['time']*1000:.2f}"
            print(f"{algo:<10} {stats['path_length']:<12} {stats['nodes_explored']:<15} {time_ms:<10} {found}")
        
        # Show path for first successful algorithm
        for algo, path, stats in results:
            if path:
                print(f"\nPath found by {algo}:")
                print(f"Path: {path}")
                searcher.visualize_grid(path)
                break

if __name__ == "__main__":
    print("Grid Path Search - Search Algorithm Comparison")
    print("=" * 50)
    test_algorithms()
