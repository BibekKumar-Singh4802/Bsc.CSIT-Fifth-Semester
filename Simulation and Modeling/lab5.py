
# Lab Topic: Markov Chains Simulation – Weather Prediction
# This program predicts weather states using a Markov chain transition probability matrix.

import numpy as np
import matplotlib.pyplot as plt

class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.state_to_index = {state: i for i, state in enumerate(states)}

    def next_state(self, current_state):
        index = self.state_to_index[current_state]
        return np.random.choice(self.states, p=self.transition_matrix[index])

    def generate_states(self, start_state, num_steps):
        states = [start_state]
        current_state = start_state

        for _ in range(num_steps):
            next_s = self.next_state(current_state)
            states.append(next_s)
            current_state = next_s

        return states


# Weather states
weather_states = ["Sunny", "Rainy", "Cloudy"]

# Transition matrix (rows must sum to 1)
weather_transition_matrix = [
    [0.7, 0.2, 0.1],   # Sunny → Sunny, Rainy, Cloudy
    [0.3, 0.4, 0.3],   # Rainy → Sunny, Rainy, Cloudy
    [0.2, 0.5, 0.3]    # Cloudy → Sunny, Rainy, Cloudy
]

# Create Markov Chain object
weather_chain = MarkovChain(weather_transition_matrix, weather_states)

# User input
start_state = input("Enter the starting state (Sunny, Rainy, Cloudy): ").strip().capitalize()

if start_state not in weather_states:
    print("Invalid state! Please enter Sunny, Rainy, or Cloudy.")
    exit()

num_days = int(input("Enter the number of days to predict: "))

# Generate weather sequence
weather_sequence = weather_chain.generate_states(start_state, num_days)

# Print sequence
print("\nPredicted Weather Sequence:")
print(" -> ".join(weather_sequence))

# Count occurrences
state_counts = {state: weather_sequence.count(state) for state in weather_states}

print("\nState Occurrences:")
for state, count in state_counts.items():
    print(f"{state}: {count} times")


# ---------- Visualization 1 : Colored Bar Chart ----------
plt.figure(figsize=(8,5))

colors = ["gold", "skyblue", "lightgreen"]

plt.bar(state_counts.keys(), state_counts.values(), color=colors)

plt.xlabel("Weather State")
plt.ylabel("Occurrences")
plt.title("Weather State Frequency in Simulation - Bibek Singh")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


# ---------- Visualization 2 : Weather Transition Graph ----------
weather_state_index = {state: i for i, state in enumerate(weather_states)}
time_steps = list(range(len(weather_sequence)))
state_indices = [weather_state_index[state] for state in weather_sequence]

plt.figure(figsize=(8,5))

plt.plot(
    time_steps,
    state_indices,
    marker='o',
    linestyle='-',
    color='purple',
    linewidth=2
)

plt.xticks(time_steps)
plt.yticks(range(len(weather_states)), weather_states)

plt.xlabel("Days")
plt.ylabel("Weather State")
plt.title("Weather Transitions Over Time - Bibek Singh")

plt.grid(True)

plt.show()