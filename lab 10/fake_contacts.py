import csv
from faker import Faker
from random import choice

fake = Faker()
filename = "huge_contacts.csv"

num_rows = 1_00
prefixes = ["705", "777", "707", "771", "708", "775"]

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["names", "phone_numbers"])

    for _ in range(num_rows):
        name = fake.first_name().lower()
        phone = fake.phone_number().replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace('.', "").replace("x", "").replace("+", "")
        print(phone)
        if not phone.startswith("+"):
            phone = "+7" + choice(prefixes) + phone[:7]
        writer.writerow([name, phone])

print(f"{num_rows} rows written to {filename}")
