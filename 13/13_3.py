print("="*40)
print("Q-1")
print("="*40)

import uuid
"""
random_uuid = uuid.uuid4()

print(f"Random UUID: {random_uuid}")

name = "Example.com"

named_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, name)
print(f"named_uuid: {named_uuid}")
"""

print("="*40)
print("Q-2")
print("="*40)
"""
student_ids = ["S101", "S102", "S103", "S104", "S105"]
student_dict = {}

for s_id in student_ids:
    student_dict[s_id] = uuid.uuid4()

print("Student Database:", student_dict)
"""

print("="*40)
print("Q-3")
print("="*40)

uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

if uuid1 == uuid2:
    print("UUIDs are equal.")
else:
    print("UUIDs are not equal.")