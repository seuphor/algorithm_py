import numpy as np

def generate_data(numb):
    x = np.arange(numb)
    y = np.random.rand(numb)
    return x, y

class linear_regression():
    def __init__(self, m, b, learning_rate, iteration=1000):
        self.m = m
        self.b = b
        self.learning_rate = learning_rate
        self.iteration = iteration
    
    def fit(self, x, y):
        assert(len(x) == len(y))
        length = float(len(x))
        print('Error before optimizing: {:0.4f}'.format(self.mse(x, y)))
        
        # loop number of iterations
        for iters in range(self.iteration):
            gradient_m = 0
            gradient_b = 0
            
            # evaluate gradient for each parameter m, b respectively
            for i in range(len(x)):
                gradient_m += - (2/length) * x[i] * (y[i] - (self.m * x[i] + self.b))
                gradient_b += - (2/length) * (y[i] - (self.m * x[i] + self.b))

            self.m -= self.learning_rate * gradient_m
            self.b -= self.learning_rate * gradient_b
            
            if (iters+1) % 100 == 0:
                print('Error for {} iteration: {:0.4f}'.format(iters+1, self.mse(x, y)))
        print('Optimization Finished')
    
    def mse(self, x, y):
        assert(len(x) == len(y))
        length = float(len(x))
        err = 0
        for i in range(len(x)):
            pred = self.m * x[i] + self.b
            err += 1/length * (pred - y[i])**2
        return err

def test():
    
    learning_rate = .001
    iteration = 1000
    init_m = 0.
    init_b = 0.
    
    x, y = generate_data(3)
    
    lr = linear_regression(init_m, init_b, learning_rate, iteration)
    lr.fit(x, y)
    
if __name__ = '__main__':
    test()