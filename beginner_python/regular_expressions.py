import re


# pattern = r'hello \d or \s'
# text = 'hello world!'

# match = re.search(pattern, text)
# print(match.group())


# ================ pattern


# pattern = r'hello'
# pattern = re.compile(pattern)

# text = 'meoew hello world!'

# match = pattern.search(text)

# print(pattern.match(text))



# ============= match and search

# pattern = r"bar"
# string = "foo bar baz"

# # Using match method
# match_obj = re.match(pattern, string)
# if match_obj:
#     print(match_obj)
#     print("Match found using match method")
# else:
#     print("Match not found using match method")

# # Using search method
# match_obj = re.search(pattern, string)
# if match_obj:
#     print(match_obj)
#     print("Match found using search method")
# else:
#     print("Match not found using search method")
    

# # ============= re.findall()

# pattern = r"bar"
# string = "foo bar bar baz"

# # Using match method
# match_obj = re.findall(pattern, string)
# if match_obj:
#     print(match_obj)
#     print("Match found using findall method")
# else:
#     print("Match not found using findall method")

# # Using search method
# match_obj = re.search(pattern, string)
# if match_obj:
#     print(match_obj)
#     print(match_obj.group())
#     print("Match found using search method")
# else:
#     print("Match not found using search method")


# ============= re.sub(), re.split()

# pattern = r"bar"
# string = "foo bar bar baz"


# match_obj = re.sub(pattern, '123', string)
# match_obj_split = re.split(pattern, string)

# print(match_obj, match_obj_split)

# =========== \d

# pattern = re.compile(r'\d{1,}')
# text = 'a2csjdflkdjf2423'

# match = pattern.findall(text)
# print(match)

# =========== \D, . -, [^abc2], [a-z], \W - 

# pattern = re.compile(r'\s')
# text = 'color colour'

# match = pattern.findall(text)
# print(match)

# () -> readibility, ?<Year> <?Month>, ^$

# pattern = re.compile(r'^acv$')
# text = 'acv sdfsdf acv'

# match = pattern.findall(text)
# print(match)


texts = [
    'john.doe@example.com',
    'jane_doe@example.co.uk',
    'invalid_email@.com'
]

pattern = re.compile(r'^[a-zA-Z0-9._%+-]{3,}@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$')

for text in texts:
    match = re.match(pattern, text)
    if match:
        print(match.group())
    else:
        print('There is no match!')
