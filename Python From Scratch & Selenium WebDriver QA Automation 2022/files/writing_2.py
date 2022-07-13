my_string = "I love to program in the Python language."

with open('./sample_output3.txt', 'w') as my_f:
    my_f.write(my_string)

my_list = ['user_1', 'user_2', 'user_3']
with open('./sample_output4.txt', 'w') as my_f:
    # my_f.write(my_list)  # write() can't handle lists
    # my_f.write(str(my_list))  # will write as a list in .txt file
    for i in my_list:
        my_f.write(i + '\n')

my_new_string = "Also love testing"

with open('./sample_output5.txt', 'a') as my_f:
    my_f.write(my_new_string + '\n')

my_langs = ['Python', 'Js', 'PHP', 'Java', 'Ruby']
with open('./my_fav.csv', 'w') as my_f:
    # my_f.writelines(my_langs)  # No list formatting but no new lines
    to_string = '\n'.join(my_langs)
    my_f.write(to_string)