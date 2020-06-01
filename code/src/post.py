from datetime import datetime


class Post:
    """Represents a text post on user's newsfeed.

    If argument group=None, the post is created as the owner's own post.
    Otherwise, it is created in the specified group.

    """

    def __init__(self, content, group=None):
        self._content = content
        self._group = group
        self._date = datetime.now()
        self._owner = None
        print('Post created')
    
    def __dir__(self):
        return ['_content', '_date', '_group', '_owner']

    def get_content(self):
        return self._content

    def get_group(self):
        return self._group
    
    def set_content(self, content):
        self._content = content

    def get_date(self):
        return self._date

    def get_owner(self):
        return self._owner
    
    def set_owner(self, owner):
        self._owner = owner

    def display(self):
        fullname = self._owner.get_fullname()
        username = self._owner.get_username()

        print('')
        if self._group is not None:
            print(f'From {fullname} ({username}) in {self._group.get_name()}:')
        else:
            print(f'From {fullname} ({username})')
        print(self._date)
        print(self._content)
        print('')
