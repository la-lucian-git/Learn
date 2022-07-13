def add_numbers(a, b):
    """
    Function return the sum of two numbers.

    :param a: <float/int>
    :param b: <float/int>
    :return: <float/int>
    """

    return a + b


def has_no_sales_tax(state):
    states_with_no_sales_tax = ["AK", "DE", "MT", "NH", "OR"]

    if state.upper() in states_with_no_sales_tax:
        return "NO"


def get_count_of_small_words(input_string, max_size=3):
    small_words = []
    for word in input_string.split():
        if len(word) <= max_size:
            small_words.append(word)

    return small_words


_sum = add_numbers(10, 3.5)
sale_tax = has_no_sales_tax("MT")

jk = "In Python hashtags are used to tell the computer a line is not worth reading.Much like social media."
num_small_list_3 = get_count_of_small_words(jk)
num_small_list_5 = get_count_of_small_words(jk, max_size=5)

print("")
print(_sum)

print("")
print(f"MT has to pay sales tax: {sale_tax}.")

print("")
print(len(num_small_list_3), num_small_list_3)

print("")
print(len(num_small_list_5), num_small_list_5)