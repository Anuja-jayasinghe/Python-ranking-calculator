def get_standard_competition_ranks(marks):
    # Step 1: Sort marks in descending order with original index
    sorted_marks = sorted(enumerate(marks), key=lambda x: -x[1])
    
    ranks = [0] * len(marks)  # To hold the final ranks
    current_rank = 1

    for i, (original_index, mark) in enumerate(sorted_marks):
        if i == 0 or mark != sorted_marks[i - 1][1]:
            current_rank = i + 1
        ranks[original_index] = current_rank

    return ranks

def main():
    # Step 2: CLI input
    user_input = input("Enter marks separated by commas (e.g., 83.3, 96.6, 87.5, 87.5, 85.0):\n")
    try:
        marks = [float(x.strip()) for x in user_input.split(',')]
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")
        return

    ranks = get_standard_competition_ranks(marks)

    print("\nMark\tRank")
    print("------------")
    for mark, rank in zip(marks, ranks):
        print(f"{mark}\t{rank}")

if __name__ == "__main__":
    main()


