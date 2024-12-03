def collect_user_info():
    """Function to collect basic user information."""
    print("Welcome! Please provide the following information:")

    # Collect user information
    name = input("Enter your full name: ").strip()
    age = input("Enter your age: ").strip()
    email = input("Enter your email address: ").strip()
    phone = input("Enter your phone number: ").strip()
    address = input("Enter your address: ").strip()

    # Store the information in a dictionary
    user_info = {
        "Name": name,
        "Age": age,
        "Email": email,
        "Phone": phone,
        "Address": address,
    }

    return user_info


def display_user_info(user_info):
    """Function to display collected user information."""
    print("\nThank you! Here's the information you provided:")
    for key, value in user_info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    user_info = collect_user_info()
    display_user_info(user_info)
