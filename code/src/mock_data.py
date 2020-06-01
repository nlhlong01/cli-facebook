from post import Post
from store import Store
import hashlib
import hmac
import os
import inspect


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
tom.join(ast_class)
alan.join(ast_class)
rick.join(ast_class)

ml_class = store.create_group('ML Class')
jane.join(ml_class)
rick.join(ml_class)

# Test posts
post_tom_self = Post('The weather is so nice!')
tom.post(post_tom_self)

post_tom_ast = Post('When is the next meeting?', group=ast_class)
tom.post(post_tom_ast)

post_john_self = Post('I finally graduated.')
john.post(post_john_self)

post_rick_ast = Post("Hey Tom. Let's team up for the assignment!", group=ast_class)
rick.post(post_rick_ast)

post_jane_ml = Post('Welcome all to the Machine Learning Class.', group=ml_class)
jane.post(post_jane_ml)

post_jack_self = Post('Check out my new video on Youtube!')
jack.post(post_jack_self)
