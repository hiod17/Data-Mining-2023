import transbigdata as tbd
import pandas as pd

data = pd.read_csv("C:\\Users\\Xu\\Downloads\\traj.csv",header = None,low_memory=False)
data.columns = ['id','time','entity_id','traj_id','coordinates','current_dis','speeds','holidays']
data.head()