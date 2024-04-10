
class Posuda:
    def __init__(self, common_volume=None, current_volume=None):
        self.common_volume = common_volume
        self.current_volume = current_volume

    # common_volume = None
    # current_volume = None

    def get_common_volume(self):
        return self.common_volume

    def get_current_volume(self):
        return self.current_volume

    def set_common_volume(self, arg):
        if arg <= self.common_volume:
            self.common_volume = arg
        else:
            print("ERROR")

    def set_current_volume(self, arg):
        self.current_volume = arg


class Stakan(Posuda):
    def __init__(self):
        super().__init__(common_volume=100, current_volume=0)

    # common_volume = 100
    # current_volume = 0

class Grafin(Posuda):
    def __init__(self):
        super().__init__(common_volume=1000, current_volume=150)
    # common_volume = 1000
    # current_volume = 150


class View:
    @staticmethod
    def print(class1, class2):
        print(class1.common_volume)
        print(class1.current_volume)

        print(class2.common_volume)
        print(class2.current_volume)



class Controller:
    @staticmethod
    def process(Stakan, Grafin):
        Stakan.set_current_volume(Grafin.get_current_volume())
        View.print(Stakan, Grafin)
        Stakan.set_current_volume(Grafin.set_current_volume())
        View.print(Stakan, Grafin)


stakan = Stakan()
grafin = Grafin()

Controller.process(stakan,grafin)
