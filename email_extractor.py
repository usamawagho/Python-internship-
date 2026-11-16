import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_dir, "input.txt")
output_file = os.path.join(base_dir, "extracted_emails.txt")

if not os.path.exists(input_file):
    with open(input_file, "w") as f:
        f.write("Hello team,\n")
        f.write("Contact alex.morgan@example.com or sarah_dev@company.org for updates.\n")
        f.write("Support email: support@service.io\n")
        f.write("Duplicate test: alex.morgan@example.com\n")

with open(input_file, "r") as f:
    text = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
unique_emails = list(dict.fromkeys(emails))

with open(output_file, "w") as f:
    for email in unique_emails:
        f.write(email + "\n")

print(f"Extracted {len(unique_emails)} email(s) into extracted_emails.txt.")