from store import Store
import hashlib
import hmac
import os


store = Store()


# Test users
john = store.create_user('John A.', 'john', 'johnpw')
jane = store.create_user('Jane B.', 'jane', 'janepw')
rick = store.create_user('Richard C.', 'rick', 'rickpw')
alan = store.create_user('Alan D.', 'alan', 'alanpw')
tom = store.create_user('Thomas E.', 'tom', 'tompw')
jack = store.create_user('Jack F.', 'jack', 'jackpw')
# Add John and Jane as friends of Tom.
# Tom should see their posts on his newsfeed.
tom.add_friend(john)
tom.add_friend(jane)

# Test group.
# People in the same group must see the posts of each other.
ast_class = store.create_group('AST Class')
joining_members = [tom, alan, rick]
for i in joining_members:
    i.join_group(ast_class)

ml_class = store.create_group('ML Class')
joining_members = [jane, rick]
for i in joining_members:
    i.join_group(ml_class)

# Test posts
tom.create_post(content='The weather is so nice!')
tom.create_post(group=ast_class,
                content='When is the next meeting?')
john.create_post(content='I finally graduated.')
rick.create_post(
    group=ast_class, content="Hey Tom. Let's team up for the assignment!")
jane.create_post(group=ml_class, content="Welcome all to the ML Class.")
jack.create_post(content='Check out my new video!')
