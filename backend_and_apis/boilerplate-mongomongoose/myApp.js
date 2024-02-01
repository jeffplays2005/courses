let mongoose = require("mongoose");
require("dotenv").config();
// connect to database
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
// Create default "person" schema
const personSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  age: { type: Number },
  favoriteFoods: { type: [String] } // list of strings
})
// assign a new person model to "Person"
let Person = mongoose.model('Person', personSchema);
// make a new person and save
const createAndSavePerson = (done) => {
  testPerson = new Person({
    name: "Test person",
    age: 19,
    favoriteFoods: [ "pizza", "burgers" ]
  })
  testPerson.save((err, data) => {
    if(err) done(err)
    done(null, data)
  })
};

var arrayOfPeople = [
  {name: "bob", age: 45, favoriteFoods: ["apple"]},
  {name: "tim", age: 62, favoriteFoods: ["pear"]},
];
// store multiple objects of people using a list and then saving
const createManyPeople = (arrayOfPeople, done) => {
  Person.create(arrayOfPeople, (err, data) => {
    if(err) return done(err)
    done(null, data)
  })
};
// find a person based on the name, returns a list
const findPeopleByName = (personName, done) => {
  Person.find({ name: personName }, (err, data) => {
    if(err) return done(err)
    done(null, data);
  })
};
// find a single person based on their favorite food, this only returns one person if found
// good for searching unique values
const findOneByFood = (food, done) => {
  Person.findOne({ favoriteFoods: food }, (err, data) => {
    if(err) return done(err)
    done(null, data);
  })
};
// search for a person by their unique alphanumeric id
const findPersonById = (personId, done) => {
  Person.findById({ _id: personId }, (err, data) => {
    if(err) return done(err);
    done(null, data);
  })
};
// find someone by the specific id and change the favorite food key to store an extra item in
// the array
const findEditThenSave = (personId, done) => {
  const foodToAdd = "hamburger";
  // search for person by their unique mongo id
  Person.findById({ _id: personId }, (err, person) => {
    // push into their favorite foods
    person.favoriteFoods.push(foodToAdd);
    // update and save the data
    person.save((err, data) => {
      if(err) return done(err)
      done(null, data)
    });
  })
};
// find by a key and set and callback
const findAndUpdate = (personName, done) => {
  const ageToSet = 20;
  Person.findOneAndUpdate({ name: personName }, { age: ageToSet }, { new: true }, (err, updatedPerson) => {
    if(err) return done(err);
    done(null, updatedPerson);
  })
};
// remove by target id or by finding by specific arguments
const removeById = (personId, done) => {
  // option 1 <model>.findByIdAndRemove
  // Person.findByIdAndRemove({_id: personId}, (err, callback) => {
  //   if(err) return done(err)
  //   done(null, callback)
  // });
  // option 2 <model>.findOneAndRemove
  Person.findOneAndRemove({_id: personId}, (err, callback) => {
    if(err) return done(err)
    done(null, callback)
  });
};
// remove bulk using <model>.remove
const removeManyPeople = (done) => {
  const nameToRemove = "Mary";
  Person.remove({ name: nameToRemove }, (err, callback) => {
    if(err) return done(err)
    done(null, callback)
  })
};
// creating a query and chaining search methods
const queryChain = (done) => {
  const foodToSearch = "burrito";
  // store data to variable
  let fetchedData = Person.find({ favoriteFoods: foodToSearch })
  .sort({ name: "asc" })
  .limit(2)
  .select("-age")
  .exec((err, callback) => {
    if(err) return done(err)
    done(null, callback)
  })
  // done(null, fetchedData.exec())
};

/** **Well Done !!**
/* You completed these challenges, let's go celebrate !
 */

//----- **DO NOT EDIT BELOW THIS LINE** ----------------------------------

exports.PersonModel = Person;
exports.createAndSavePerson = createAndSavePerson;
exports.findPeopleByName = findPeopleByName;
exports.findOneByFood = findOneByFood;
exports.findPersonById = findPersonById;
exports.findEditThenSave = findEditThenSave;
exports.findAndUpdate = findAndUpdate;
exports.createManyPeople = createManyPeople;
exports.removeById = removeById;
exports.removeManyPeople = removeManyPeople;
exports.queryChain = queryChain;
