# Task 2: Write and Append Data to a File

with open("output.txt", "a+") as fh:
    data_1 = input("Enter text to write to the file: ").strip()
    fh.write(f"\n{data_1}\n")
    print("Data successfully written to output.txt.\n")

    data_2 = input("Enter additional text to append: ").strip()
    print("Data successfully appended.\n")
    fh.write(data_2)

    # Move the cursor back to the start to read
    fh.seek(0)
    contents = fh.read()
    print(f"Final content of output.txt:\n{contents}")