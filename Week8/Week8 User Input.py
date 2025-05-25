# Disallowed characters 
disallowed_name_chars = set('!"@#$%^&*()_=+,<>/?;:{}[]\\')
disallowed_email_chars = set('!"\'#$%^&*()=+,<>/?;:{}[]\\')
disallowed_address_chars = set('!"\'@$%^&*_=+<>?;:{}[]')

# This function checks if a string contains any disallowed characters
def disallowed_characters(input_str, disallowed_set):
    return any(char in disallowed_set for char in input_str)

# Employee ID: must be a number with up to 7 digits
employee_id = input("Enter Employee ID (up to 7 digits): ")
if not (employee_id.isdigit() and len(employee_id) <= 7):
    print("Invalid ID. The ID must be a number with up to 7 digits.")
    exit()

# Employee Name
employee_name = input("Enter Employee Name: ")
if (not employee_name.replace(" ", "").isalpha() or
        disallowed_characters(employee_name, disallowed_name_chars)):
    print("Invalid Name.")
    exit()

# Employee Email Address
employee_email = input("Enter Employee Email Address: ")
if (not employee_email.replace(".", "").replace("@", "").isalnum() or
        disallowed_characters(employee_email, disallowed_email_chars)):
    print("Invalid Email Address.")
    exit()

# Optional Employee Address
employee_address = input("Enter Employee Address (optional): ").strip()
if employee_address:
    if (not employee_address.replace(" ", "").isalnum() or
            disallowed_characters(employee_address, disallowed_address_chars)):
        print("Invalid Address.")
        exit()

# Output
print(f"\nHello, {employee_name}. Your Employee ID is {employee_id}, and your email address is {employee_email}.")
if employee_address:
    print(f"Your address is {employee_address}.")
else:
    print("You did not provide an address.")
