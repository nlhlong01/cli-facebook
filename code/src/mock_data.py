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
for user in joining_members:
    user.join_group(ast_class)

ml_class = store.create_group('ML Class')
joining_members = [jane, rick]
for user in joining_members:
    user.join_group(ml_class)

# Test posts
tom.create_post('The weather is so nice!')
tom.create_post('When is the next meeting?', group=ast_class)
john.create_post('I finally graduated.')
rick.create_post("Hey Tom. Let's team up for the assignment!", group=ast_class)
jane.create_post("Welcome all to the Machine Learning Class.", group=ml_class)
jack.create_post('Check out my new video on Youtube!')
