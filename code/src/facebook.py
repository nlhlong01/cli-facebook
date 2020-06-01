import cmd
import getpass
import hashlib
import os
import re
import hmac
from post import Post


class Facebook(cmd.Cmd):
    """The app extends the cmd.Cmd class, which is
    a built-in framework for CLI app.

    All commands:

    When logged out/Before logged in: register, login

    When logged in: newsfeed, friends, add, groups, join, post, search, logout

    """
    intro = '''\nWelcome to Facebook. Type help or ? to list commands.
    Type help <command> to know how to use the command.'''
    prompt = '(facebook) '

    def __init__(self, store):
        super().__init__()
        self._store = store

    def precmd(self, line):
        """Called before the command is executed."""
        # Commands which cannot be executed when not logged in
        restricted_commands = ('logout', 'newsfeed', 'friends', 'groups',
                               'group', 'search', 'add', 'join', 'post')

        if self._store.get_current_user() is None and line in restricted_commands:
            print('Please log in to use this feature!')
            return ''

        return line

    def emptyline(self):
        pass

    def do_register(self, arg):
        'Registers a new user.'
        fullname = input('Full name: ')
        username = input('Username: ')
        password = getpass.getpass('Password: ')

        self._store.create_user(fullname, username, password)

    def do_login(self, arg):
        'Log in with registered username and password.'
        username = input('Username: ')
        user = self._store.get_user(username)
        if (user is not None):
            input_password = getpass.getpass('Password: ')

            # TODO: encapsulate this feature in User class
            salt = user.get_salt()
            input_pw_hash = hashlib.pbkdf2_hmac(
                'sha256',
                input_password.encode('utf-8'),
                salt,
                100000
            ) + salt

            if (hmac.compare_digest(input_pw_hash, user.get_pw_hash())):
                self._store.set_current_user(user)
                self.prompt = f'({self._store.get_current_user().get_username()}) '
            else:
                print('Wrong password.')
        else:
            print('Wrong username.')

    def do_logout(self, arg):
        'Log out of current session.'
        self._store.set_current_user(None)
        self.prompt = '(facebook) '

    def do_newsfeed(self, arg):
        'Aggregates and displays posts on a central newsfeed.'
        # Aggregates posts from all sources (own, friends, groups)
        current_user = self._store.get_current_user()

        own_posts = current_user.get_posts()

        friends_posts = []
        for friend in current_user.get_friends():
            friends_posts.extend(friend.get_posts())

        groups_posts = []
        for group in current_user.get_groups():
            groups_posts.extend(group.get_posts())

        total_posts = []
        total_posts.extend(own_posts)
        total_posts.extend(friends_posts)
        total_posts.extend(groups_posts)

        total_posts = sorted(total_posts, key=lambda post: post.get_date())

        # Displays posts
        print('')
        print('NEWSFEED')
        for post in total_posts:
            post.display()
        print('')

    def do_friends(self, arg):
        'Displays all added friends'
        friends = sorted(
            self._store.get_current_user().get_friends(),
            key=lambda friend:
            friend.get_fullname()
        )

        # Displays friends.
        print('')
        print('FRIEND LIST')
        print(f'{len(friends)} friend(s)')
        print('=========================')
        for friend in friends:
            print(f'{friend.get_fullname()} ({friend.get_username()})')
        print('')

    def do_add(self, arg):
        'Add a new friends. Usage: add <friend_name>.'
        friend = self._store.get_user(arg)
        self._store.get_current_user().add_friend(friend)

    def do_search(self, arg):
        'Search a friend by first name. Usage: search <name>'
        print('Search result:')
        for user in self._store.get_users():
            if re.match(rf'^{arg}\w*\s', user.get_fullname(), re.IGNORECASE):
                print(f'{user.get_fullname()} ({user.get_username()})')

    def do_groups(self, arg):
        'Displays all joined groups and all created groups'
        current_user = self._store.get_current_user()

        joined_groups = sorted(
            current_user.get_groups(),
            key=lambda group:
            group.get_name()
        )

        total_groups = sorted(
            self._store.get_groups(),
            key=lambda group:
            group.get_name()
        )

        # Displays groups
        print('')
        print('GROUP LIST')
        print('')
        print(f'{len(joined_groups)} joined group(s):')
        for group in joined_groups:
            print(f'{group.get_name()}')
        print('')
        print('All group(s):')
        for group in total_groups:
            print(f'{group.get_name()}')
        print('')

    def do_join(self, arg):
        'Join a group. Usage: join <group_name>'
        group = self._store.get_group(arg)
        self._store.get_current_user().join(group)

    def do_post(self, arg):
        'Create a text post. Usage: post <content>'
        post = Post(arg)
        self._store.get_current_user().post(post)
