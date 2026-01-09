# Reading .txt file

file = open("log.txt", "r")
content = file.read()             # Not a good Practice
print(content)
file.close()

# Best Practice (always use with)

with open("log.txt", "r") as file:  #✅ Automatically closes file , ✅ Cleaner & safer
    content = file.read()
    print(content)                  # usecase : File is small, You need full content at once

# Read line by line (Log-file style)

with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())    

# Usecases
#     File is large
#     Logs, ETL, streaming
#     Counting errors, words, patterns          

# Count number of lines

with open("log.txt", "r") as file:
    lines = file.readlines()
    print("Total lines:", len(lines))      

# Count number of words  

word_count = 0

with open("log.txt", "r") as file:
    for line in file:
        words = line.split()
        word_count += len(words)

print("Total Words:", word_count)

# Write in txt file

with open("output.txt", "a") as file:
    file.write("Hello Python using append 'a'\n")
    file.write("Learning Python file writing using append 'a'\n")


