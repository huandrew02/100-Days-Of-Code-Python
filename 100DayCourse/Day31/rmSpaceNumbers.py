def process_line(line):
    # Split the line into words
    words = line.split()

    # Extract Korean words by removing numbers and joining the remaining parts
    korean_words = [word for word in words if not any(c.isdigit() for c in word)]
    
    # Return each Korean word on a new line
    return "\n".join(korean_words) + "\n"

def main(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        processed_lines = [process_line(line) for line in lines]

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(processed_lines)

        print("Processing complete. Result saved to", output_filename)

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    input_file_name = "100DayCourse/Day31/ko_full.txt"  # Change this to the name of your input file
    output_file_name = "100DayCourse/Day31/output.txt"  # Change this to the name you want for the output file
    main(input_file_name, output_file_name)
