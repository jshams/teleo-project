class LookUpDict():

    def __init__(self, route_cost_path, phone_number_path):
        self.route_cost_path = route_cost_path
        self.phone_number_path = phone_number_path

        self.route_cost_dict = self.route_cost_to_dict()

    def route_cost_to_dict(self):
        '''
        This method will convert our route cost text file into dictionary{prefix: cost}
        Time complexity: O(n) worst and best case
        Memroy complexity: O(n) worst and best
        '''
        route_dict = {}

        file = open(self.route_cost_path)

        for line in file:
            splitted_line = line.strip().split(',')
            prefix = splitted_line[0]
            cost = splitted_line[1]
            route_dict[prefix] = cost

        file.close()
        
        return route_dict

if __name__ == "__main__":
    test_dict = LookUpDict("teleo.txt", "hello")
    print(test_dict.route_cost_dict)