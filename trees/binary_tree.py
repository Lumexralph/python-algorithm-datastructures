from tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # additional abstract methods
    def left_child(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child
        """
        raise NotImplementedError('must be implemented by the subclass')
    
    def right_child(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child
        """
        raise NotImplementedError('must be implemented by the subclass')

    # concrete methods that got implemented in this class
    def sibling(self, p):
        """Return a Position representing p's sibling or None if no sibling."""
        parent = self.parent(p)
        
        if parent is None:                                      # p must be the root
            return None                                         # a root has no sibling
        else:
            if p == self.left_child(parent):                    # if it is the left child
                return self.right_child(parent)
            else:
                return self.left_child(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left_child(p) is not None:
            yield self.left_child(p)
        if self.right_child(p) is not None:
            yield self.right_child(p)




