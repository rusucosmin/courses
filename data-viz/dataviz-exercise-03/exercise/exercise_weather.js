
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

const TEST_TEMPERATURES = [13, 18, 21, 19, 26, 25,16];

// Part 1 - DOM

whenDocumentLoaded(() => {

	forecast = new Forecast(document.getElementById('weather-part1'));
	forecast.show();
	forecastOnline = new ForecastOnline(document.getElementById('weather-part1'));
	forecastOnlineCity = new ForecastOnlineCity(document.getElementById('weather-city'));
	// Part 1.1: Find the button + on click event
	var button = document.getElementById("btn-part1");
	button.addEventListener("click", function() {
		forecastOnline.reload();
	});

	var buttonCity = document.getElementById("btn-city");
	buttonCity.addEventListener("click", function() {
		forecastOnlineCity.setCity(document.getElementById("query-city").value);
		forecastOnlineCity.reload();
	});

	// Part 1.2: Write temperatures
	function showTemperatures(container_element, temperature_array) {
		container_element.innerHTML = temperature_array.map((temp) => {
			if (temp >= 23) return `<p class='warm'>${temp}</p>`;
			if (temp <= 17) return `<p class='cold'>${temp}</p>`;
			return `<p>${temp}</p>`;
		}).join()
	}
	//showTemperatures(document.getElementById('weather-part1'), TEST_TEMPERATURES)
});

// Part 2 - class

class Forecast {
	constructor(container) {
		this.container = container;
		this.temperature = [1, 2, 3, 4, 5, 6, 7];
	}
	toString() {
		return this.temperature.join(", ") + " " + this.container;
	}
	print() {
		console.log(this.toString());
	}
	show() {
		this.container.innerHTML = this.temperature.map((temp) => {
			if (temp >= 23) return `<p class='warm'>${temp}</p>`;
			if (temp <= 17) return `<p class='cold'>${temp}</p>`;
			return `<p>${temp}</p>`;
		}).join()
	}
	reload() {
		this.temperature = TEST_TEMPERATURES;
		this.show();
	}
}


// Part 3 - fetch

const QUERY_LAUSANNE = 'http://query.yahooapis.com/v1/public/yql?format=json&q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="Lausanne") and u="c"';

function yahooToTemperatures(url) {
	return fetch(url).then(function(response) {
		return response.json();
	});
}

yahooToTemperatures(QUERY_LAUSANNE)

class ForecastOnline extends Forecast {
	reload() {
		self = this;
		yahooToTemperatures(QUERY_LAUSANNE).then(function(json) {
			console.log(json.query.results.channel.item.forecast);
			self.temperature = json.query.results.channel.item.forecast.map((item) => ((Number(item.low) + Number(item.high)) / 2));
			console.log(self.temperature);
			self.show();
		});
	}
}

// Part 4 - interactive

class ForecastOnlineCity extends Forecast {
	setCity(city) {
		this.city = city;
	}
	show() {
		super.show();
		this.container.innerHTML += `<p>in ${this.city}</p>`
	}
	reload() {
		self = this;
		var url = `http://query.yahooapis.com/v1/public/yql?format=json&q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="${this.city}") and u="c"`;
		yahooToTemperatures(url).then(function(json) {
			console.log(json.query.results.channel.item.forecast);
			self.temperature = json.query.results.channel.item.forecast.map((item) => ((Number(item.low) + Number(item.high)) / 2));
			console.log(self.temperature);
			self.show();
		});
	}
}