from user import User
from group import Group
import utils


class Store():
    """The simple storage for all public information of the social network:

    1. Registered users.
    2. Created groups.
    3. Currently logged-in user.

    """
    _users = []
    _groups = []
    _current_user = None

    def __dir__(self):
        return ['_users', '_groups']

    # Get all users from the database
    def get_users(self):
        return self._users

    # Find a user given his/her username
    def get_user(self, username):
        for user in self._users:
            if username == user.get_username():
                return user
        return None

    def get_groups(self):
        return self._groups

    def get_group(self, name):
        for group in self._groups:
            if name == group.get_name():
                return group
        return None

    # Create new user in the database.
    # Called when a new user is registered.
    def create_user(self, fullname, username, plain_password):
        pw_hash_salt = utils.generate_pw_hash(plain_password)
        new_user = User(fullname, username, pw_hash_salt)
        self.get_users().append(new_user)
        return new_user

    # Called when a user creates a group
    def create_group(self, name):
        new_group = Group(name)
        self.get_groups().append(new_group)
        return new_group

    # Called when user log in/out
    def set_current_user(self, user):
        self._current_user = user

    def get_current_user(self):
        return self._current_user
