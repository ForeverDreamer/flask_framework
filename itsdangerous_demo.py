import os
from itsdangerous.serializer import Serializer

SECRET_KEY = 'base64 encoded random bytes'
s = Serializer(SECRET_KEY)
print(dir(s))
