
import matplotlib.pyplot as plt
from probability import *

def mean(x):
    return sum(x) / len(x)

def Q1(x):
    x = sorted(x)
    if len(x) % 2 == 0:
        return median(x[0:int(len(x)/2)])
    else:
        return median(x[0:int(len(x)/2)])

def Q3(x):
    x = sorted(x)
    if len(x) % 2 == 0:
        return median(x[int(len(x)/2):])
    else:
        return median(x[int(len(x)/2+1):])


def median(x):
    x = sorted(x)
    if len(x) % 2 == 0:
        return mean(x[int(len(x)/2-1): int(len(x)/2+1)])
    else:
        return x[int(len(x)/2)]

def mode(x):
    mode = [[None], 0]
    for item in set(x):
        if x.count(item) > mode[1]:
            mode[0] = [item]
            mode[1] = x.count(item)
        elif x.count(item) == mode[1]:
            mode[0].append(item)

    return mode[0]

def _range(x):
    return max(x) - min(x)

def IQR(x):
    """Inter Quartile Range of x"""
    return Q3(x) - Q1(x)

def var(x):
    m = mean(x)
    v = lambda a: (m-a)**2
    V = list(map(v, x))
    return sum(V)/len(x)

def std(x):
    return var(x)**0.5

np.random.seed(42)
population = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0])
n = len(population)
m = 5
p = mean(population) / n
q = 1-p

for i in range(1):
    sample = np.random.choice(population, size=m, replace=True)
    description = """Proportion of the poplation that drink coffee: %f
    Variance of the population that drink coffee: %f
    The npq of the population is: %f
    Proportion of the sample: %f
    Variance of the sample: %f
    """ % (p,
        var(population),
        n*p*q,
        mean(sample),
        var(sample))

    print(description)

# a = []
# for i in range(3,11):
#     a.append(laplace_probability(10, i, 0.15))
# 
# print(str(sum(a)))

# p_a = 0.2
# p_b = 0.1
# df, summa = unconditional_truth_table(p_a, p_b)
# plt.show()
# print(df)
# print('\n')
# print(summa)


# a = 3
# print(factorial(a))
# print(format(laplace_probability(12, 9, .8), 'g'))




"""
a = [5, 8, 15, 7, 10, 22, 3, 1, 15]
b = [5, 8, 15, 7, 10, 22, 3, 1, 15, 1]
c = [8, 12, 32, 10, 3, 4, 4, 4 ,4, 5, 12, 20]
c = [5, 8, 15, 7, 10, 22, 3, 1, 15, 10]
c = [5, 15, 3, 3, 8, 10, 12]
c = [1, 5, 10, 3, 8, 12, 4, 1, 2, 8]
c = [5, 10, 3, 8, 12, 4, 1, 2, 8]
c = [1, 5, 10, 3, 8, 12, 4]
c = [12, -2, 10, 0, 7, 3]
c = [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]
c = [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]

print('The amount of data is % 7d' % (len(c)))
print('The sum is            % 7.2f' % (sum(c)))
print('The range is          % 7.2f' % (_range(c)))
print('The IQR is            % 7.2f' % (IQR(c)))
print('The mean is           % 7.2f' % (mean(c)))
print('The Q1 is             % 7.2f' % (Q1(c)))
print('The median is         % 7.2f' % (median(c)))
print('The Q3 is             % 7.2f' % (Q3(c)))
print('The Variance is       % 7.2f' % (var(c)))
print('The Std. Deviation is % 7.2f' % (std(c)))
print('The mode is           %s' % str(mode(c)))
"""