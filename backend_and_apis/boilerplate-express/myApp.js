let express = require("express");
let app = express();
require("dotenv").config(); // initialise .env files
let bodyParser = require("body-parser"); // alllows parsing url encoded data

console.log("Hello World");
// middleware functions
// NOTE: As usual, the middleware must be mounted before all the routes that depend on it.
app.use(function (req, res, next) {
  console.log(`${req.method} ${req.path} - ${req.ip}`);
  next();
});
app.use(bodyParser.urlencoded({extended: false}))
// / - send file
app.get("/", function (req, res) {
  absolutePath = __dirname + "/views/index.html";
  // res.send("'Hello Express'");
  res.sendFile(absolutePath);
});
// /public
app.use("/public", express.static(__dirname + "/public"));
app.get("/public", function (req, res) {
  absolutePath = __dirname + "/views/index.html";
  res.sendFile(absolutePath);
});
// /json - json and env handling
app.get("/json", function (req, res) {
  message = "Hello json";
  if (process.env.MESSAGE_STYLE == "uppercase") {
    res.json({ message: message.toUpperCase() });
  } else {
    res.json({ message: message });
  }
});
// /now - middleman functions
app.get('/now', function(req, res, next){ // middleman function
  req.time = new Date().toString()
  next();
}, function(req, res){ // function following middleman function
  res.json({ time: req.time });
})
// /echo - paramaters
app.get("/:word/echo", function(req, res){
  res.json({ "echo": req.params.word });
})
// /name - queries and posts
// NOTE: /name route path. If you want, you can use the
// method app.route(path).get(handler).post(handler)
//
app.route("/name")
.get(function(req, res){ // get requests
  res.json({ name: `${req.query["first"]} ${req.query["last"]}`});
})
.post(function(req, res){ // post requests
  let body = req.body;
  res.json({ name: `${body["first"]} ${body["last"]}`});
})

module.exports = app;
