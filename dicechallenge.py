def calculate_total_combinations():
    number_of_faces_die_a = 6
    number_of_faces_die_b = 6
    total_combinations = number_of_faces_die_a * number_of_faces_die_b
    return total_combinations

def calculate_combination_distribution():
    distribution_list = [
        [{'Die A': i, 'Die B': j, 'Sum': i + j} for j in range(1, 7)] for i in range(1, 7)
    ]
    return distribution_list

def calculate_sum_probability():
    sides = 6
    total_combinations = sides ** 2
    probability_map = {}

    for i in range(2, 13):
        count = 0
        for j in range(1, sides + 1):
            if i - j <= sides and i - j >= 1:
                count += 1
        probability_map[i] = f"{count}/{total_combinations}"

    return probability_map

def main():
    # Calculate and display total combinations
    total_combinations = calculate_total_combinations()
    print("Total Combinations:", total_combinations)

    # Calculate and display combination distribution
    combination_distribution = calculate_combination_distribution()
    print("\nCombination Distribution:")
    for row in combination_distribution:
        for combo_map in row:
            print(combo_map)

    # Calculate and display sum probabilities
    sum_probabilities = calculate_sum_probability()
    print("\nProbability of Sums:")
    for sum_value, prob in sum_probabilities.items():
        print(f"P(Sum = {sum_value}): {prob}")

if __name__ == "__main__":
    main()
