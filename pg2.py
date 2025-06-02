# Defuzzification, Lambda cut method Define the fuzzy set as a dictionary where the keys are the elements and the values are their membership values
fuzzy_set = {'x': 4.5, 'y': 3.5, 'z':4.33}

# Define the lambda value for the cut
lambda_value = 4

# Perform the lambda cut
def lambda_cut(fuzzy_set, lambda_value):
    # Create a list to store the elements that satisfy the lambda-cut condition
    cut_set = []

    # Iterate through the fuzzy set
    for element, membership_value in fuzzy_set.items():
        if membership_value >= lambda_value:
            cut_set.append(element)

    return cut_set

# Get the resulting crisp set (elements with membership >= lambda_value)
result = lambda_cut(fuzzy_set, lambda_value)

# Output the result
print(f"Elements in the fuzzy set with membership >= {lambda_value}: {result}")

#Mean of maximum method
def mean_of_maximum(fuzzy_set):
    # Find the maximum membership value
    max_membership = max(fuzzy_set.values())

    # Get all x values where membership is maximum
    max_x_values = [x for x, mu in fuzzy_set.items() if mu == max_membership]

    # Compute the mean of these x values
    return sum(max_x_values) / len(max_x_values)

# Example fuzzy set (dictionary format: {x: membership_value})
fuzzy_set = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0, 5: 1.0, 6: 0.7, 7: 0.3}

# Compute MOM defuzzification
result = mean_of_maximum(fuzzy_set)

# Output the result
print(f"Mean of Maximum (MOM) defuzzified value: {result}")

def center_of_gravity(fuzzy_set):
    # Compute the numerator (sum of x * μ(x))
    numerator = sum(x * mu for x, mu in fuzzy_set.items())

    # Compute the denominator (sum of μ(x))
    denominator = sum(fuzzy_set.values())

    # Avoid division by zero
    return numerator / denominator if denominator != 0 else 0

# Example fuzzy set (dictionary format: {x: membership_value})
fuzzy_set = {1: 0.2, 2: 0.5, 3: 0.8, 4: 1.0, 5: 0.7}

# Compute COG defuzzification
result = center_of_gravity(fuzzy_set)

# Output the result
print(f"Center of Gravity (COG) defuzzified value: {result}")

