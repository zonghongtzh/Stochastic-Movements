from utils import *
from functions import * 

# %matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d   

AAPL = pd.read_csv(os.path.join(utils.mypath, 'data', 'AAPL.csv'), index_col = [0]).rename(columns = {'adjclose': 'AAPL'})
AMZN = pd.read_csv(os.path.join(utils.mypath, 'data', 'AMZN.csv'), index_col = [0]).rename(columns = {'adjclose': 'AMZN'})
MSFT = pd.read_csv(os.path.join(utils.mypath, 'data', 'MSFT.csv'), index_col = [0]).rename(columns = {'adjclose': 'MSFT'})
df = pd.concat([AAPL,AMZN,MSFT], axis=1, join='outer').sort_index().ffill()

# data handling
scaled_df = scale(df.T).T # start from 0, end near 1, [0, 0,00114, ..., 0.99854, 1]

n = 126 # Half year worth of trading days
smoothed_df = scaled_df.rolling(n).mean()

# plot
fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = smoothed_df['AAPL'].tolist()
xline = smoothed_df['AMZN'].tolist()
yline = smoothed_df['MSFT'].tolist()
ax.plot3D(xline, yline, zline, 'black')

print(f'Scaling factor: {n} days mean')
# rotate the axes and update
for angle in range(0, 360*2):
    ax.view_init(10, angle)
    plt.draw()
    plt.pause(.001)