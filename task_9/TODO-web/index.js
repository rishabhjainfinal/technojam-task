const express = require('express');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');
const { v4: uuidv4 } = require('uuid');

const port = process.env.PORT || 5000;
app.locals.basedir = __dirname;
app.use(bodyParser.urlencoded({ extended: true }));

// Serve the static files from the React app
app.set('views', path.join(__dirname, 'views'))

// #### Api endpoints for todo lists ####
// local datavartibale to store data
const database = {}

// create new entry, take only data
app.post('/api/create',(req,res)=>{
    database[uuidv4()] = req.body.task;
    res.json(database);
    res.status(200);
})
// read all entry, takes nothing
app.get('/api/read', (req,res) => {
    res.json(database);
    res.status(200);
});
// update entry, takes id and new data 
app.post('/api/update', (req,res) => {
    database[req.body.id]=req.body.task
    res.json("ok")
    res.status(200);
});
// delete an entry, takes id of the entry
app.post('/api/delete', (req,res) => {
    delete database[req.body.id]
    res.json("ok")
    res.status(200);
});
// #### ################ ####


// Handles requests for the pages
app.get('/', (req,res) =>{
    res.sendFile(path.join(__dirname, 'views/index.html'))
    res.status(200);
});

//The 404 Routes
app.route('*')
    .get((req, res) => {
        console.log('404 page open');
        res.status(404).send(`<h1>Page not found 404 </h1>`);
    })
    .post((req, res) => {
        console.log('404 page open');
        res.status(404).send(`<h1>Page not found 404 </h1>`);
    })

app.listen(port);
console.log('App is listening on port ' + port);