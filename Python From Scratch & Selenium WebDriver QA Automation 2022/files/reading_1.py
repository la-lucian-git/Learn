# DOT RECOMMENDED METHOD TO READ A FILE

sample_file = './programming_language_wikipedia.txt'

# Pointer will go to the end of the file, need to open and close each time
my_file = open(sample_file, 'r')
content_string = my_file.read()  # Return string
my_file.close()

my_file = open(sample_file, 'r')
content_line = my_file.readline()
my_file.close()

# Or use seek to point to the beginning of the file
my_new_file = open(sample_file, 'r')
content_1 = my_new_file.readline()
my_new_file.seek(0)
content_2 = my_new_file.readlines()
my_new_file.close()


print("")
print(type(content_string))
print(content_string)

print("")
print(type(content_line))
print(content_line)

print("")
print(type(content_1))
print(content_1)

print("")
print(type(content_2))
print(content_2)

