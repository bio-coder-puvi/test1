# file_handling_example.py

# Step 1: Write data to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("Data written to file.")

# Step 2: Read and print the data
with open("sample.txt", "r") as file:
    content = file.read()

print("\nContent of the file:")
print(content)

# Step 3: Append new data to the file
with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")

print("\nNew data appended to the file.")

# Step 4: Read again to verify
with open("sample.txt", "r") as file:
    updated_content = file.read()

print("\nUpdated content of the file:")
print(updated_content)
