import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

IMG_WIDTH = 1600
IMG_HEIGHT = 900
SCALE_FACTOR = 0.5
HEADER_COL = 'grey'
EVEN_ROW_COL = 'lightgrey'
ODD_ROW_COL = 'white'

image_count = len(df.member_id) + 1
images = []
for index in range(len(df.member_id)):
  if df.image_url[index]:
    print('@1 - ', df.member_id[index], df.image_url[index])
    img_url = df.image_url[index]
    images.append(
      go.layout.Image(
        x = IMG_WIDTH * SCALE_FACTOR / 10 * 2 - 5,
        sizex = IMG_WIDTH * SCALE_FACTOR / 10 * 2 + 10,
        y = IMG_HEIGHT * SCALE_FACTOR / image_count * (index + 1) - index * 16/9,
        sizey = IMG_HEIGHT * SCALE_FACTOR / image_count - 10,
        xref = "x",
        yref = "y",
        opacity = 1.0,
        layer = "above",
        sizing = "stretch",
        source = img_url
    ))
    
if image_count > 0:
    layout = go.Layout(
        xaxis = go.layout.XAxis(visible = False, range = [0, IMG_WIDTH * SCALE_FACTOR]),
        yaxis = go.layout.YAxis(visible = False, range = [0, IMG_HEIGHT * SCALE_FACTOR], scaleanchor = 'y'),
        width = IMG_WIDTH * SCALE_FACTOR,
        height = IMG_HEIGHT * SCALE_FACTOR,
        margin = {'l': 0, 'r': 0, 't': 0, 'b': 0},
        clickmode = "none",
        dragmode = False,
        images = images
    )

    fig = go.Figure(
      data = [go.Table(
        columnwidth = [10, 10, 30],
        header = dict(
          values = ['<b>Member_ID</b>', '<b>Image</b>', '<b>Child First Name</b>'],
          line = dict(color='darkslategray'),
          fill = dict(color=HEADER_COL),
          align = ['left','center', 'center'],
          font = dict(color='black', size=16)
        ),
        cells = dict(
          values = [df.member_id, df.image_url, df.child_first_name],
          height = IMG_HEIGHT * SCALE_FACTOR / image_count,
          line = dict(color='darkslategray'),
          fill = dict(color=[[ODD_ROW_COL, EVEN_ROW_COL] * 5]),
          font = dict(color = 'darkslategray', size = 14),
          align = ['left','center', 'center']
        )
      )],
      layout = layout
    )
    periscope.plotly(fig)
# periscope.table(df)
# periscope.table(df)