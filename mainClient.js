let suca;
function connect(){

    const socket = io();
    //console.log(socket);

    socket.on("connect", async () => {
        console.log("Connesso");
    });

    socket.on("disconnect", () => {
        console.log("desuca");
    })

    socket.on("BohBroadcast", (p, s) => {
        console.log("BohBroadcast" + p + s);
    })

    suca = function(){
        socket.emit("sucaaa");
    }

}