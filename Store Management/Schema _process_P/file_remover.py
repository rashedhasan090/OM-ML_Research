import sys
import os
from os import listdir

test=os.listdir("/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Store Management/Schema _process_P")

for item in test:
    # if item.endswith(".sql"):
    #     os.remove(item)
    if item.endswith(".xml"):
        os.remove(item)
    # if item.endswith(".xml.txt"):
    #     os.remove(item)
    # if item.endswith(".txt"):
    #     os.remove(item)
