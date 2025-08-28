import json

"""
A simple script to filter users from users.json by name, age, or email.
"""


def load_users():
    """
    Load all users from the users.json file.

    Returns:
        list: A list of user dictionaries loaded from the JSON file.
    """
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    return users


def filter_users_by_name(name):
    """
    Filter users by their name (case-insensitive).

    Args:
        name (str): The name to search for.

    Returns:
        list: A list of matching user dictionaries based on names.
        Returns an empty list if no matches.
    """
    users = load_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    return filtered_users


def filter_users_by_age(age):
    """
    Filter users by their age.

    Args:
        age (int): The age to search for.

    Returns:
        list: A list of matching user dictionaries based on age.
        Returns an empty list if no matches.
    """
    users = load_users()

    filtered_users = [user for user in users if user["age"] == age]
    return filtered_users


def filter_users_by_email(email):
    """
    Filter users by their email (case-insensitive).

    Args:
        email (str): The email to search for.

    Returns:
        list: A list of matching user dictionaries based on email.
        Returns an empty list if no matches.
    """
    users = load_users()

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]
    return filtered_users


def main():
    """
    Entry point for the program.

    Prompts the user to choose a filter option (name, age, or email),
    then asks for the corresponding value to filter users from the JSON file.
    It then prints out the filtered users or a message if no matches are found.
    """
    filter_option = (
        input(
            "What would you like to filter by?"
            "(Currently, only name, age and email is supported): "
        )
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        matched_users_name = filter_users_by_name(name_to_search)
        if not matched_users_name:
            print("No users with that name were found.")
        else:
            for user in matched_users_name:
                print(user)

    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        age_to_search = int(age_to_search)
        matched_users_age = filter_users_by_age(age_to_search)
        if not matched_users_age:
            print("No users with that age were found.")
        else:
            for user in matched_users_age:
                print(user)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        matched_users_email = filter_users_by_email(email_to_search)
        if not matched_users_email:
            print("No users with that email were found.")
        else:
            for user in matched_users_email:
                print(user)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
