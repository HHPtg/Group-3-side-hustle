import random, string
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=15))
print(password)