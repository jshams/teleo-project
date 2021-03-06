class DecimalTreeNode():
    def __init__(self):
        self.children = [None] * 10
        self.cost = None

    def __repr__(self):
        return "{}"
    
    def insert(self, num, cost = None):
        if self.children[num] is None:
            self.children[num] = DecimalTreeNode()
        if cost is not None:
            self.cost = cost

class DecimalTree():
    def __init__(self, route_cost_path, phone_number_path):
        self.route_cost_path = route_cost_path
        self.phone_number_path = phone_number_path
        self.root = DecimalTreeNode()
        self.populate_tree()

        self.result = self.lookup_all_numbers()


    def _slice_prefix_and_cost(self, line):
        splitted_line = line.strip().split(',')
        prefix = splitted_line[0][1:]
        cost = splitted_line[1]
        return prefix, cost

    def populate_tree(self):
        route_costs = open(self.route_cost_path)
        for line in route_costs:
            item = self._slice_prefix_and_cost(line)
            self.insert(*item)
        route_costs.close()

    def insert(self, prefix, cost):
        '''will add a whole prefix of integers to our tree'''
        node = self.root
        for i, num in enumerate(prefix):
            num = int(num)
            if i < len(prefix) - 1:
                node.insert(num)
                node = node.children[num]
            else:
                node.insert(num, cost)
    
    def find_cost_of_num(self, number):
        node = self.root
        cost = None
        for digit in number:
            if node.cost is not None:
                cost = node.cost
            if node.children[int(digit)] is None: # in the case that the number is larger than its prefix
                return cost
            node = node.children[int(digit)]
        # in the case that the number is the same size as its prefix
        return cost

    def lookup_all_numbers(self):
        '''Go through phone number path an find the cost of each phone number 
        Use the lookup_number method to look through dictionary'''
        result = {}

        phone_numbers = open(self.phone_number_path, 'r')
        for line in phone_numbers:
            number = line.strip()[1:]
            cost = self.find_cost_of_num(number)
            result[f"+{number}"] = cost
            print(f"{number} , {cost}")


        phone_numbers.close()

        return result

if __name__ == '__main__':
    test_dict = DecimalTree("route-costs-10000000.txt", "phone-numbers-10000.txt")
    # result = test_dict.result
    # print(result)
    import pickle