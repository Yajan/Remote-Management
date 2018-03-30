import chartjs
import json

memory_array = []
time_array = []
disk_array = []
with open("C:/Users/Yajana/PycharmProjects/Distributed-setup-4/Data/data.json",'r') as input:
    data = input.read()
    data = json.loads(data)
    #print(data)

for eachdata in data:
    #print(eachdata)
    time_array.append(eachdata['time'])
    memory_array.append(eachdata['memory'])
    disk_array.append(eachdata['disk'])


print(time_array,memory_array,disk_array)


mychart = chartjs.chart("System Info", "Bar", 3040, 880)
mychart.set_labels(time_array)
mychart.add_dataset(memory_array)
mychart.set_params(fillColor = "rgba(220,220,220,0.5)", strokeColor = "rgba(220,220,220,0.8)", highlightFill = "rgba(220,220,220,0.75)", highlightStroke = "rgba(220,220,220,1)",)
mychart.add_dataset(disk_array)
mychart.set_colors(['#FA0000', '#008811', '#0055FA', '#559090'])
mychart.set_highlights(['#FF0000', '#00B851', '#0055FF', '#75B0B0'])
#print(mychart.make_chart_full_html())
with open("report.html","w") as f:
    f.write(mychart.make_chart_full_html())





