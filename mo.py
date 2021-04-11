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
