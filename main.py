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


class MarketOrder:
    def __init__(self, size, buy=True):
        self.size = size
        self.type = type
        self.buy = buy

    def execute_order(self, ob):
        if self.buy:
            min_ask = ob.get_min_ask()
            if self.size < min_ask[1]:
                price = min_ask[0]
                updatedSize = min_ask[1]
                ob.update_min_ask_size(price, updatedSize)
                self.size = 0
            elif self.size == min_ask[1]:
                price = min_ask[0]
                ob.remove_min_ask(price)
        # if size is smaller than minimum ask size, subtract order size from minimum ask size else if equal or greater, then remove and subtract till size is smaller than lowest ask size(sorted on price)
        else:
            pass  # if size is smaller than maximum bid size, subtract order size from maximum bid size else if equal or greater, then remove and subtract till size is smaller than highest bid size(sorted on price)


class LimitOrder:
    def __init__(self, price, size, buy=True):
        self.price = price
        self.size = size
        self.type = type
        self.buy = buy

    def execute_order(self):
        if self.buy:
            pass  # if price is smaller than minimum ask price, add to bid dictionary else execute market order
        else:
            pass  # if price is greater than highest bid price, add to ask dictionary else execute market order


def main():
    ob = OrderBook()
    # Read Sample Data and perform operations in order maintaining a queue of pending orders
    # Display Bid Table
    # Display Ask Table
    pass


if __name__ == "__main__":
    main()
