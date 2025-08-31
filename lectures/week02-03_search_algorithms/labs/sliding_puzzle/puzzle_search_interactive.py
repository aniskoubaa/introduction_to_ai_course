# 8-Puzzle Interactive Demo
# SE 444: Introduction to AI - Prof. Anis Koubaa
# Run this in Jupyter/Colab for interactive experience

from collections import deque
import heapq
import time

# Check environment
try:
    import google.colab
    print("📍 Running in Google Colab")
except ImportError:
    print("📍 Running in Local Environment")

class PuzzleSearcher:
    def __init__(self):
        self.nodes_explored = 0
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 = empty space
        
    def reset_stats(self):
        self.nodes_explored = 0
    
    def print_puzzle(self, state):
        """Pretty print puzzle state."""
        puzzle_2d = [list(state[i:i+3]) for i in range(0, 9, 3)]
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
        return state.index(0)
    
    def get_neighbors(self, state):
        """Generate neighboring states by moving empty space."""
        neighbors = []
        empty_idx = self.get_empty_position(state)
        empty_row, empty_col = empty_idx // 3, empty_idx % 3
        
        # Try moving empty space in 4 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = empty_row + dr, empty_col + dc
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_idx = new_row * 3 + new_col
                new_state = list(state)
                new_state[empty_idx], new_state[new_idx] = new_state[new_idx], new_state[empty_idx]
                neighbors.append(tuple(new_state))
        
        return neighbors
    
    def manhattan_distance(self, state):
        """Calculate Manhattan distance heuristic."""
        distance = 0
        for i, tile in enumerate(state):
            if tile != 0:
                current_row, current_col = i // 3, i % 3
                goal_idx = self.goal_state.index(tile)
                goal_row, goal_col = goal_idx // 3, goal_idx % 3
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance
    
    def misplaced_tiles(self, state):
        """Count misplaced tiles heuristic."""
        count = 0
        for i, tile in enumerate(state):
            if tile != 0 and tile != self.goal_state[i]:
                count += 1
        return count
    
    def reconstruct_path(self, parent, start, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent.get(current)
        path.reverse()
        return path

    def bfs(self, initial_state):
        """BFS: Finds shortest solution."""
        if initial_state == self.goal_state:
            return [initial_state], {'algorithm': 'BFS', 'path_length': 0, 
                                   'nodes_explored': 1, 'time_ms': 0}
        
        self.reset_stats()
        start_time = time.time()
        
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
                        path = self.reconstruct_path(parent, initial_state, neighbor)
                        return path, {
                            'algorithm': 'BFS',
                            'path_length': len(path) - 1,
                            'nodes_explored': self.nodes_explored,
                            'time_ms': (time.time() - start_time) * 1000
                        }
                    
                    queue.append(neighbor)
        
        return None, {'algorithm': 'BFS', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def dfs(self, initial_state, max_depth=20):
        """DFS: Depth-first with limit."""
        if initial_state == self.goal_state:
            return [initial_state], {'algorithm': 'DFS', 'path_length': 0, 
                                   'nodes_explored': 1, 'time_ms': 0}
        
        self.reset_stats()
        start_time = time.time()
        
        stack = [(initial_state, 0)]
        visited = {initial_state}
        parent = {initial_state: None}
        
        while stack:
            current, depth = stack.pop()
            self.nodes_explored += 1
            
            if depth < max_depth:
                neighbors = self.get_neighbors(current)
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = current
                        
                        if neighbor == self.goal_state:
                            path = self.reconstruct_path(parent, initial_state, neighbor)
                            return path, {
                                'algorithm': 'DFS',
                                'path_length': len(path) - 1,
                                'nodes_explored': self.nodes_explored,
                                'time_ms': (time.time() - start_time) * 1000
                            }
                        
                        stack.append((neighbor, depth + 1))
        
        return None, {'algorithm': 'DFS', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def astar_manhattan(self, initial_state):
        """A* with Manhattan distance heuristic."""
        if initial_state == self.goal_state:
            return [initial_state], {'algorithm': 'A* (Manhattan)', 'path_length': 0, 
                                   'nodes_explored': 1, 'time_ms': 0}
        
        self.reset_stats()
        start_time = time.time()
        
        h_initial = self.manhattan_distance(initial_state)
        pq = [(h_initial, 0, initial_state)]
        g_costs = {initial_state: 0}
        parent = {initial_state: None}
        visited = set()
        
        while pq:
            f_cost, g_cost, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            self.nodes_explored += 1
            
            if current == self.goal_state:
                path = self.reconstruct_path(parent, initial_state, current)
                return path, {
                    'algorithm': 'A* (Manhattan)',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time_ms': (time.time() - start_time) * 1000
                }
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost + 1
                
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    parent[neighbor] = current
                    h_cost = self.manhattan_distance(neighbor)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(pq, (f_cost, tentative_g, neighbor))
        
        return None, {'algorithm': 'A* (Manhattan)', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def astar_misplaced(self, initial_state):
        """A* with misplaced tiles heuristic."""
        if initial_state == self.goal_state:
            return [initial_state], {'algorithm': 'A* (Misplaced)', 'path_length': 0, 
                                   'nodes_explored': 1, 'time_ms': 0}
        
        self.reset_stats()
        start_time = time.time()
        
        h_initial = self.misplaced_tiles(initial_state)
        pq = [(h_initial, 0, initial_state)]
        g_costs = {initial_state: 0}
        parent = {initial_state: None}
        visited = set()
        
        while pq:
            f_cost, g_cost, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            self.nodes_explored += 1
            
            if current == self.goal_state:
                path = self.reconstruct_path(parent, initial_state, current)
                return path, {
                    'algorithm': 'A* (Misplaced)',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time_ms': (time.time() - start_time) * 1000
                }
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost + 1
                
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    parent[neighbor] = current
                    h_cost = self.misplaced_tiles(neighbor)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(pq, (f_cost, tentative_g, neighbor))
        
        return None, {'algorithm': 'A* (Misplaced)', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def show_solution_steps(self, path, max_steps=6):
        """Show solution steps (limit for readability)."""
        if not path:
            print("❌ No solution found!")
            return
        
        print(f"\\n🎯 Solution in {len(path) - 1} moves:")
        show_count = min(len(path), max_steps)
        
        for i in range(show_count):
            print(f"\\nStep {i}:")
            self.print_puzzle(path[i])
            if i < show_count - 1:
                print("↓")
        
        if len(path) > max_steps:
            print(f"... (showing first {max_steps} steps of {len(path)})")

def run_demo():
    """Interactive demo for 8-puzzle algorithms."""
    print("🧩 8-Puzzle Search Algorithm Demo")
    print("=" * 40)
    
    # Test cases
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
        print(f"\\n🎯 Testing: {test_name}")
        print("Initial State:")
        searcher.print_puzzle(initial_state)
        print("Goal State:")
        searcher.print_puzzle(searcher.goal_state)
        
        print(f"\\n{'Algorithm':<15} {'Length':<8} {'Nodes':<8} {'Time(ms)':<10} {'Found'}")
        print("-" * 55)
        
        results = []
        
        for algo_name, algo_method in algorithms:
            try:
                path, stats = getattr(searcher, algo_method)(initial_state)
                found = "✅" if path else "❌"
                print(f"{algo_name:<15} {stats['path_length']:<8} {stats['nodes_explored']:<8} {stats['time_ms']:<10.2f} {found}")
                
                if path and len(path) <= 6:  # Show short solutions
                    results.append((algo_name, path))
                    
            except Exception as e:
                print(f"{algo_name:<15} {'Error':<8} {'-':<8} {'-':<10} ❌")
        
        # Show solution for first successful algorithm
        if results:
            print(f"\\n🏆 Sample solution ({results[0][0]}):")
            searcher.show_solution_steps(results[0][1])

if __name__ == "__main__":
    run_demo()
