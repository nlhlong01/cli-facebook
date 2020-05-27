class Group():
    """A group where people can become members and post discussions.
    The posts are shared on newsfeed of every member.

    """

    def __init__(self, name):
        self._name = name
        self._members = []
        self._posts = []
        print(f'Group {self._name} created')

    def get_members(self):
        return self._members

    # Called when a user join this club from his/her account.
    # His/her data will be added to the group database as well.
    def add_member(self, user):
        self._members.append(user)

    def get_name(self):
        return self._name

    # Called when a post is created in a user's account.
    # TODO: This feature is not yet developed.
    def add_post(self, post):
        self._posts.append(post)

    def get_posts(self):
        return self._posts
