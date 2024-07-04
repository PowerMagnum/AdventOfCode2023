const express = require("express");
const serverExpress = express();
const serverHttp = require("http").Server(serverExpress);
const serverSocketIO = require("socket.io")(serverHttp);

serverExpress.use(express.static("./www"));

serverSocketIO.on("connect", (socketClient) => {
    console.log("suca");

    socketClient.on("disconnect", () => {
        console.log("desuca");
    });

    socketClient.on("sucaaa", () => {
        console.log("Sucaaa");
        //socketClient.broadcast.emit("BohBroadcast"); //Invia agli altri client
        serverSocketIO.sockets.emit("BohBroadcast", "Pesce", "Stocco");   //Invia a tutti
    });
});

serverHttp.listen(8080);
