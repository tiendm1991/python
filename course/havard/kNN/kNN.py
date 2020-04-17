
import pandas as pd
import numpy as np, random, scipy.stats as ss
import sklearn.preprocessing as preprocessing
import sklearn.decomposition as decomposition
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.neighbors import KNeighborsClassifier

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

def gen_data(n = 50):
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    points = np.concatenate((ss.norm(0, 1).rvs((n,2)), ss.norm(1, 1).rvs((n,2))))
    return (points, outcomes)

def make_prediction_grid(predictors, outcomes, limits, h, k):
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    predict_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            predict_grid[j, i] = knn_predict(p, predictors, outcomes, k)
    return (xx, yy, predict_grid)

data = pd.read_csv("wine.csv")
data.loc[data["color"] == "red", "is_red"] = 1
data.loc[data["color"] != "red", "is_red"] = 0
data = data.drop(columns=["color"])
scaled_data = preprocessing.scale(data)
numeric_data = pd.DataFrame(scaled_data)
columns = numeric_data.columns
pca = decomposition.PCA()
principal_components = pca.fit_transform(numeric_data)

# observation_colormap = ListedColormap(['red', 'blue'])
# x = principal_components[:,0]
# y = principal_components[:,1]
#
# plt.title("Principal Components of Wine")
# plt.scatter(x, y, alpha = 0.2,
#     c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
# plt.xlim(-8, 8); plt.ylim(-8, 8)
# plt.xlabel("Principal Component 1")
# plt.ylabel("Principal Component 2")
# plt.show()

np.random.seed(1) # do not change this!

x = np.random.randint(0, 2, 1000)
y = np.random.randint(0 ,2, 1000)

def accuracy(predictions, outcomes):
    return len([1 for i in range(len(outcomes)) if predictions[i] == outcomes[i]]) * 100 / len(outcomes)

# print(np.array(data["high_quality"]))
# print(np.array(data["high_quality"][data.high_quality==0]))
# print(accuracy(np.array(data["high_quality"]), np.zeros(len(data["high_quality"]))))

# knn = KNeighborsClassifier(n_neighbors = 5)
# knn.fit(numeric_data, data['high_quality'])
# library_predictions = knn.predict(numeric_data)
# print(accuracy(library_predictions, data['high_quality']))

n_rows = data.shape[0]
random.seed(123)
selection = random.sample(range(n_rows), 10)
print(selection)

predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = [knn_predict(p, predictors[training_indices,:], outcomes, k=5) for p in predictors[selection]]
print(my_predictions)
percentage = accuracy(my_predictions, outcomes[selection])
print(percentage)
