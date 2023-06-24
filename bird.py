import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

iteration=1000000
h=0.001

x_0=5
y_0=10

x=[x_0]
y=[y_0]

def forward(x,y,h):
        x_i=x
        y_i=y

        x_iplus1=y_i-0.97*x_i+5/(1+x_i**2)-5
        y_iplus1=-0.995*x_i

        return x_iplus1,y_iplus1

for i in tqdm(range(iteration)):
    x_iplus1,y_iplus1=forward(x[i],y[i],h)
    x.append(x_iplus1)
    y.append(y_iplus1)    

fig=plt.figure(figsize=(10,4))
ax=fig.subplots()
ax.scatter(x,y,s=0.01,color="black")
plt.show()