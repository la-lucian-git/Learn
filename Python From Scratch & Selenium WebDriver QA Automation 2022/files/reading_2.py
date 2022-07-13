sample_file = './programming_language_wikipedia.txt'
country_file = './list_of_countries_with_no_comma.txt'

with open(sample_file, 'r') as f:
    content = f.read()

with open(country_file, 'r') as f:
    country_content = f.read()

print("")
print(content)

print("")
print(country_content)

split_country_content = country_content.split('\n')

print("")
print(split_country_content)