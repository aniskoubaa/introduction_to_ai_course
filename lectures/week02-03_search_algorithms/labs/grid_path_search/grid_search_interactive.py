# Grid Search Interactive Demo
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

class GridSearcher:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.nodes_explored = 0
        
    def reset_stats(self):
        self.nodes_explored = 0
    
    def is_valid(self, row, col):
        return (0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] == 0)
    
    def get_neighbors(self, pos):
        row, col = pos
        neighbors = []
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_row, new_col = row + dr, col + dc
            if self.is_valid(new_row, new_col):
                neighbors.append((new_row, new_col))
        return neighbors
    
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def reconstruct_path(self, parent, start, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = parent.get(current)
        path.reverse()
        return path
    
    def visualize(self, path=None):
        print("\\n📍 Grid: S=Start, G=Goal, █=Obstacle, .=Empty, *=Path")
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

    def bfs(self, start, goal):
        """BFS: Level-by-level exploration using queue."""
        self.reset_stats()
        start_time = time.time()
        
        queue = deque([start])
        visited = {start}
        parent = {start: None}
        
        while queue:
            current = queue.popleft()
            self.nodes_explored += 1
            
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                return path, {
                    'algorithm': 'BFS',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time_ms': (time.time() - start_time) * 1000
                }
            
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        return None, {'algorithm': 'BFS', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def dfs(self, start, goal, max_depth=50):
        """DFS: Depth-first exploration using stack."""
        self.reset_stats()
        start_time = time.time()
        
        stack = [(start, 0)]
        visited = {start}
        parent = {start: None}
        
        while stack:
            current, depth = stack.pop()
            self.nodes_explored += 1
            
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                return path, {
                    'algorithm': 'DFS',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time_ms': (time.time() - start_time) * 1000
                }
            
            if depth < max_depth:
                for neighbor in reversed(self.get_neighbors(current)):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = current
                        stack.append((neighbor, depth + 1))
        
        return None, {'algorithm': 'DFS', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def ucs(self, start, goal):
        """UCS: Uniform-cost search using priority queue."""
        self.reset_stats()
        start_time = time.time()
        
        pq = [(0, start)]
        costs = {start: 0}
        parent = {start: None}
        visited = set()
        
        while pq:
            current_cost, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)
            self.nodes_explored += 1
            
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                return path, {
                    'algorithm': 'UCS',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time_ms': (time.time() - start_time) * 1000
                }
            
            for neighbor in self.get_neighbors(current):
                new_cost = current_cost + 1
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parent[neighbor] = current
                    heapq.heappush(pq, (new_cost, neighbor))
        
        return None, {'algorithm': 'UCS', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

    def astar(self, start, goal):
        """A*: Heuristic-guided search using f(n) = g(n) + h(n)."""
        self.reset_stats()
        start_time = time.time()
        
        h_start = self.manhattan_distance(start, goal)
        pq = [(h_start, 0, start)]
        g_costs = {start: 0}
        parent = {start: None}
        visited = set()
        
        while pq:
            f_cost, g_cost, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            visited.add(current)
            self.nodes_explored += 1
            
            if current == goal:
                path = self.reconstruct_path(parent, start, goal)
                return path, {
                    'algorithm': 'A*',
                    'path_length': len(path) - 1,
                    'nodes_explored': self.nodes_explored,
                    'time_ms': (time.time() - start_time) * 1000
                }
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_cost + 1
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    parent[neighbor] = current
                    h_cost = self.manhattan_distance(neighbor, goal)
                    f_cost = tentative_g + h_cost
                    heapq.heappush(pq, (f_cost, tentative_g, neighbor))
        
        return None, {'algorithm': 'A*', 'path_length': -1, 
                      'nodes_explored': self.nodes_explored, 
                      'time_ms': (time.time() - start_time) * 1000}

def run_demo():
    """Interactive demo function for students and instructors."""
    print("🗺️ Grid Search Algorithm Demo")
    print("=" * 40)
    
    # Test grids
    simple_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    maze_grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    test_cases = [
        ("Simple 3x3", simple_grid, (0, 0), (2, 2)),
        ("Maze 5x5", maze_grid, (0, 0), (0, 4))
    ]
    
    for grid_name, grid, start, goal in test_cases:
        print(f"\\n🎯 Testing: {grid_name}")
        print(f"Start: {start} → Goal: {goal}")
        
        searcher = GridSearcher(grid)
        searcher.visualize()
        
        algorithms = ['bfs', 'dfs', 'ucs', 'astar']
        results = []
        
        for algo in algorithms:
            path, stats = getattr(searcher, algo)(start, goal)
            results.append((algo.upper(), path, stats))
        
        # Results table
        print(f"{'Algorithm':<8} {'Length':<8} {'Nodes':<8} {'Time(ms)':<10} {'Found'}")
        print("-" * 50)
        
        for algo, path, stats in results:
            found = "✅" if path else "❌"
            print(f"{algo:<8} {stats['path_length']:<8} {stats['nodes_explored']:<8} {stats['time_ms']:<10.2f} {found}")
        
        # Show best path
        for algo, path, stats in results:
            if path:
                print(f"\\n🏆 Solution by {algo}:")
                searcher.visualize(path)
                break

if __name__ == "__main__":
    run_demo()
