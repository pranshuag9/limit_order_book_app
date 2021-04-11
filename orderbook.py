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
