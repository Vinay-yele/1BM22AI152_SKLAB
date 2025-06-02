import numpy as np

R = {
    "Low Temp": [0.8, 0.5, 0.3],
    "Medium Temp": [0.6, 0.7, 0.4],
    "High Temp": [0.3, 0.6, 0.9]
}

# Fuzzy Relations for Humidity to Cooling (S(Y -> Z))
S = {
    "Dry": [0.7, 0.4, 0.3],        # Low Cooling, Medium Cooling, High Cooling
    "Normal": [0.5, 0.6, 0.4],
    "Humid": [0.2, 0.5, 0.8]
}

# Input values
temperature_input = "Low Temp"  # Low Temperature
humidity_input = "Dry"         # Dry Humidity

# Extract the relevant membership values for the given inputs
mu_R = R[temperature_input]  # Membership values for Low Temp
mu_S = S[humidity_input]     # Membership values for Dry Humidity

# Apply Min-Max Composition
def min_max_composition(mu_R, mu_S):
    # Initialize the result for the composed relation (Low Cooling, Medium Cooling, High Cooling)
    result = []

    # Perform Min-Max Composition for each cooling action (Low, Medium, High Cooling)
    for z in range(3):  # We have 3 cooling actions
        # Take the minimum of the corresponding values from R and S
        min_value = min(mu_R[0], mu_S[0]) if z == 0 else \
                    min(mu_R[1], mu_S[1]) if z == 1 else \
                    min(mu_R[2], mu_S[2])
        result.append(min_value)

    return result

# Calculate the final result for Low Temp and Dry Humidity
composed_result = min_max_composition(mu_R, mu_S)

# Find the maximum membership value to determine the cooling action
cooling_action = ["Low Cooling", "Medium Cooling", "High Cooling"]
max_membership_value = max(composed_result)
action_index = composed_result.index(max_membership_value)

# Output the results
print(f"Input: Temperature = {temperature_input}, Humidity = {humidity_input}")
print(f"Membership values for Cooling Actions: {composed_result}")
print(f"The system selects: {cooling_action[action_index]} with a membership value of {max_membership_value:.2f}")
