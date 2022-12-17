class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.requests = list()

    def __len__(self):
        return len(self.requests)

    def __customer_turnover_per_day(self):
        days = dict()
        for line in self.requests:
            if line[2] in days:
                days[line[2]] += 1
            else:
                days[line[2]] = 1
        return days

    def __get_bigger(self, dict):
        compare, max = 0, ''
        for key in dict:
            if dict[key] > compare:
                compare = dict[key]
                max = key
        return max

    def __generic_never(self, n, name):
        v = [line[n] for line in self.requests if line[0] == name]
        v_n = [line[n] for line in self.requests if line[n] not in v]
        v_d = set()
        for i in v_n:
            if i not in v_d:
                v_d.add(i)
        return v_d

    def add_new_order(self, customer, order, day):
        self.requests.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        dishes = dict()
        for line in self.requests:
            if line[0] == customer:
                if line[1] in dishes:
                    dishes[line[1]] += 1
                else:
                    dishes[line[1]] = 1
        return self.__get_bigger(dishes)

    def get_never_ordered_per_customer(self, customer):
        return self.__generic_never(1, customer)

    def get_days_never_visited_per_customer(self, customer):
        return self.__generic_never(2, customer)

    def get_busiest_day(self):
        return self.__get_bigger(self.__customer_turnover_per_day())

    def get_least_busy_day(self):
        days = self.__customer_turnover_per_day()
        compare, min = list(days.items())[0][1], ''
        for key in days:
            if days[key] < compare:
                compare = days[key]
                min = key
        return min
