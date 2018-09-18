net = require('net');
exec = require('child_process').exec;

net.createServer(function (socket) {
    socket.name = socket.remoteAddress + ":" + socket.remotePort
    console.log("LOG > " + socket.name + " connected");

    socket.on('data', function(data) {
        console.log("LOG > executing " + data);
        execCmd(socket, data);
    });

    socket.on('end', function(data) {
        console.log("LOG > " + socket.name + " disconnected");
    });

    socket.on('error', function(err) {
        console.log("ERROR > " + err);
    });

    function execCmd(socket, data) {
        exec(data, function(err, stdout, stderr) {
            if(err) {
                console.error("ERROR > execCmd: " + err);
                socket.write("ERROR > execCmd " + data + "\n"  + err);
                return ;
            }
            console.log("LOG > cmd " + data + " ended");
            socket.write("stdout: " + stdout + "\nstderr: " + stderr);
        });
    }
}).listen(5001);

console.log("Command execution server running at port 5001\n");
