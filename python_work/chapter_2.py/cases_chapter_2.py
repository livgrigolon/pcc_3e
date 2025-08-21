# Capítulo 2 - 16 de agosto de 2025
# 2.1
message = "Simple message!"
print(message)

# 2.2
message = "Simple message!"
print(message)

message = "Simple messages!"
print(message)

# 2.3
name = 'eric'
name = name.title()
print(f'Olá {name}, gostaria de aprender um pouco de Python hoje?')

# 2.4
name = 'eric'
name_lower = name.lower()
name_upper = name.upper()
name_title = name.title()
print(f'{name_lower} { name_upper} {name_title}')

# 2.5
quotes = 'Follow the path of the unsafe, independent thinker. Expose your ideas to the danger of controversy. Speak your mind and fear less the label of crackpot than the stigma of conformity.'
author = 'Thomas J. Watson'
print(f'{author} disse uma vez: "{quotes}"')

# 2.6
quotes_1 = 'Everything in the world began with a yes. One molecule said yes to another molecule and life was born.'
famous_person = 'Clarice Lispector'
message = f'{author} disse uma vez: "{quotes}"'
print(message)

# 2.7
person_name = '\n\t  Lívia '
print(person_name)
print(person_name.rstrip())
print(person_name.lstrip())
print(person_name.strip())

# 2.8
file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))

# 2.9 
print(5+3)
print(10-2)
print(4*2)
print(16/2)

# 2.10
favorite_number = 5
print(f'Seu número favorito é: {favorite_number}')

# 2.11 - Comentários


# 2.12
import this
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''