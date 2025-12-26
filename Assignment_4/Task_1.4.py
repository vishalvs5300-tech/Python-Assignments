# Task 1: Read a File and Handle Errors

try:
    with open("sample.txtt", "rt") as fh:
        line_1 = fh.readline().rstrip()
        line_2 = fh.readline()
     
        print("Reading file content:")
        print(f"Line 1: {line_1}")
        print(f"Line 2: {line_2}")

# If file doesn't exist:
except FileNotFoundError:
    print("Error: The file sample.txt was not found.")