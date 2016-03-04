class Tree(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    @classmethod
    def create(self):
        tree = Tree(5)
        tree.insert(8)
        tree.insert(2)
        tree.insert(4)
        return tree

    def insert(self, data):
        if not self.data:
            self.data = data
            return

        if data < self.data:
            if not self.left:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Tree(data)
            else:
                self.right.insert(data)

    def find(self, data):
        if data == self.data:
            print self.data
            print self.left
            print self.right
            return True

        if data < self.data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self.data:
            print self.data
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self.data:
            if self.left:
                self.left.inorder()
            print self.data
            if self.right:
                self.right.inorder()
