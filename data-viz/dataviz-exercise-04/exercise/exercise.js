


/*
	Run the action when we are sure the DOM has been loaded
	https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded
	Example:
	whenDocumentLoaded(() => {
		console.log('loaded!');
		document.getElementById('some-element');
	});
*/
function whenDocumentLoaded(action) {
	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", action);
	} else {
		// `DOMContentLoaded` already fired
		action();
	}
}

const TEST_TEMPERATURES = [13, 18, 21, 19, 26, 25, 16];
const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
data = []
for(var i = 1; i <= 7; ++ i) {
	data.push({
		x: i,
		y: TEST_TEMPERATURES[i],
		name: DAYS[i],
	})
}

//const MARGIN = { top: 10, right: 10, bottom: 10, left: 10 };

class ScatterPlot {
	constructor(elementId, data) {
		this.elementId = elementId;
		this.data = data;
		this.draw();
	}
	draw() {
		var svg = d3.select(`#${this.elementId}`);
		var x = d3.scaleLinear()
			.domain([d3.min(this.data, (data) => data.x), d3.max(this.data, (data) => data.x)])
			.range([0, 200])
		var y = d3.scaleLinear()
			.domain([d3.min(this.data, (data) => data.y), d3.max(this.data, (data) => data.y)])
			.range([100, 0])
		var xAxis = d3.axisBottom(
			d3.scalePoint()
				.domain(DAYS)
				.range([0, 200]));
		var yAxis = d3.axisLeft(y);
		svg
			.append('g')
			.attr('transform', `translate(0, 95)`)
			.call(xAxis);
		svg
			.append('g')
			.attr('transform', `translate(0, 0)`)
  		.call(yAxis);
		svg.append("g")
			.selectAll("circle")
			.data(this.data)
			.enter()
			.append("circle")
				.attr("cx", (data) => x(data.x))
				.attr("cy", (data) => y(data.y))
				.attr("class", function(data) {
					if(data.y <= 17) return "cold";
					if(data.y >= 23) return "warm";
					return "";
				})
				.attr("r", 2.5);
	}
}

whenDocumentLoaded(() => {

	// prepare the data here

	//console.log(data);

	const plot = new ScatterPlot('plot', data);
});

