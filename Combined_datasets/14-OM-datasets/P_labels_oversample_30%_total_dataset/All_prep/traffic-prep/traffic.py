from imblearn.over_sampling import RandomOverSampler
from collections import Counter

import pandas as pd
df = pd.read_csv('Traffic_30.csv')

#Split our data into features(X) and labels(y)
X=df.drop('OM_Regular',axis=1)
y=df['OM_Regular']


print("Original Count")

print(y.value_counts())

from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(sampling_strategy="not majority") # String
X_res, y_res = ros.fit_resample(X, y)


print("Oversampled Count")

print(y_res.value_counts())

y_res.to_csv('traffic_oversample_3.csv')
