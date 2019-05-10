class DecimalTreeNode():
    def __init__(self):
        self.children = [None] * 10
        self.cost = None
    
    def insert(self, num, cost = None):
        if self.children[num] is None:
            self.children[num] = DecimalTreeNode()
        if cost is not None:
            self.children[num].cost = cost

class DecimalTree():
    def __init__(self, route_cost_path, phone_number_path):
        self.route_cost_path = route_cost_path
        self.phone_number_path = phone_number_path
        self.root = DecimalTreeNode()
    
    def _slice_prefix_and_cost(self, line):
        splitted_line = line.strip().split(',')
        prefix = splitted_line[0][1:]
        cost = splitted_line[1]
        return prefix, cost

    def populate_tree(self):
        file = open(self.route_cost_path)
        for line in file:
            item = self._slice_prefix_and_cost(line)
            self.insert(*item)
        file.close()

    def insert(self, prefix, cost):
        '''will add a whole prefix of integers to our tree'''
        node = self.root
        for i, num in enumerate(prefix):
            if i <= len(prefix) - 1:
                node.insert(num)
                node = node.children[num]
            else:
                self.insert(num, cost)
