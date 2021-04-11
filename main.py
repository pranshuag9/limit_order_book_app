class OrderBook:
    def __init__(self):
        self.askbook = dict()
        self.bidbook = dict()

    def get_min_ask(self):
        self.askbook = dict(sorted(self.askbook.items(), key=lambda kv: (kv[1], kv[0])))
        return list(self.askbook.items())[0]

    def get_max_bid(self):
        self.bidbook = dict(sorted(self.bidbook.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
        return list(self.bidbook.items())[0]

    def update_min_ask_size(self, price, updatedSize):
        self.askbook[price] = updatedSize

    def update_max_bid_size(self, price, updatedSize):
        self.bidbook[price] = updatedSize

    def remove_min_ask(self, price):
        self.askbook.pop(price)

    def remove_max_bid(self, price):
        self.bidbook.pop(price)

    def add_to_askbook(self, limitPrice, limitSize):
        self.askbook[limitPrice] = self.askbook.get(limitPrice, 0) + limitSize

    def add_to_bidbook(self, limitPrice, limitSize):
        self.bidbook[limitPrice] = self.bidbook.get(limitPrice, 0) + limitSize


class MarketOrder:
    def __init__(self, size, buy):
        self.size = size
        self.buy = buy

    def execute_order(self, ob):
        if self.buy:
            try:
                min_ask = ob.get_min_ask()
            except:
                print("Error getting minimum ask!! Invalid size entered.")
                pass
            else:
                while self.size >= min_ask[1]:
                    price = min_ask[0]
                    min_ask_size = min_ask[1]
                    self.size -= min_ask_size
                    ob.remove_min_ask(price)
                    try:
                        min_ask = ob.get_min_ask()
                    except:
                        print("Error getting minimum ask!! Invalid size entered.")
                        pass
                if self.size < min_ask[1]:
                    price = min_ask[0]
                    updatedSize = min_ask[1] - self.size
                    self.size = 0
                    ob.update_min_ask_size(price, updatedSize)
        else:
            try:
                max_bid = ob.get_max_bid()
            except:
                print("Error getting maximum bid!! Invalid size entered.")
                pass
            else:
                while self.size >= max_bid[1]:
                    price = max_bid[0]
                    max_bid_size = max_bid[1]
                    self.size -= max_bid_size
                    ob.remove_max_bid(price)
                    try:
                        max_bid = ob.get_max_bid()
                    except:
                        print("Error getting maximum bid!! Invalid size entered.")
                        pass
                if self.size < max_bid[1]:
                    price = max_bid[0]
                    updatedSize = max_bid[1] - self.size
                    self.size = 0
                    ob.update_max_bid_size(price, updatedSize)


class LimitOrder:
    def __init__(self, price, size, buy):
        self.price = price
        self.size = size
        self.type = type
        self.buy = buy

    def execute_order(self, ob):
        if self.buy:
            try:
                min_ask = ob.get_min_ask()
            except:
                print("Error getting minimum ask!! Invalid size entered.")
                pass
            else:
                if self.price < min_ask[0]:
                    ob.add_to_bidbook(self.price, self.size)
                else:
                    mo = MarketOrder(size=self.size, buy=self.buy)
                    mo.execute_order(ob)
                    del mo
        else:
            try:
                max_bid = ob.get_max_bid()
            except:
                print("Error getting maximum bid!! Invalid size entered.")
                pass
            else:
                if self.price > max_bid[0]:
                    ob.add_to_askbook(self.price, self.size)
                else:
                    mo = MarketOrder(size=self.size, buy=self.buy)
                    mo.execute_order(ob)
                    del mo


def main():
    ob = OrderBook()
    # Read Sample Data and perform operations in order maintaining a queue of pending orders
    # Display Bid Table
    # Display Ask Table
    pass


if __name__ == "__main__":
    main()
