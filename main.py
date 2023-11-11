import numpy as np


def calculate_probabilities(data, utilities):
    """
    Calculate probabilities for each alternative in a multinomial choice setting using the logistic function.

    Parameters:
    - parameters: A dictionary containing the β coefficients for each alternative.
    - data: A dictionary containing the independent variables for each alternative.
    - utilities: A list of functions defining the deterministic utilities for each alternative.

    Returns:
    - probabilities: A dictionary with keys representing each alternative and values as lists containing
      the calculated probabilities for each data point.
    """
    try:
        # Validate input dimensions
        num_alternatives = len(utilities)
        num_data_points = len(data[list(data.keys())[0]])

        if not all(len(data[var]) == num_data_points for var in data.keys()):
            raise ValueError("Mismatched dimensions between parameters and data points.")

        # Initialize probabilities dictionary
        calculated_probabilities = {f'P{i + 1}': [] for i in range(num_alternatives)}

        # Calculate probabilities for each alternative and data point
        for i in range(num_data_points):
            utilities_values = [utility(i) for utility in utilities]
            exp_utilities = np.exp(utilities_values)
            sum_exp_utilities = sum(exp_utilities)

            for j in range(num_alternatives):
                probability = exp_utilities[j] / sum_exp_utilities
                calculated_probabilities[f'P{j + 1}'].append(probability)

        return calculated_probabilities
    except Exception as er:
        raise ValueError(f"Error in calculate_probabilities: {str(er)}")


# the given sample parameters
parameters = {
    'β01': 0.1,
    'β1': 0.5,
    'β2': 0.5,
    'β02': 1,
    'β03': 0
}

# the given sample data
data = {
    'X1': [2, 3, 5, 7, 1, 8, 4, 5, 6, 7],
    'X2': [1, 5, 3, 8, 2, 7, 5, 9, 4, 2],
    'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Defining utilities functions
utilities = [
    lambda i: parameters['β01'] + parameters['β1'] * data['X1'][i] + parameters['β2'] * data['X2'][i],
    lambda i: parameters['β02'] + parameters['β1'] * data['X1'][i] + parameters['β2'] * data['X2'][i],
    lambda i: parameters['β03'] + parameters['β1'] * data['Sero'][i] + parameters['β2'] * data['Sero'][i]
]

try:
    # Calculating probabilities
    probabilities = calculate_probabilities(data, utilities)

    # Save the output in a .txt file
    with open('probabilities_output.txt', 'w') as f:
        f.write(str(probabilities))
except Exception as e:
    print(f"Error: {str(e)}")

############################ If we want the user to give prompt inputes, please uncomment the code below #############################


# def calculate_probabilities(data, utilities):
#     """
#     Calculate probabilities for each alternative in a multinomial choice setting using the logistic function.
#
#     Parameters:
#     - data: A dictionary containing the independent variables for each alternative.
#     - utilities: A list of functions defining the deterministic utilities for each alternative.
#
#     Returns:
#     - probabilities: A dictionary with keys representing each alternative and values as lists containing
#       the calculated probabilities for each data point.
#     """
#     try:
#         # Validate input dimensions
#         num_alternatives = len(utilities)
#         num_data_points = len(data[list(data.keys())[0]])
#
#         if not all(len(data[var]) == num_data_points for var in data.keys()):
#             raise ValueError("Mismatched dimensions between parameters and data points.")
#
#         # Initialize probabilities dictionary
#         calculated_probabilities = {f'P{i + 1}': [] for i in range(num_alternatives)}
#
#         # Calculate probabilities for each alternative and data point
#         for i in range(num_data_points):
#             utilities_values = [utility(i) for utility in utilities]
#             exp_utilities = np.exp(utilities_values)
#             sum_exp_utilities = sum(exp_utilities)
#
#             for j in range(num_alternatives):
#                 probability = exp_utilities[j] / sum_exp_utilities
#                 calculated_probabilities[f'P{j + 1}'].append(probability)
#
#         return calculated_probabilities
#     except Exception as er:
#         raise ValueError(f"Error in calculate_probabilities: {str(er)}")
#
#
# try:
#     # Taking user input for parameters
#     parameters = {}
#     num_params = int(input("Enter the number of parameters: "))
#     for i in range(1, num_params + 1):
#         param_name = input(f"Enter parameter {i} name: ")
#         param_value = float(input(f"Enter parameter {i} value: "))
#         parameters[param_name] = param_value
#
#     # Taking user input for data
#     num_data_keys = int(input("Enter the number of data keys: "))
#     num_data_points = int(input("Enter the number of data points: "))
#     data = {}
#     for key_index in range(1, num_data_keys + 1):
#         key_name = input(f"Enter data key {key_index} name: ")
#         data[key_name] = [float(input(f"Enter {key_name} for data point {j + 1}: ")) for j in range(num_data_points)]
#
#     # for key in data.keys():
#     #     data[key] = [float(input(f"Enter {key} for data point {j + 1}: ")) for j in range(num_data_points)]
#
#     # Defining utilities functions
#     utilities = [lambda i: parameters[key] * data[key][i] for key in parameters.keys()]
#
#     # Calculating probabilities
#     probabilities = calculate_probabilities(data, utilities)
#
#     # Save the output in a .txt file
#     with open('probabilities_output.txt', 'w') as f:
#         f.write(str(probabilities))
# except Exception as e:
#     print(f"Error: {str(e)}")
