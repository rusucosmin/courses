$(document).ready(() => {
  var width = $(".column").width();
  var height = 620;
  var projection = d3.geoMercator()
    .scale(110)
    .translate([width / 2, height/ 2]);

  var path = d3.geoPath()
    .pointRadius(2)
    .projection(projection);

  var svg = d3.select("#map")
    .attr("class", "main")
    .attr("width", width)
    .attr("height", height);

  // Define the div for the tooltip
  var tooltip = d3.select("body").append("div")	
    .attr("class", "tooltip")				
    .style("opacity", 0);

  d3.json("data/countries.topo.json").then(function(countries) {
    d3.json("data/nodes.json").then(function(airports) {
      d3.json("data/edges.json").then(function(flights) {
        svg.append("rect")
          .attr("class", "background")
          .attr("width", width)
          .attr("height", height);

        svg.append("g")
          .attr("class", "countries")
          .selectAll("path")
          .data(topojson.feature(countries, countries.objects.countries).features)
          .enter()
          .append("path")
          .attr("d", path);

        var airports_geos = airports.map(node => {
          return {
            type: "Feature",
            properties: {
              AirportID: node.AirportID,
              Altitude: node.Altitude,
              City: node.City,
              Country: node.Country,
              DST: node.DST,
              IATA: node.IATA,
              ICAO: node.ICAO,
              Latitude: node.Latitude,
              Longitude: node.Longitude,
              Name: node.Name,
              Source: node.Source,
              Timezone: node.Timezone,
              Type: node.Type,
              TzDatabaseTimeZone: node.TzDatabaseTimeZone,
              node: node.node
            },
            geometry: {
              type: "Point",
              coordinates: [node.Longitude, node.Latitude]
            },
          }
        });

        nodePropertiesHTML = (node) => {
          return "Name: " + node.Name + "<br>" +
              "IATA: " + node.IATA + "<br>" +
              "City: " + node.City + "<br>" + 
              "Country: " + node.Country + "<br>" +
              "node: " + node.node + "<br>"
        }

        var flights_geos = flights.splice(0, 10000).map(edges => {
          source = airports[edges.node_source]
          target = airports[edges.node_dest]
          return {
            type: "LineString",
            coordinates: [[source.Longitude, source.Latitude], [target.Longitude, target.Latitude]]
          }
        })

        var flights = svg.append("g")
          .attr("class", "flights")
          .selectAll("path")
          .data(flights_geos)
          .enter()
          .append("path")
          .attr("class", "route")
          .attr("d", path);

        svg.append("g")
          .attr("class", "airports")
          .selectAll("path")
          .data(airports_geos)
          .enter()
          .append("path")
          .attr("d", path)
          .on("mouseover", function(d) {		
            tooltip.transition()		
              .duration(100)		
              .style("opacity", .9);		
            tooltip.html(nodePropertiesHTML(d.properties)	)
              .style("left", (d3.event.pageX) + "px")		
              .style("top", (d3.event.pageY - 28) + "px");	
            })					
          .on("mouseout", function(d) {		
            tooltip.transition()		
              .duration(500)		
              .style("opacity", 0);	
          });
      });
    })
  });
});