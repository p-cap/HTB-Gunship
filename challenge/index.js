const express       = require('express');
const app           = express();
const routes        = require('./routes');
const path          = require('path');


app.use(express.json());
app.set('views','./views');

// To serve static files such as images, CSS files, and JavaScript files, use the express.static built-in middleware function in Express.
// https://expressjs.com/en/starter/static-files.html
app.use('/static', express.static(path.resolve('static')));


app.use(routes);
// app.all('*', (req, res) => {
//     return res.status(404).send('404 page not found');
// });

app.listen(1555, () => console.log('Listening on port 1555'));