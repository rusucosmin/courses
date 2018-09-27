
/*
	Run the action when we are sure the DOM has been loaded
	https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded
*/
function whenDocumentLoaded(action) {
	if (document.readyState === "loading") {
    	document.addEventListener("DOMContentLoaded", action);
	} else {  // `DOMContentLoaded` already fired
		action();
	}
}

// Apply the color cycle to boxes
function showColorCycle(cycle) {
	whenDocumentLoaded(() => {
		const plot_g = document.getElementById('plot-color-cycle');

		Array.from(plot_g.getElementsByTagName('rect')).forEach((elem) => {
			const color = cycle();
			elem.setAttribute('fill', color);
		});
	});
}

function setCharacterCountingFunction(char_counting_func, colors = () => 'rgb(240, 50, 10)') {
	const nbsp = String.fromCharCode(160); //https://stackoverflow.com/questions/5237989/nonbreaking-space

	function countCharacters() {
		// get from textarea
		const src_text = document.getElementById('input-count-text').value;
		// count characters
		const counts_relative = char_counting_func(src_text.toLowerCase());

		// Draw plot
		const plot_area = document.getElementById('plot-occurrences');
		plot_area.innerHTML = ''; // erase the plot

		const max_value = Object.values(counts_relative).reduce((cur_max, x) => Math.max(cur_max, x), 0);

		const entries = Object.entries(counts_relative);
		// sort from biggest key to smallest
		// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

		entries.sort((kva, kvb) => {
			// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
			if (kva[1] < kvb[1]) {
				return 1;
			} else {
				return -1;
			}
		});

		entries.forEach((key_and_value) => {
			const bar_container = document.createElement('div');

			const bar = document.createElement('div');
			bar.classList.add('bar');
			bar.style.height = (100*key_and_value[1]/max_value).toString() + '%';
			bar.style.background = colors();

			const text = document.createElement('label');
			text.textContent = nbsp + key_and_value[0] + nbsp; // add nbsps so that the box has the same size even with a single space inside

			const val = document.createElement('label');
			val.classList.add('label-value')
			val.textContent = key_and_value[1].toFixed(3);

			bar_container.appendChild(bar);
			bar_container.appendChild(text);
			bar_container.appendChild(val);
			plot_area.appendChild(bar_container);
		});
	}

	whenDocumentLoaded(() => {
		// count the currently entered text
		countCharacters();

		const btn = document.getElementById('btn-count-text');
		// Remove previous listener if it exists
		if (btn.hasOwnProperty('count_text_listener')) {
			btn.removeEventListener('click', btn.count_text_listener);
		}
		// Register new listener to repeat the counting when the user enters a new text
		btn.addEventListener('click', countCharacters);
		btn.count_text_listener = countCharacters;
	});
}

function plotBall(positions, color='rgb(71, 255, 195)') {
	whenDocumentLoaded(() => {
		const plot_g = document.getElementById('plot-ball');

		const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');

		const ps = 'M 0 0' + positions.map((xy) => 'L ' + xy[0].toString() + ' ' + xy[1].toString()).join(' ');

		path.style.stroke = color;
		path.setAttribute('d', ps);

		plot_g.appendChild(path);
	});
}
