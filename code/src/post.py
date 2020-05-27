from datetime import datetime


class Post:
    """Represents a text post on user's newsfeed.

    If argument group=None, the post is created as the owner's own post.
    Otherwise, it is created in the specified group.

    """

    def __init__(self, owner, content='', group=None):
        # TODO: Since the post is always created from the User object,
        # it may be not necessary to specify the post owner.
        self._owner = owner
        self._content = content
        self._group = group
        self._date_created = datetime.now()
        print('Post created')

    def get_owner(self):
        return self._owner

    def get_content(self):
        return self._content

    def get_date_created(self):
        return self._date_created

    def display(self):
        fullname = self._owner.get_fullname()
        username = self._owner.get_username()

        print('')
        if self._group is not None:
            print(f'From {fullname} ({username}) in {self._group.get_name()}:')
        else:
            print(f'From {fullname} ({username})')
        print(self._date_created)
        print(self._content)
        print('')
