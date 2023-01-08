from reading_let import *
from util import *




shapes = read("shapes_learn")
shapes = np.array(shapes)
X = []
Y = []
for i in range(len(shapes)):
    if i+1 > len(shapes)//2:
        Y.append(shapes[i])
    else:
        X.append(shapes[i])
X = np.array(X)
Y = np.array(Y)
W = X.T @ Y
W2 = W.T

X = np.array([read_shape("bad_shapes/modified2.txt")])
X2 = np.zeros_like(X)
print(X[0])
iterations = 0
while check(shapes, X2[0]) is False:
    iterations+=1
    print("Ассоциирую с этим образом:")
    Y = X @ W
    Y = f_activ(Y)
    show_shape(Y[0], 7)
    print("---------------------------------------------------")
    X2 = Y @ W2
    X2 = f_activ(X2)
    X = X2

    if iterations > 20:
        print("Не удалось распознать образ")
        exit()
print('Кол-во итераций: ', iterations)
show_shape(X2[0], 7)
