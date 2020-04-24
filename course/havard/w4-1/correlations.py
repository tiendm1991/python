
from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np, pandas as pd

whisky = pd.read_csv("whiskies.csv", index_col=0)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)
print(correlations)

# First, we import a tool to allow text to pop up on a plot when the cursor
# hovers over it.  Also, we import a data structure used to store arguments
# of what to plot in Bokeh.  Finally, we will use numpy for this section as well!

from bokeh.models import HoverTool, ColumnDataSource

# Let's plot a simple 5x5 grid of squares, alternating between two colors.
plot_values = [1,2,3,4,5]
plot_colors = ['#0173b2', '#de8f05']

# How do we tell Bokeh to plot each point in a grid?  Let's use a function that
# finds each combination of values from 1-5.
from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)
# The first value is the x coordinate, and the second value is the y coordinate.

# Let's store these in separate lists.
xs, ys = zip(*grid)
print(xs)
print(ys)

# Now we will make a list of colors, alternating between the two chosen colors.
colors = [plot_colors[i%2] for i in range(len(grid))]
print(colors)

# Finally, let's determine the strength of transparency (alpha) for each point,
# where 0 is completely transparent.
alphas = np.linspace(0, 1, len(grid))

# Bokeh likes each of these to be stored in a special dataframe, called
# ColumnDataSource.  Let's store our coordinates, colors, and alpha values.
source = ColumnDataSource(
    data = {
        "x": xs,
        "y": ys,
        "colors": colors,
        "alphas": alphas,
    }
)
print(alphas)

# We are ready to make our interactive Bokeh plot!
from bokeh.plotting import figure, output_file, show

# output_file("Basic_Example.html", title="Basic Example")
# fig = figure(tools="hover")
# fig.rect("x", "y", 0.9, 0.9, source=source, color="colors",alpha="alphas")
# hover = fig.select(dict(type=HoverTool))
# hover.tooltips = {
#     "Value": "@x, @y",
#     }
# show(fig)

cluster_colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#cc78bc', '#ca9161']
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]
region_colors = pd.Series(cluster_colors, index=regions)

distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i][j] < 0.7:                   # if low correlation,
            correlation_colors.append('white')         # just use white.
        else:                                          # otherwise,
            if cluster_colors[whisky.Group[i]] == cluster_colors[whisky.Group[j]]:                # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]]) # color them by their mutual group.
            else:                                      # otherwise
                correlation_colors.append('lightgray') # color them lightgray.


# source = ColumnDataSource(
#     data = {
#         "x": np.repeat(distilleries,len(distilleries)),
#         "y": list(distilleries)*len(distilleries),
#         "colors": correlation_colors,
#         "correlations": correlations,
#     }
# )

# output_file("Whisky Correlations.html", title="Whisky Correlations")
# fig = figure(title="Whisky Correlations",
#     x_axis_location="above", x_range=list(reversed(distilleries)), y_range=distilleries)
# fig.grid.grid_line_color = None
# fig.axis.axis_line_color = None
# fig.axis.major_tick_line_color = None
# fig.axis.major_label_text_font_size = "5pt"
# fig.xaxis.major_label_orientation = np.pi / 3
# fig.rect('x', 'y', .9, .9, source=source,
#      color='colors', alpha='correlations')
# hover = fig.select(dict(type=HoverTool))
# hover.tooltips = {
#     "Whiskies": "@x, @y",
#     "Correlation": "@correlations",
# }
# show(fig)

# points = [(0,0), (1,2), (3,1)]
# xs, ys = zip(*points)
# colors = ['#0173b2', '#de8f05', '#029e73']
#
# output_file("Spatial_Example.html", title="Regional Example")
# location_source = ColumnDataSource(
#     data={
#         "x": xs,
#         "y": ys,
#         "colors": colors,
#     }
# )
#
# fig = figure(title = "Title",
#     x_axis_location = "above", tools="hover, save")
# fig.plot_width  = 300
# fig.plot_height = 380
# fig.circle("x", "y", size=10, source=location_source,
#      color='colors', line_color = None)
#
# hover = fig.select(dict(type = HoverTool))
# hover.tooltips = {
#     "Location": "(@x, @y)"
# }
# show(fig)

def location_plot(title, colors):
    output_file(title+".html")
    location_source = ColumnDataSource(
        data = {
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery
        }
    )

    fig = figure(title = title,
        x_axis_location = "above", tools="hover, save")
    fig.plot_width  = 400
    fig.plot_height = 500
    fig.circle("x", "y", size=9, source=location_source, color='colors', line_color = None)
    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type = HoverTool))
    hover.tooltips = {
        "Distillery": "@distilleries",
        "Location": "(@x, @y)"
    }
    show(fig)

allRegion = whisky.Region
allCluster = whisky.Group
region_cols = [region_colors[allRegion[i]] for i in range(len(allRegion))]
classification_cols = [cluster_colors[allCluster[i]] for i in range(len(allCluster))]

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)