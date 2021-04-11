from mo import MarketOrder
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
