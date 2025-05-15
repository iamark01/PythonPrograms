import random
import string

characters = string.ascii_letters + string.digits
captcha_code = ' '.join(random.choice(characters) for i in range(6))

print("Generated Captcha: ",captcha_code)
