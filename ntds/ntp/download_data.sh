echo "Getting airports data"
curl https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat 2&>/dev/null > airports.dat
echo "Getting airlines data"
curl https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat 2&>/dev/null > airlines.dat
echo "Getting routes data"
curl https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat 2&>/dev/null > routes.dat
echo "Getting planes data"
curl https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat 2&>/dev/null > planes.dat

