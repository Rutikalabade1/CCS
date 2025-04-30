import hashlib
msg=input("Enter the message::")
sha1_hash = hashlib.sha1(msg.encode()).hexdigest()
print("sha1 hash for", msg, ":", sha1_hash)