class Zebra:
    def __init__(self,):
        self.total = 0

    def which_stripe(self):
        self.total += 1
        if self.total % 2 !=0:
            return 'Poloska white'
        else:
            return 'Poloska black'

z1 = Zebra()

print(z1.which_stripe())
print(z1.which_stripe())
print(z1.which_stripe())