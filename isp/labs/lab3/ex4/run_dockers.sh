#!/usr/bin/env bash
NETWORK=172.16.0

if [ ! "$1" ]; then
	echo "Please give your email-address @epfl for the first parameter"
	exit 1
fi
EMAIL=$1
TAG=latest

stop(){
	for node in client attacker; do
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
	for node in client attacker; do
	  echo "Running container $node"
	  IP=$NETWORK.$HOST
	  img=dedis/com402_hw3_ex4_$node:$TAG
	  if [ $node = client ]; then
	  	cmd="while sleep 30; do python3 runclient.py $EMAIL; done"
	  else
	  	cmd="/bin/bash"
	  fi
	  docker run -d --net cybercafe --ip $IP -h $node -t -i --name $node -v "$(pwd)":/shared --cap-add=ALL $img /bin/sh -c "$cmd"
      if [ $node = attacker ]; then
        docker exec attacker /bin/bash -c 'iptables -t nat -A POSTROUTING -j MASQUERADE'
        docker exec attacker /bin/bash -c 'iptables -A FORWARD -s 172.16.0.2 -p tcp --dport 443 -j NFQUEUE --queue-num 0'
        echo "[+] Running attacker"
      elif [ $node = client ]; then
        docker exec client /bin/sh -c 'route del default'
        docker exec client /bin/sh -c 'route add default gateway 172.16.0.3'
        echo "[+] Running client"
      fi
	  HOST=$(( HOST + 1 ))
	done
}

stop
network
run

echo "To enter the attacker, type the following:"
echo
echo "docker attach attacker"
echo
echo "have fun."
