class DecimalTreeNode():
    def __init__(self, data):
        self.children = [None] * 10
        self.cost = None

class DecimalTree():
    def __init__(self, route_cost_path, phone_number_path):
        self.route_cost_path = route_cost_path
        self.phone_number_path = phone_number_path
        self.items = 0
        self.root = DecimalTreeNode()

    def route_tree(self, route_cost_list):
        ''' Given an array of route costs with (key, value) pairs
        Add these integers to a tree'''

    def map_route_cost_list(self, base = 10):
        '''take the phone_number_path and convert the whole file to a list with the numbers in base n
        return a list of (number in base n, cost)'''
        pref_cost_pairs = []
        f = open(self.route_cost_path, 'r')
        for line in f:
            splitted_line = line.strip().split(',')
            prefix = splitted_line[0][1:]
            if base != 10:
                # convert prefix to base base
                prefix = prefix
            cost = splitted_line[1]
            pref_cost_pairs.append((prefix, cost))
        f.close()
        return pref_cost_pairs
