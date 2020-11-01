# # Simple ReLU
# inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

# output = []
# for i in inputs:
#     # if i > 0:
#     #     output.append(i)
#     # else:
#     #     output.append(0)
#     output.append(max(0, i))


# print(output)


# # In NumPY
# import numpy as np

# inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
# output = np.maximum(0, inputs)
# print(output)


# # Softmax
# # Values from the previous output when we described
# # what a neural network is
# layer_outputs = [4.8, 1.21, 2.385]

# # e - mathematical constant, we use E here to match a common coding
# # style where constants are uppercased
# E = 2.71828182846  # you can also use math.e

# # For each value in a vector, calculate the exponential value
# exp_values = []
# for output in layer_outputs:
#     exp_values.append(E ** output)  # ** - power operator in Python
# print("exponentiated values:")
# print(exp_values)

# # Now normalize values
# norm_base = sum(exp_values)  # We sum all values
# norm_values = []
# for value in exp_values:
#     norm_values.append(value / norm_base)
# print("Normalized exponentiated values:")
# print(norm_values)

# print("Sum of normalized values:", sum(norm_values))


# # And in NumPy
# import numpy as np

# # Values from the earlier previous when we described
# # what a neural network is

# layer_outputs = [4.8, 1.21, 2.385]

# # For each value in a vector, calculate the exponential value
# exp_values = np.exp(layer_outputs)
# print("exponentiated values:")
# print(exp_values)

# # Now normalize values
# norm_values = exp_values / np.sum(exp_values)
# print("normalized exponentiated values:")
# print(norm_values)
# print("sum of normalized values:", np.sum(norm_values))


# Axis and keepdims
import numpy as np

layer_outputs = np.array([[4.8, 1.21, 2.385], [8.9, -1.81, 0.2], [1.41, 1.051, 0.026]])

print("Sum without axis")
print(np.sum(layer_outputs))

print("This will be identical to the above since default is None:")
print(np.sum(layer_outputs, axis=None))

print("Another way to think of it w/ a matrix == axis 0: columns:")
print(np.sum(layer_outputs, axis=0))

print("But we want to sum the rows instead, like this w/ raw py:")
for i in layer_outputs:
    print(sum(i))

print("So we can sum axis 1, but note the current shape:")
print(np.sum(layer_outputs, axis=1))

print("Sum axis 1, but keep the same dimensions as input:")
print(np.sum(layer_outputs, axis=1, keepdims=True))
