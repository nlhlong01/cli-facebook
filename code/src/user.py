from post import Post


class User:
    """Represents a user in the social network
    Requires a full name, a username, and a password

    """

    def __init__(self, fullname, username, pw_hash):
        self._fullname = fullname
        self._username = username
        # TODO: use a different data structure to store password
        self._pw_hash = pw_hash
        self._salt = pw_hash[32:]
        self._friends = []
        # Joined group
        self._groups = []
        # Post created by this user
        self._posts = []
        print(f'User created {self._fullname} ({self._username})')

    def __dir__(self):
        return ['_fullname', '_username']

    def get_fullname(self):
        return self._fullname

    def get_username(self):
        return self._username

    def get_pw_hash(self):
        return self._pw_hash

    def get_salt(self):
        return self._salt 

    def add_friend(self, user):
        # Checks if the friend has been added.
        try:
            self._friends.index(user)
        except ValueError:
            self._friends.append(user)
            # Also adds this user to the friend list of the just added friend
            user.add_friend(self)

    def get_friends(self):
        return self._friends

    def join_group(self, group):
        try:
            self._groups.index(group)
        except ValueError:
            self._groups.append(group)
            group.add_member(self)

    def get_groups(self):
        return self._groups

    def create_post(self, content, group=None):
        new_post = Post(self, content, group=group)
        if group is None:
            self._posts.append(new_post)
        else:
            group.add_post(new_post)
        return new_post

    def get_posts(self):
        return self._posts
