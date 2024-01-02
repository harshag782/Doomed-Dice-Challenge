# Initial dice configurations
A_die = [1, 2, 3, 4, 5, 6]
B_die = [1, 2, 3, 4, 5, 6]

# Create duplicates of dice for transformation
New_Die_A = A_die[:]
New_Die_B = B_die[:]

# Transformation logic for New_Die_A
for i in range(len(New_Die_A)):
    # Replace values greater than 4 with the lowest values in New_Die_A
    if New_Die_A[i] > 4:
        min_value = min(New_Die_A)
        New_Die_A[i] = min_value

# Transformation logic for New_Die_B
for i in range(len(New_Die_B)):
    # Replace values with sequential values from 1 to 6 in New_Die_B
    New_Die_B[i] = (i % 6) + 1

# Display the results
print("Original Die_A:", A_die)
print("Original Die_B:", B_die)
print("Modified Die_A:", New_Die_A)
print("Modified Die_B:", New_Die_B)
