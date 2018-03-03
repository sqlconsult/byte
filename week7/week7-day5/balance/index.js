
console.log('Start...');

var express = require('express');

var app = express();

// This is a comment
app.get('/', function (req, res) {
    res.send('Thanks for the GET request, homie');
});

app.post('/', function (req, res) {
    res.send('Thanks for the POST request, homie.');
});

app.listen(3000, function(){
    console.log('start: listening on port 3000...');
})