"""A CLI app replicating the basic features of Facebook:

1. Register new users, with usernames and passwords.
2. Login into an account, with username and password.
3. Search users by their first name.
4. Add a friend to the friend list.
5. Create, Join and Leave a group.
6. Show the list of friends and joined groups.
7. Create a text post.
8. See the posts from friends and joined groups on a central newsfeed.
"""


from facebook import Facebook
from mock_data import store


def main():
    Facebook(store).cmdloop()


if __name__ == "__main__":
    main()
