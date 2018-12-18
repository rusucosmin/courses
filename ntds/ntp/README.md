# ntp
Network Tour Project ✈️

## TODO
* Add charts for analysing central quantities
  a. Graph visualisation (bonus with maps)
  b. Add scatter plot for probabilities of outbound and inbound degree
  c. Add plot for the probability of the number of stops of flights
  d. Plot Clustering coefficient


*Proposition*: for data interpretation look at whether the data indicates that flight routes data indicates that it is a random network (even if we know it won't match) and to check for the scale free network property.

## Install

```
# Clone the repository
git clone https://github.com/rusucosmin/ntp
# Create the conda environment
conda env create -f ntp/environment.yml
# Activate the environment
conda activate ntp
# Open a notebook
cd ntp
jupyter notebook
```

## Flight Routes
By Rodrigo

Resources:
* <https://openflights.org/data.html#route>
* <https://openflights.org/data.html>

This OpenFlights/Airline Route Mapper Route Database contains 67,663 routes (EDGES) between 3,321 airports (NODES) on 548 airlines spanning the globe.

The construction of the graph is facilitated by the source and destination airports of each flight, which gives essentially an edge list for the airport graph. Students could complement the graph construction by providing weigths to the edges, proportional to the number of flights connecting the corresponding pair of airports. The visualization of the graph embedded on the globe can be achieved by using the supplemented data in https://openflights.org/data.html, which contains, among others, information on latitute/longitude of each airport. A potential goal of the extra work could then be comparing the embedding produced by the Laplacian eigenmaps algorithm seen in the course and the "natural" embedding given by the terrestrial coordinates. The most sensitive part of the project (which could be examined in the extra work) would be to find a label signal on the graph that could be recovered via a label propagation algorithm on the graph. In principle, the average number of stops of flights leaving each airport could fulfill this purpose, but it remains a metter of study whether a subsampled version of this information can be recovered from the topological information of the graph alone or not.

|          | Description                                 | Amount |
| -------- | ------------------------------------------- | -----: |
| nodes    | airports                                    |  3,321 |
| edges    | count of flights connecting airports        | 67,663 |
| features | average number of stops of outbound flights |      1 |
| labels   | N/A                                         |    N/A |

* **Data acquisition**: already collected and packaged
* **Requires down-sampling**: no
* **Network creation**: network is essentially given (list of edges)
