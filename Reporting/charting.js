d3.csv("Data/performance-data.csv", function (error, data) {
    if (error) throw error;
    // format the data

    // set the dimensions and margins of the graph
    var margin = { top: 20, right: 20, bottom: 30, left: 50 },
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);

    // define the line
    var memoryline = d3.line()
        .x(function (d) { return x(d.time); })
        .y(function (d) { return y(d.memory); });

    var diskline = d3.line()
        .x(function (d) { return x(d.time); })
        .y(function (d) { return y(d.disk); });

    var cpuline = d3.line()
        .x(function (d) { return x(d.time); })
        .y(function (d) { return y(d.cpu); });

    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g").attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    // get data
    data.forEach(function (d) {
        d.time = +d.time;
        d.memory = +d.memory;
        d.disk = +d.disk;
        d.cpu = +d.cpu
        console.log(d.time, d.disk, d.memory, d.cpu)

        // Scale the range of the data
        x.domain(d3.extent(data, function (d) { return d.time; }));
      
        y.domain([0, d3.max(data, function (d) { return d.memory; })]);

        // Add the valueline path.
        svg.append("path")
            .data([data])
            .attr("class", "memoryline")
            .attr("d", memoryline);

        svg.append("path")
            .data([data])
            .attr("class", "diskline")
            .attr("d", diskline);

        svg.append("path")
            .data([data])
            .attr("class", "cpuline")
            .attr("d", cpuline);

        // Add the X Axis
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));


        // Add the Y Axis
        svg.append("g")
            .call(d3.axisLeft(y));
    });

});

d3.csv("Data/processdata.csv", function (error, data) {
    if (error) throw error;
    // format the data

    // set the dimensions and margins of the graph
    var margin = { top: 20, right: 20, bottom: 30, left: 50 },
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);

    // define the line
    var memoryline = d3.line()
        .x(function (d) { return x(d.time); })
        .y(function (d) { return y(d.memory); });


    var cpuline = d3.line()
        .x(function (d) { return x(d.time); })
        .y(function (d) { return y(d.cpu); });

    // append the svg obgect to the body of the page
    // appends a 'group' element to 'svg'
    // moves the 'group' element to the top left margin
    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g").attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    // get data
    data.forEach(function (d) {
        d.time = +d.time;
        d.memory = +d.memory;
        d.disk = +d.disk;
        d.cpu = +d.cpu
        console.log(d.time, d.disk, d.memory, d.cpu)

        // Scale the range of the data
        x.domain(d3.extent(data, function (d) { return d.time; }));

        y.domain([0, d3.max(data, function (d) { return d.memory; })]);

        // Add the valueline path.
        svg.append("path")
            .data([data])
            .attr("class", "memoryline")
            .attr("d", memoryline);


        svg.append("path")
            .data([data])
            .attr("class", "cpuline")
            .attr("d", cpuline);

        // Add the X Axis
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x));


        // Add the Y Axis
        svg.append("g")
            .call(d3.axisLeft(y));
    });

});
