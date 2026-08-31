print("="*40)
print("Q-1")
print("="*40)

import uuid

random_uuid = uuid.uuid4()

print(f"Random UUID: {random_uuid}")

name = "Example.com"

named_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, name)
print(f"named_uuid: {named_uuid}")

print("="*40)
print("Q-2")
print("="*40)