'''NodeVisitor.py'''  
d = True
def dprint(msg):
    if d:
        print(msg)

class NodeVisitor(object):
    '''Combine the visit() methods from node into a
    single class with a dispatcher method:
    '''
    def visit(self, node):
        dprint(f'visit : {node}')
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))