from hashlib import blake2b
items = [b'hello', b' ', b'world']
h = blake2b()
for item in items:
    h.update(item)
print(h.hexdigest())

