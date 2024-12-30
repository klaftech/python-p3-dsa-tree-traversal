class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_look = [self.root]
    
    while len(nodes_to_look) > 0:
      node = nodes_to_look.pop(0)
      print('NODE HERE:')
      print(node)
      node_id = node['id']
      if node_id and node_id == id:
        print("SUCCESS")
        return node
      else:
        nodes_to_look = nodes_to_look + node['children']
    
    return None
