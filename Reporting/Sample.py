import chartjs
import time

# Create a new chart object and set some values
mychart = chartjs.chart("Performance Matrix", "Line", 1600, 800)

# Set some basic options
mychart.set_params(barValueSpacing = 100)


actions = ['login','fileupload','logout']

timestamp = [1,5,3]







print(timestamp)

# Set labels to be the countries found in our file
mychart.set_labels(actions)

# Add three datasets for the three years
mychart.add_dataset(timestamp)
mychart.set_params(fillColor = "rgba(100,200,200,0.25)", strokeColor = "rgba(100,200,200,0.75)", pointColor = "rgba(100,200,200,0.75)")
'''mychart.add_dataset(values2011)
mychart.set_params(fillColor = "rgba(200,100,100,0.25)", strokeColor = "rgba(200,100,100,0.75)", pointColor = "rgba(200,100,100,0.75)")
mychart.add_dataset(values2010)'''



# Write sample.html
f = open("sample.html", 'w')
f.write(mychart.make_chart_full_html())
f.close()