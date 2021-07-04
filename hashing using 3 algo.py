import hashlib


def hashing(str):
    hashed1 = hashlib.md5(str.encode())
    print(hashed1.hexdigest())


hashing(input("enter a string :"))


def hashing2(str):
    hashed2 = hashlib.sha1(str.encode())
    print(hashed2.hexdigest())


hashing2(input("enter a string :"))


def hashing3(str):
    hashed3 = hashlib.sha256(str.encode())
    print(hashed3.hexdigest())


hashing3(input("enter a string :"))
