import random

class GetData():
    
    def __init__(self):
        pass

    def return_data(self):
        data = open('lib/data','rb').readlines()
        domain = []
        for x in range(2):
            domain.append(data.pop(random.randint(0,len(data)-1)).strip())
        return domain[0],domain[1]