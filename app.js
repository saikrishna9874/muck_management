const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');
const cors = require('cors');
const fs = require('fs');
const port = 4000;
app.use(bodyParser.json());
app.use(cors());
const {PythonShell} = require('python-shell')
// set public folder for views

app.use(express.static(path.join(__dirname,'./muck/build')));

app.post('/',function(request,response) {
    let k = request.body;
   fs.writeFile('params.txt',k.inputValue,(err) => {
    if (err) throw err;
    console.log('Saved!');
   });
   PythonShell.run('main.py', null, function (err) {
    if (err) throw err;
    console.log('finished');
  });
   response.send({success: true});
});


app.listen(port,() => {
    console.log('Server started on port 4000');
    });