
var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);


app.get('/', function (req, res) {
    //res.send('<h3>Hello World</h3>');
    res.sendFile(__dirname + '/index.html')
});


io.on('connection', function(socket){
    // console.log('It\'s Mr. Steal Your Girl... O-o-o-ooo');
    console.log('Server: A user has entered a chat room');
    socket.on('disconnect', function(){
        console.log('Server: A user has disconnected from a chat room');
        //console.log('Server: ...also... a member of AC/DC was arrested for selling meth');
    });
});


io.on('connection', function(socket){
    socket.on('chat message', function(msg){
       console.log('message: ' + msg);
       io.emit('chat message', msg);
    });
});


http.listen(3000, function (){
    console.log('Server: listening on port 3000...')
});
