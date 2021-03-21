import pylab
import matplotlib 
import networkx as nx
from datetime import datetime
import time

sample_1 = datetime.now()
time.sleep(2)
sample_2 = datetime.now()
secs = (sample_2 - sample_1).total_seconds()
print(int(secs))
