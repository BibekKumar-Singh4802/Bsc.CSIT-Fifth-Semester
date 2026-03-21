# lab5
import numpy as np
import matplotlib.pyplot as plt

class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.n_states = len(states)

    def next_state(self, current_state):
        return np.random.choice(
            self.states,
            p=self.transition_matrix[self.states.index(current_state)]
        )

    def generate_states(self, current_state, n_steps):
        states = [current_state]
        for _ in range(n_steps):
            next_state = self.next_state(current_state)
            states.append(next_state)
            current_state = next_state
        return states


# Define transition matrix
weather_transition_matrix = [
    [0.7, 0.2, 0.1],  # Sunny
    [0.3, 0.6, 0.1],  # Rainy
    [0.2, 0.3, 0.5]   # Cloudy
]

weather_states = ["Sunny", "Rainy", "Cloudy"]

# Create Markov Chain
weather_chain = MarkovChain(weather_transition_matrix, weather_states)

# User input
start_state = input("Enter the starting state (Sunny/Rainy/Cloudy): ")
num_days = int(input("Enter the number of days to predict: "))

# Generate sequence
weather_sequence = weather_chain.generate_states(start_state, num_days)

# Output sequence
print("\nPredicted Weather Sequence:")
print(" -> ".join(weather_sequence))

# Count occurrences
state_counts = {state: weather_sequence.count(state) for state in weather_states}

print("\nState Occurrences in Simulation:")
for state, count in state_counts.items():
    print(f"{state}: {count} times")


# ----------- VISUALIZATION (SEPARATE FOR EASY SCREENSHOT) -----------

# 1️⃣ Bar Chart - Weather State Frequency
plt.figure(figsize=(6, 5))

plt.bar(
    state_counts.keys(),
    state_counts.values(),
    color=['gold', 'blue', 'gray'],
    edgecolor='black'
)

plt.xlabel("Weather State")
plt.ylabel("Occurrences")
plt.title("Weather State Frequency in Simulation")

plt.tight_layout()
plt.show()   # FIRST GRAPH


# 2️⃣ Line Graph - Weather Transitions Over Time
plt.figure(figsize=(6, 5))

time_steps = list(range(len(weather_sequence)))
state_indices = [weather_states.index(state) for state in weather_sequence]

plt.plot(
    time_steps,
    state_indices,
    marker='o',
    linestyle='-',
    color='green',
    markerfacecolor='red',
    markersize=8
)

plt.yticks(range(len(weather_states)), weather_states)
plt.xlabel("Time Steps (Days)")
plt.ylabel("Weather State")
plt.title("Weather Transitions Over Time")

plt.tight_layout()
plt.show()   # SECOND GRAPH
