#!/usr/bin/python3
# Define the answers for each task
answers = {
    "8-answer.txt": "True\n",          # s1 == s2
    "9-answer.txt": "True\n",          # s1 is s2
    "10-answer.txt": "True\n",         # l1 == l2
    "11-answer.txt": "False\n",        # l1 is l2
    "12-answer.txt": "True\n",         # l1 == l2 (l1 and l2 are the same object)
    "13-answer.txt": "True\n",         # l1 is l2 (l1 and l2 are the same object)
    "14-answer.txt": "[1, 2, 3, 4]\n", # l2 points to l1, which was modified
    "15-answer.txt": "[1, 2, 3]\n",    # l2 remains unchanged because l1 now points to a new list
    "16-answer.txt": "1\n",            # Integers are immutable; 'a' remains 1
    "17-answer.txt": "[1, 2, 3, 4]\n", # l is modified in place by the function
    "18-answer.txt": "[1, 2, 3]\n",    # l1 is not modified because assignment in the function does not affect the original list
}

# Create files and write the corresponding answers
directory = "python-everything_is_object"

import os

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create the files with the answers
for filename, answer in answers.items():
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        f.write(answer)

print("Files created successfully!")
