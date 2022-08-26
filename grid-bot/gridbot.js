url = "wss://stream.bybit.com/realtime"
let socket = new WebSocket(url);

socket.onmessage = function(event) {
    console.log(event);
}

socket.send('{"op":"ping"}');