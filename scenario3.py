class DecimalTreeNode():
    def __init__(self, data):
        self.data = data
        self.children = [None] * 10
        self.cost = None

class DecimalTree():
    def __init__(self, route_cost_path, phone_number_path):
        self.route_cost_path = route_cost_path
        self.phone_number_path = phone_number_path
        
        self.root = DecimalTreeNode('+')

    def populate_tree(self, prefix, cost):
        pass

    def slice_prefix_and_cost(self):

        f = open(self.route_cost_path, 'r')
        for line in f:
            splitted_line = line.strip().split(',')
            prefix = splitted_line[0][1:]
            cost = splitted_line[1]

            self.populate_tree(prefix, cost)

        f.close()
