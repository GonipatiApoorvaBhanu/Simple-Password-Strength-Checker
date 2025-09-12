import random
import string
def random_pass(length=15):
    characters=string.ascii_letters+string.digits+string.punctuation
    password="".join(random.choice(characters)for i in range (length))
    return password
print(random_pass())