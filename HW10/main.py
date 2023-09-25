import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data.sample(10))

