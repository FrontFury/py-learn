first_name = 'Estiak Ahamed'
last_name = 'Tasin'
space = ' '
full_name = first_name + space + last_name

print(full_name)  # Estiak Ahamed Tasin

# Checking length of a string using len() builtin function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Using format()
first_name = 'Estiak Ahamed'
last_name = 'Tasin'
job = 'Web & Native Android Developer'
country = 'Bangladesh'

sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country
)

print(sentence)