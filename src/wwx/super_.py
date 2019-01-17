class Pizza(object):
    def __init__(self,toppings):
        self.toppings = toppings


    def __repr__(self):
        return "pizza with "+" and ".join(self.toppings)
    @classmethod
    def recommend(cls):
        return cls(['spam','ham','eggs'])
class Viking(Pizza):
    @classmethod
    def recommend(cls):
        recommend = super().recommend();
        recommend.toppings +=['spam']*5
        return recommend
#Pizza('').recommend('')
#Pizza('').recommend('')
#s = Pizza.recommend()
#print(s)
s = Viking(['wwx']).recommend()
s = Viking(['wwx'])
print(s)
s= Pizza(['']).recommend()
print(s)
#Viking(('屎','尿')).test()
#Viking('').test()

