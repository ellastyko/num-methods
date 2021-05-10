import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import json
import plotly
import plotly.graph_objects as go  
from io import BytesIO  # noqa: I201
# x = np.array([0.705, 0.646, 0.610, 0.513, 0.738, 0.751], dtype=float)
# plt.plot(x)
# plt.grid(True)

x = [1, 2, 3, 4, 5]
y = ['a', 'b', 'c', 'd', 'v']
fig = go.Figure(data=[go.Table(header=dict(values=['X', 'Y']),
                                   cells=dict(values=[x, y]))
                          ])                        
graphJSON = json.dumps(plt, cls=plotly.utils.PlotlyJSONEncoder)
tmpfile = BytesIO()
fig.savefig(tmpfile, format='png')
encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')