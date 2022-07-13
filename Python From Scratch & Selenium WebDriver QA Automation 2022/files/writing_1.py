my_string = "I love to program in the Python language."

my_f = open('./sample_output1.txt', 'w')  # Will overwrite the file
my_f.write(my_string)  # No new line
my_f.write(my_string)
my_f.write(my_string)
my_f.close()

my_f = open('./sample_output2.txt', 'w')  # Will overwrite the file
my_f.write(my_string)  # No new line
my_f.write('\n')
my_f.write(my_string)
my_f.write('\n')
my_f.write(my_string)
my_f.close()
