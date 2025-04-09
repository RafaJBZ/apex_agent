import numpy as np

# Environment Setup
class GridWorld:
    def __init__(self, height=4, width=4):
        self.height = height
        self.width = width
        
        # Define rewards
        self.rewards = np.zeros((height, width))
        self.rewards[3, 2] = 1       # High reward at [3,2]
        self.rewards[2, 2] = -0.04   # Small negative reward at [2,2]
        self.rewards[3, 3] = -0.1    # Larger negative reward at [3,3]
        
        # Define actions: 8 king moves + NOP
        # Format: [row_delta, col_delta]
        self.actions = [
            [0, 0],    # NOP - stay in place
            [-1, 0],   # Up
            [-1, 1],   # Up-Right
            [0, 1],    # Right
            [1, 1],    # Down-Right
            [1, 0],    # Down
            [1, -1],   # Down-Left
            [0, -1],   # Left
            [-1, -1]   # Up-Left
        ]
        
        # Action names for visualization
        self.action_names = ['NOP', 'Up', 'UpRight', 'Right', 'DownRight', 'Down', 'DownLeft', 'Left', 'UpLeft']
        
    def get_next_state(self, state, action):
        """Determine next state given current state and action"""
        row, col = state
        delta_row, delta_col = self.actions[action]
        
        # Calculate new position
        new_row = max(0, min(self.height - 1, row + delta_row))
        new_col = max(0, min(self.width - 1, col + delta_col))
        
        return (new_row, new_col)
    
    def get_reward(self, state):
        """Get reward for being in a state"""
        row, col = state
        return self.rewards[row, col]
    
    def get_random_state(self):
        """Get a random starting state"""
        row = np.random.randint(0, self.height)
        col = np.random.randint(0, self.width)
        return (row, col)