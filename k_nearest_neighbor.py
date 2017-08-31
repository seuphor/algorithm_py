import numpy as np
from collections import Counter

def gen_data(numb):
    x1 = np.random.rand(numb,2) + np.array([0,0])
    x2 = np.random.rand(numb,2) + np.array([10,10])
    x = np.vstack((x1,x2))
    y = np.concatenate((np.zeros(numb), np.ones(numb)))
    return x, y

class kNN():
    def __init__(self, x, y):
        # evaluate all sample data point distance to the given point
        assert(len(x) == len(y))
        self.x = x
        self.y = y
        self.length = len(x)
        print('Loading Finished..')

    def predict(self, p, num_neighbor=3):
        # find the nearest neighbor points
        dist_arr = [0 for _ in range(self.length)]
        
        # sort the value and get nearest neighbour points
        dist = np.sqrt(np.sum((p - x)**2, axis=1))
        cls = y
        sorted_index = np.argsort(dist)
        # print(dist)
        # print(sorted_index)
            
        # vote for the class for this given point
        top_index = sorted_index[:num_neighbor]
        top_cls = cls[top_index]
        top_counter = Counter(top_cls)
        print('Predict Class for the point {}: {}'.format(p, top_counter.most_common(n=1)[0][0]))
        return top_cls
    
def test():
    point = np.array([4,1])
    num_neighbor = 3
    x, y = gen_data(10)
    
    knn = kNN(x, y)
    pred_class = k.predict(point,num_neighbor=num_neighbor)
    
if __name__ == '__main__':
    test()