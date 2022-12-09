import sys

from app.users.models import User


def create_dummy_users_command():
    """Create dummy users"""

    users_exist = User.query.count()
    if users_exist:
        sys.stdout.write("create_dummy_users(): Users already exist \n")
        return

    users = [
        {
            "firstname": "John",
            "lastname": "Doe",
            "email": "johndoe@example.com",
            "password": "password",
        },
        {
            "firstname": "Jane",
            "lastname": "Doe",
            "email": "janedoe@example.com",
            "password": "password",
        },
    ]

    admin = {
        "firstname": "Admin",
        "lastname": "User",
        "email": "adminuser@example.com",
        "password": "password",
    }

    # create admin user
    admin_user = User(**admin)
    admin_user.save()
    admin_user.set_role("ADMIN")

    # create dummy users
    for user in users:
        reg_user = User(**user)
        reg_user.save()

    sys.stdout.write("create_dummy_users(): Users created \n")