# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print('汪汪汪')
# class Cat(Animal):
#     def speak(self):
#         print('喵喵喵')
# def make_noise(animal:Animal):
#     animal.speak()
# dog = Dog()
# cat = Cat()
# make_noise(dog)
# make_noise(cat)

class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass
class Midea(AC):
    def cool_wind(self):
        print('美的空调制冷')
    def hot_wind(self):
        print('美的空调制热')
    def swing_l_r(self):
        print('美的空调左右摆风')
class GREE(AC):
    def cool_wind(self):
        print('格力空调制冷')
    def hot_wind(self):
        print('格力空调制热')
    def swing_l_r(self):
        print('格力空调左右摆风')
def make_cool(ac:AC):
    ac.cool_wind()
midea_ac = Midea()
gree_ac = GREE()
make_cool(gree_ac)
make_cool(midea_ac)

