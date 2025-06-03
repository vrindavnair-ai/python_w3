import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random
import time

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()
time.sleep(5)  # Wait for 5 seconds
plt.close()

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()

time.sleep(5)  # Wait for 5 seconds
plt.close()

sns.displot(random.normal(size=1000), kind="kde")

plt.show()
sns.displot(random.binomial(n=10, p=0.5, size=1000)) #binomial is discrete with less data point whereas normal distribution is continuos

plt.show()
time.sleep(5)  # Wait for 5 seconds
plt.close()

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()
time.sleep(5)  # Wait for 5 seconds
plt.close()

sns.displot(random.poisson(lam=2, size=1000))

plt.show()