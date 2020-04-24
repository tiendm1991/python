import scipy.stats as ss
import matplotlib.pyplot as plt

def gen_data(n, h, sd1, sd2):
   x1 = ss.norm.rvs(h, sd1, n)
   y1 = ss.norm.rvs(0, sd1, n)
   x2 = ss.norm.rvs(-h, sd2, n)
   y2 = ss.norm.rvs(0, sd2, n)
   return (x1, y1, x2, y2)

def plot_data(x1, y1, x2, y2):
   plt.figure()
   plt.plot(x1, y1, "o", ms=2)
   plt.plot(x2, y2, "o", ms=2)
   plt.xlabel("$X_1$")
   plt.ylabel("$X_2$")
   plt.show()


def prob_to_odds(p):
   if p <= 0 or p >= 1:
      print("Probabilities must be between 0 and 1.")
   return p / (1 - p)

print(prob_to_odds(0.2))

