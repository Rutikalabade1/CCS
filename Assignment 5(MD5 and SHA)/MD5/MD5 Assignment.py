import hashlib
msg=input("Enter the message::")
md5_hash = hashlib.md5(msg.encode()).hexdigest()
print("MD5 hash for", msg, ":", md5_hash)