"""
8-Puzzle Search - Educational Implementation
===========================================

This module contains starter code for implementing search algorithms
on the classic 8-puzzle. Students should complete the TODO sections.

Author: Prof. Anis Koubaa
Course: SE 444 - Introduction to AI
"""

from collections import deque
import heapq
import time

class PuzzleSearcher:
    """Class for performing search algorithms on the 8-puzzle."""
    
    def __init__(self):
        """Initialize the puzzle searcher."""
        self.nodes_explored = 0
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 represents empty space
        
    def reset_stats(self):
        """Reset search statistics."""
        self.nodes_explored = 0
    
    def tuple_to_2d(self, state):
        """
        Convert tuple state to 2D list for display.
        
        Args:
            state: Tuple representing puzzle state
            
        Returns:
            2D list (3x3) representation
        """
        return [list(state[i:i+3]) for i in range(0, 9, 3)]
    
    def print_puzzle(self, state):
        """
        Pretty print the puzzle state.
        
        Args:
            state: Tuple representing puzzle state
        """
        puzzle_2d = self.tuple_to_2d(state)
        print("┌───┬───┬───┐")
        for i, row in enumerate(puzzle_2d):
            print("│", end="")
            for cell in row:
                if cell == 0:
                    print("   │", end="")
                else:
                    print(f" {cell} │", end="")
            print()
            if i < 2:
                print("├───┼───┼───┤")
        print("└───┴───┴───┘")
    
    def get_empty_position(self, state):
        """
        Find the position of the empty space (0) in the puzzle.
        
        Args:
            state: Tuple representing puzzle state
            
        Returns:
            int: Index of empty space in the tuple
        """
        # TODO: Find and return the index of 0 in the state tuple
        return state.index(0)
    
    def get_neighbors(self, state):
        """
        Generate all valid neighboring states by moving the empty space.
        
        Args:
            state: Current puzzle state
            
        Returns:
            List of valid neighboring states
        """
        neighbors = []
        empty_idx = self.get_empty_position(state)
        empty_row, empty_col = empty_idx // 3, empty_idx % 3
        
        # TODO: Generate neighbors by moving empty space in 4 directions
        # Directions: up (-1,0), down (1,0), left (0,-1), right (0,1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            
            # Check if new position is valid
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Calculate new index
                new_idx = new_row * 3 + new_col
                
                # Create new state by swapping empty space with tile
                new_state = list(state)
                new_state[empty_idx], new_state[new_idx] = new_state[new_idx], new_state[empty_idx]
                neighbors.append(tuple(new_state))
        
        return neighbors
    
    def manhattan_distance(self, state):
        """
        Calculate Manhattan distance heuristic for A*.
        
        Args:
            state: Current puzzle state
            
        Returns:
            int: Sum of Manhattan distances for all tiles
        """
        distance = 0
        
        # TODO: Implement Manhattan distance heuristic
        # For each tile (except empty space), calculate its Manhattan distance
        # from current position to goal position
        
        for i, tile in enumerate(state):
            if tile != 0:  # Skip empty space
                # Current position
                current_row, current_col = i // 3, i % 3
                
                # Goal position for this tile
                goal_idx = self.goal_state.index(tile)
                goal_row, goal_col = goal_idx // 3, goal_idx % 3
                
                # Manhattan distance for this tile
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        
        return distance
    
    def misplaced_tiles(self, state):
        """
        Calculate number of misplaced tiles heuristic.
        
        Args:
            state: Current puzzle state
            
        Returns:
            int: Number of tiles not in their goal positions
        """
        count = 0
        
        # TODO: Count tiles that are not in their correct positions
        # Don't count the empty space (0)
        
        for i, tile in enumerate(state):
            if tile != 0 and tile != self.goal_state[i]:
                count += 1
        
        return count
    
    def reconstruct_path(self, parent, start, goal):
        """
        Reconstruct path from start to goal using parent pointers.
        
        Args:
            parent: Dictionary mapping child -> parent
            start: Start state
            goal: Goal state
            
        Returns:
            List of states from start to goal
        """
        path = []
        current = goal
        
        while current is not None:
            path.append(current)
            current = parent.get(current)
        
        path.reverse()
        return path
    
    def bfs(self, initial_state):
        """
        Breadth-First Search for 8-puzzle.
        
        Args:
            initial_state: Starting puzzle state
            
        Returns:
            Tuple (path, stats) where path is list of states or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement BFS for puzzle solving
        # 1. Initialize queue with initial state
        # 2. Keep track of visited states to avoid cycles
        # 3. Keep track of parent pointers for path reconstruction
        # 4. Process states level by level until goal is found
        
        if initial_state == self.goal_state:
            end_time = time.time()
            stats = {
                'algorithm': 'BFS',
                'path_length': 0,
                'nodes_explored': 1,
                'time': end_time - start_time
            }
            return [initial_state], stats
        
        queue = deque([initial_state])
        visited = {initial_state}
        parent = {initial_state: None}
        
        while queue:
            current = queue.popleft()
            self.nodes_explored += 1
            
            # Generate and explore neighbors
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    
                    # Check if goal reached
                    if neighbor == self.goal_state:
                        path = self.reconstruct_path(parent, initial_state, neighbor)
                        end_time = time.time()
                        stats = {
                            'algorithm': 'BFS',
                            'path_length': len(path) - 1,
                            'nodes_explored': self.nodes_explored,
                            'time': end_time - start_time
                        }
                        return path, stats
                    
                    queue.append(neighbor)
        
        # No solution found
        end_time = time.time()
        stats = {
            'algorithm': 'BFS',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def dfs(self, initial_state, max_depth=20):
        """
        Depth-First Search for 8-puzzle with depth limit.
        
        Args:
            initial_state: Starting puzzle state
            max_depth: Maximum search depth
            
        Returns:
            Tuple (path, stats) where path is list of states or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement DFS with depth limit for puzzle solving
        # 1. Use a stack for DFS exploration
        # 2. Include depth tracking to limit search depth
        # 3. Keep track of visited states and parent pointers
        
        if initial_state == self.goal_state:
            end_time = time.time()
            stats = {
                'algorithm': 'DFS',
                'path_length': 0,
                'nodes_explored': 1,
                'time': end_time - start_time
            }
            return [initial_state], stats
        
        stack = [(initial_state, 0)]  # (state, depth)
        visited = {initial_state}
        parent = {initial_state: None}
        
        while stack:
            current, depth = stack.pop()
            self.nodes_explored += 1
            
            # Check depth limit
            if depth >= max_depth:
                continue
            
            # Generate and explore neighbors
            neighbors = self.get_neighbors(current)
            for neighbor in reversed(neighbors):  # Reverse for consistent behavior
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    
                    # Check if goal reached
                    if neighbor == self.goal_state:
                        path = self.reconstruct_path(parent, initial_state, neighbor)
                        end_time = time.time()
                        stats = {
                            'algorithm': 'DFS',
                            'path_length': len(path) - 1,
                            'nodes_explored': self.nodes_explored,
                            'time': end_time - start_time
                        }
                        return path, stats
                    
                    stack.append((neighbor, depth + 1))
        
        # No solution found within depth limit
        end_time = time.time()
        stats = {
            'algorithm': 'DFS',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def astar_manhattan(self, initial_state):
        """
        A* search using Manhattan distance heuristic.
        
        Args:
            initial_state: Starting puzzle state
            
        Returns:
            Tuple (path, stats) where path is list of states or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement A* with Manhattan distance heuristic
        # 1. Use priority queue ordered by f(n) = g(n) + h(n)
        # 2. g(n) = number of moves from start
        # 3. h(n) = Manhattan distance heuristic
        
        if initial_state == self.goal_state:
            end_time = time.time()
            stats = {
                'algorithm': 'A* (Manhattan)',
                'path_length': 0,
                'nodes_explored': 1,
                'time': end_time - start_time
            }
            return [initial_state], stats
        
        h_initial = self.manhattan_distance(initial_state)
        priority_queue = [(h_initial, 0, initial_state)]  # (f_cost, g_cost, state)
        g_costs = {initial_state: 0}
        parent = {initial_state: None}
        visited = set()
        
        while priority_queue:
            f_cost, g_cost, current = heapq.heappop(priority_queue)
            
            # Skip if already processed
            if current in visited:
                continue
            
            visited.add(current)
            self.nodes_explored += 1
            
            # Check if goal reached
            if current == self.goal_state:
                path = self.reconstruct_path(parent, initial_state, current)
                end_time = time.time()
                stats = {
                    'algorithm': 'A* (Manhattan)',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time': end_time - start_time
                }
                return path, stats
            
            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost + 1
                
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    parent[neighbor] = current
                    h_cost = self.manhattan_distance(neighbor)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(priority_queue, (f_cost, tentative_g, neighbor))
        
        # No solution found
        end_time = time.time()
        stats = {
            'algorithm': 'A* (Manhattan)',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def astar_misplaced(self, initial_state):
        """
        A* search using misplaced tiles heuristic.
        
        Args:
            initial_state: Starting puzzle state
            
        Returns:
            Tuple (path, stats) where path is list of states or None
        """
        self.reset_stats()
        start_time = time.time()
        
        # TODO: Implement A* with misplaced tiles heuristic
        # Similar to Manhattan distance version but use misplaced_tiles() for h(n)
        
        if initial_state == self.goal_state:
            end_time = time.time()
            stats = {
                'algorithm': 'A* (Misplaced)',
                'path_length': 0,
                'nodes_explored': 1,
                'time': end_time - start_time
            }
            return [initial_state], stats
        
        h_initial = self.misplaced_tiles(initial_state)
        priority_queue = [(h_initial, 0, initial_state)]  # (f_cost, g_cost, state)
        g_costs = {initial_state: 0}
        parent = {initial_state: None}
        visited = set()
        
        while priority_queue:
            f_cost, g_cost, current = heapq.heappop(priority_queue)
            
            # Skip if already processed
            if current in visited:
                continue
            
            visited.add(current)
            self.nodes_explored += 1
            
            # Check if goal reached
            if current == self.goal_state:
                path = self.reconstruct_path(parent, initial_state, current)
                end_time = time.time()
                stats = {
                    'algorithm': 'A* (Misplaced)',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time': end_time - start_time
                }
                return path, stats
            
            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost + 1
                
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    parent[neighbor] = current
                    h_cost = self.misplaced_tiles(neighbor)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(priority_queue, (f_cost, tentative_g, neighbor))
        
        # No solution found
        end_time = time.time()
        stats = {
            'algorithm': 'A* (Misplaced)',
            'path_length': -1,
            'nodes_explored': self.nodes_explored,
            'time': end_time - start_time
        }
        return None, stats
    
    def show_solution_steps(self, path):
        """
        Display solution steps with puzzle states.
        
        Args:
            path: List of states from initial to goal
        """
        if not path:
            print("No solution found!")
            return
        
        print(f"\nSolution found in {len(path) - 1} moves:")
        print("=" * 40)
        
        for i, state in enumerate(path):
            print(f"Step {i}:")
            self.print_puzzle(state)
            if i < len(path) - 1:
                print("↓")
        
        print("Solution complete!")

def test_algorithms():
    """Test all algorithms on various puzzle instances."""
    
    # Test cases with different difficulty levels
    test_cases = [
        ("Easy (2 moves)", (1, 2, 3, 4, 5, 6, 7, 0, 8)),
        ("Medium (4 moves)", (1, 2, 3, 4, 0, 6, 7, 5, 8)),
        ("Hard (>10 moves)", (8, 1, 2, 0, 4, 3, 7, 6, 5)),
    ]
    
    algorithms = [
        ('BFS', 'bfs'),
        ('A* (Manhattan)', 'astar_manhattan'),
        ('A* (Misplaced)', 'astar_misplaced'),
        ('DFS', 'dfs')
    ]
    
    searcher = PuzzleSearcher()
    
    for test_name, initial_state in test_cases:
        print(f"\n{'='*60}")
        print(f"Testing: {test_name}")
        print(f"{'='*60}")
        
        print("Initial State:")
        searcher.print_puzzle(initial_state)
        print("\nGoal State:")
        searcher.print_puzzle(searcher.goal_state)
        
        print(f"\n{'Algorithm':<15} {'Path Length':<12} {'Nodes Explored':<15} {'Time (ms)':<10} {'Found'}")
        print("-" * 70)
        
        results = []
        
        for algo_name, algo_method in algorithms:
            try:
                if algo_method == 'bfs':
                    path, stats = searcher.bfs(initial_state)
                elif algo_method == 'dfs':
                    path, stats = searcher.dfs(initial_state, max_depth=25)
                elif algo_method == 'astar_manhattan':
                    path, stats = searcher.astar_manhattan(initial_state)
                elif algo_method == 'astar_misplaced':
                    path, stats = searcher.astar_misplaced(initial_state)
                
                found = "Yes" if path else "No"
                time_ms = f"{stats['time']*1000:.2f}"
                print(f"{algo_name:<15} {stats['path_length']:<12} {stats['nodes_explored']:<15} {time_ms:<10} {found}")
                
                if path and len(path) <= 6:  # Show solution for short paths
                    results.append((algo_name, path))
                    
            except Exception as e:
                print(f"{algo_name:<15} {'Error':<12} {'-':<15} {'-':<10} No")
                print(f"  Error: {e}")
        
        # Show solution for first successful algorithm
        if results:
            print(f"\nSample solution ({results[0][0]}):")
            searcher.show_solution_steps(results[0][1])

if __name__ == "__main__":
    print("8-Puzzle Search - Algorithm Comparison")
    print("=" * 50)
    test_algorithms()
