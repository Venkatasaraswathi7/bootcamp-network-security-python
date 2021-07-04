import hashlib
def hashing(str):
      hashed = hashlib.md5((str).encode())
      print(hashed.hexdigest())
hashing("enter a string :")
