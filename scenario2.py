class LookUpDict():

    def __init__(self, route_cost_path, phone_number_path):
        self.route_cost_path = route_cost_path
        self.phone_number_path = phone_number_path
        self.longest_pref = None
        self.shortest_pref = None

        self.route_cost_dict = self.route_cost_to_dict()
        self.result = self.lookup_all_numbers()

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

            if self.longest_pref is None:
                self.longest_pref = len(prefix)
                self.shortest_pref = len(prefix)
            else:
                if len(prefix) < self.shortest_pref:
                    self.shortest_pref = len(prefix)
                if len(prefix) > self.longest_pref:
                    self.longest_pref = len(prefix)

        file.close()

        return route_dict

    def lookup_number(self, num):
        '''Given a full number search our dictionary for the cost or return None if not found'''
        # search for full number in dict
        # if not found, remove the last char
        # OPTIMIZATION, the length of largest prefix is the index we should start at as long as len(num) < largest_pref_len
        if len(num) > self.longest_pref:
            num = num[:self.longest_pref]
        if len(num) < self.shortest_pref:
            return None

        if num in self.route_cost_dict:
            return self.route_cost_dict[num]
        else:
            return self.lookup_number(num[:-1])

    def lookup_all_numbers(self):
        '''Go through phone number path an find the cost of each phone number 
        Use the lookup_number method to look through dictionary'''
        
        result = {}

        file = open(self.phone_number_path, 'r')

        for line in file:
            number = line.strip()
            cost = self.lookup_number(number)
            result[number] = cost
        file.close()

        return result

if __name__ == "__main__":
    test_dict = LookUpDict("route-costs-1000000.txt", "phone.txt")
    result = test_dict.result
    print(result)