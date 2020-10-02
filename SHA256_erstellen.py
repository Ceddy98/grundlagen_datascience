from hashlib import sha256

eingabe = input("Text: ")
hashCode = sha256(eingabe.encode('utf-8'))
print("Hashcode: " + hashCode.hexdigest())
