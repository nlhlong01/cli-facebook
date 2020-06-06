"""Draw a class diagram of a snapshot of the program using Graphviz library.
Objects are taken from the mock_data module. 
"""

import datetime
import inspect
import mock_data
from graphviz import Graph
from group import Group
from post import Post
from user import User


def is_builtin(obj):
    return type(obj) in (int, float, str, datetime.datetime)


def is_defined(obj):
    return type(obj) in (Post, User, Group)


def draw_nodes(graph, objects):
    for name, object in objects:
        attribute_info = ''

        for attr in dir(object):
            value = getattr(object, attr)
            # Self-defined classes must be treated differently
            if is_builtin(value):
                attribute_info += rf'{attr}:{type(value).__name__} = {str(value)}\n'

        # Simply let the unique id (memory address) be the node name of the object
        graph.node(
            name=str(id(object)),
            label=rf'{{{name}:{type(object).__name__} | {attribute_info}}}'
        )


def assign_label(head, tail):
    """Assign a text label to an edge"""
    label = ''

    if set((head, tail)) == set(('User', 'Post')):
        label = 'creates'
    elif set((head, tail)) == set(('User', 'Group')):
        label = 'joins'
    elif set((head, tail)) == set(('User', 'User')):
        label = 'adds as friend'
    elif set((head, tail)) == set(('Post', 'Group')):
        label = 'contains'

    return label


def draw_edges(graph, objects):
    # Since edges cannot be created without nodes, we must go through the
    # objects again after all nodes are created.
    for name, obj in objects:
        for attr in dir(obj):
            value = getattr(obj, attr)
            if value is None:
                break
            # Generate multiple edges from list of linked objects
            if isinstance(value, list):
                for item in value:
                    graph.edge(
                        str(id(obj)),
                        str(id(item)),
                        label=assign_label(
                            type(obj).__name__,
                            type(item).__name__
                        )
                    )
            # Generate only 1 edge from single linked object
            elif not is_builtin(value):
                graph.edge(
                    str(id(obj)),
                    str(id(value)),
                    label=assign_label(
                        type(obj).__name__,
                        type(value).__name__
                    )
                )


graph = Graph(
    'Facebook Object Diagram',
    format='png',
    node_attr={'shape': 'record'},
    strict=True
)

objects = inspect.getmembers(mock_data, is_defined)

draw_nodes(graph, objects)
draw_edges(graph, objects)

print(graph.source)
graph.render('documentation/diagram.gv')
