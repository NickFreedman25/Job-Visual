from URL_Request import url_request
import matplotlib.pyplot as plt
import numpy


class visualize:
    def __init__(self):
        self.x = list()
        self.y = list()
        data = url_request()
        d = data.get_jobs()
        for keys in d:
            self.x.append(keys)
            self.y.append(d[keys])
        self.x.sort()
        self.y.sort()

    def plot(self):
        plt.bar(self.x, self.y)
        plt.xlabel("Years of Experience Required")
        plt.ylabel("Quantity of Jobs")
        plt.title("Quantity of Entry-Level Jobs by Required Years of Experience")
        plt.show()

v = visualize()
v.plot()
