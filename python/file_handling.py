# Tasks and solutions
# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


#1 Create a file called text.txt and write at least five lines of text into it.
with open('text.txt', 'w') as file:
    file.write("Hello World\n")
    file.write("This is a test file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("We will process this file in Python.\n")
    file.write("Let's see how it works!\n")

#2 Write a Python script to:
# Read the contents of text.txt. 
try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        content = file.readlines()
        for i in range(len(content)):
            content[i] = content[i].strip()
            print(content[i])

    #3 Count the number of words in the file.
    word_count = sum(len(line.split()) for line in content)
    print("Word Count:", word_count)

    #4 Convert all text to uppercase.
    upper_content = [line.upper() for line in content]
    print("Uppercase Content:", upper_content)

    #5 Write the processed text and the word count to a new file called output.txt.
    output_filename = "output.txt"
    with open(output_filename, 'w') as file:
        file.writelines(upper_content)
        file.write(f"\nWord Count: {word_count}\n")

    #6. Print a success message once the new file is created.
    print(f"File processed successfully. Output written to {output_filename}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
