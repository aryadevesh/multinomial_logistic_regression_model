# multinomial_logistic_regression_model
The Python code properly implements the Mulinomial Logisic Regression Model 

**Report**

Introduction: 
The task was to develop a Python function capable of calculating the probability of each alternative in a multinomial choice setting using the logistic function. In a multinomial logit model, the probability of each alternative is determined by a logistic function, where the utility for each alternative is derived from a linear combination of independent variables and their respective coefficients.

Assumptions:
1. The function assumes that the input parameters and data are structured as dictionaries, making it easy to associate coefficients with independent variables.
2. The code assumes that the utility functions provided are correctly formulated like the way it is done in the code, and compatible with the data because of the critical role of the utility functions. 
3. We can also make one other function that can convert given Utility formulas into calculative equations using split(), replace(), and eval functions. 
4. As the data size is large so, I have put the inputs as hardcoded in the working code, but I have also provided the code which is the user in the prompt for all the Inputs. I have not used that code because the keys might have errors that do not match with the utility functions.  

Function Overview:
The `calculate_probabilities()` function takes three main inputs:
- `parameters`: A dictionary containing coefficients for each alternative.
- `data`: A dictionary containing independent variables for each alternative.
- `utilities`: A list of utility functions defining the deterministic utilities for each alternative.
The output is a dictionary, `probabilities`, where keys represent each alternative, and values are lists containing the calculated probabilities for each data point.


Error Handling: 
The code includes error handling to ensure that the dimensions of the input parameters and data match. If there is a mismatch, a `ValueError` is raised, providing a clear indication of the issue.
Additionally, a try-except block is implemented to catch any unforeseen errors during the execution of the `calculate_probabilities` function and the main code. This helps in identifying and addressing issues that might arise during execution.

Visualizations:
The code itself does not include visualizations, as it is primarily a utility function. However, when applying this function to real-world scenarios, it would be beneficial to visualize the calculated probabilities for each alternative over the dataset. This could be done using appropriate plotting libraries like Matplotlib or Boxplot.
For Example:  
 

Findings:
1. The code successfully implements the multinomial choice probability calculation using the logistic function.   
2. The error handling mechanisms ensure that the function handles potential issues, such as dimension mismatches, in a robust manner.
3. The provided example demonstrates the application of the function to a specific scenario with three alternatives and three independent variables. This showcases the flexibility of the function to handle different scenarios with varying numbers of alternatives and independent variables.


Conclusion:
The developed Python function serves its purpose of calculating multinomial choice probabilities using the logistic function. Its generic nature makes it adaptable to different scenarios with varying numbers of alternatives and independent variables. Further, the error-handling mechanisms enhance the reliability of the function in handling potential issues.
