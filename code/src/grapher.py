import inspect
import mock_data
from graphviz import Digraph, Graph


graph = Digraph(
    'Facebook Object Diagram',
    format='png',
    node_attr={'shape': 'record'}  
)

objects = inspect.getmembers(
    mock_data,
    lambda object:
        # type(object).__name__ in ('Store', 'User', 'Group', 'Post')
        type(object).__name__ in ('User')
)

for name, object in objects:
    attribute_info = rf''

    for attr in dir(object):
        value = getattr(object, attr)
        attribute_info += rf'{attr}:{type(value).__name__} = {value}\n'

    label = rf'{{{name}:{type(object).__name__} | {attribute_info}}}'

    graph.node(name=str(id(object)), label=label)


# diagram.edges(['AB', 'AL'])
# diagram.edge('B', 'L', constraint='false')
print(graph.source)
graph.render('documentation/diagram.gv', view=True)
