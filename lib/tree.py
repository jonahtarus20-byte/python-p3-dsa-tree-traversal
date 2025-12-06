class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id_value):
        # Start with a list containing the root node
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            # Take the first node from the list
            node = nodes_to_visit.pop(0)

            # Check if this node has the matching id
            if node.get('id') == id_value:
                return node

            # Add its children to the beginning of the list (DFS)
            nodes_to_visit = node['children'] + nodes_to_visit

        # If no node matches the id
        return None
