def get_standard_competition_ranks(marks):
    sorted_marks = sorted(enumerate(marks), key=lambda x: -x[1])
    ranks = [0] * len(marks)
    current_rank = 1
    for i, (original_index, mark) in enumerate(sorted_marks):
        if i == 0 or mark != sorted_marks[i - 1][1]:
            current_rank = i + 1
        ranks[original_index] = current_rank
    return ranks

def parse_pasted_marks(raw_input):
    lines = raw_input.replace(',', '\n').splitlines()
    marks = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                marks.append(float(line))
            except ValueError:
                print(f"⚠️ Skipped invalid entry: '{line}'")
    return marks

def main():
    print("📋 Paste your marks below (one per line or comma-separated). Press Enter twice to finish:\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    raw_input = "\n".join(lines)

    marks = parse_pasted_marks(raw_input)

    if not marks:
        print("❌ No valid marks found.")
        return

    ranks = get_standard_competition_ranks(marks)

    print("\nMark\tRank")
    print("------------")
    for mark, rank in zip(marks, ranks):
        print(f"{mark}\t{rank}")

    # Ask if user wants only ranks
    choice = input("\n🔄 Do you want to copy only the ranks for pasting back into Excel? (y/n): ").strip().lower()
    if choice == 'y':
        print("\n📋 Copy the ranks below and paste into Excel:\n")
        for rank in ranks:
            print(rank)

if __name__ == "__main__":
    main()
