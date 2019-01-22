# A network topology analysis of the airline industry

## About the Repository

This repository contains our work for the A Network Tour of Data Science
course. The notebook 'Airline Analysis' contains our code for the original
part of the course. 

## About the project

The network of airlines spans the entire globe and enables us to travel from Greenland to Australia with only a few stops in-between. This network is composed of subnetworks corresponding to individual airlines. In this project, we analyze these airline networks to gain insight into what the structure of an airline’s flight network tells us about the airline. We discover how the topology of airline networks correlates with their price class and geographical location. We also discover that these same topological features in combination with robustness measures strongly correlate with the airlines average delay times. Using this information, we find competitors and give recommendations on how airlines could form strategic partnerships to increase their competitive advantage, by increasing the robustness and reach of their network.


## How to run the code

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
