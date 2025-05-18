
import re


# Validators
def is_valid_name(name):
    """
    """
    return bool(re.match(r"^[a-zA-Z\s'-]+$", name))

def is_valid_phone_number(phonenumber):
    """
    """
    return bool(re.match(r"^[\d\s()+-]+$", phonenumber))

def is_valid_email(email):
    """
    """
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))


# Booking Function
def book_client():
    client_name = input("enter client name:")
    while not is_valid_name(client_name):
            print("invalid name.please try again")
            client_name = input("enter client name:")

    client_number = input("enter phonenumber:")
 
    while not is_valid_phone_number(client_number):
            print("invalid phonenumber.Please try again")
            client_number = input("Enter phone number: ")

    client_email = input("enter client emailaddress:")
    while not is_valid_email(client_email):
            print("invalid email.Please try again")
            client_email = input("Enter client's email address: ")
            
    print(f"Client name: {client_name}")
    print(f"Phone number: {client_number}")
    print(f"Email: {client_email}")


if __name__ == "__main__":
    book_client()
    


