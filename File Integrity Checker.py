import hashlib

def get_file_hash(filename):
  with open(filename, 'rb') as f:
    content = f.read()
    hash_value = hashlib.sha256(content).hexdigest()
  return hash_value

def check_integrity(filename, stored_hash):
  current_hash = get_file_hash(filename) # Calculate current hash
  if current_hash == stored_hash:
    print("File is SAFE - No changes detected")
    return True
  else:
    print("WARNING: File has been MODIFIED!")
    return False

with open ('test_file.txt', 'w') as f:
  f.write("This is a test file for integrity checking")

orignal_hash = get_file_hash('test_file.txt')
print("Stored Hash:" , orignal_hash)

check_integrity('test_file.txt', orignal_hash)

