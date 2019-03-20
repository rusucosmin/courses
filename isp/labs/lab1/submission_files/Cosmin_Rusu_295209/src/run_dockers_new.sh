#!/usr/bin/env bash
NETWORK=172.16.0

if [ ! "$1" ]; then
	echo "Please give your email-address @epfl for the first parameter"
	exit 1
fi
EMAIL=$1
TAG=2

stop(){
	for node in generator attacker; do
	  echo "Stopping $node"
	  if docker ps | grep -q $node; then
		docker kill $node > /dev/null
	  fi
	  if docker ps -a | grep -q $node; then
		docker rm $node > /dev/null
	  fi
	done
}

network(){
	echo "Restarting network"
	docker network rm cybercafe > /dev/null
	docker network create --subnet $NETWORK.0/24 --gateway $NETWORK.254 cybercafe > /dev/null
}

run(){
	HOST=2
	for node in generator attacker; do
	  echo "Running container $node"
	  IP=$NETWORK.$HOST
	  img=dedis/com402_hw1_ex3_$node:$TAG
	  if [ $node = generator ]; then
	  	cmd="while sleep 1; do python3 tmp189.pyc $EMAIL; done"
	  else
	  	cmd="/bin/bash"
	  fi
	  docker run -d --net cybercafe --ip $IP -h $node -t -i --name $node -v "$(pwd)":/shared --cap-add=ALL $img /bin/sh -c "$cmd"
      if [ $node = attacker ]; then
        docker exec attacker /bin/bash -c 'iptables -t nat -A POSTROUTING -j MASQUERADE'
        docker exec attacker /bin/bash -c 'iptables -A FORWARD -s 172.16.0.2 -p tcp --dport 80 -j NFQUEUE --queue-num 0'
    else
        docker exec generator /bin/sh -c 'route del default'
        docker exec generator /bin/sh -c 'route add default gateway 172.16.0.3'
    fi
	  HOST=$(( HOST + 1 ))
	done
}

stop
network
run

echo "To enter the attacker, type the following:"
echo
echo "docker exec -ti attacker /bin/bash"
echo
echo "have fun."
