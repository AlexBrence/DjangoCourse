var fname = prompt("Enter your first name");
var lname = prompt("Enter your last name");
var age = prompt("Enter your age");
var height = prompt("Enter your height in cm");
var petName = prompt("Enter your pet name");
alert("Thank you for your information!");

var isSpy = fname[0] === lname[0] &&
            age > 20 && age < 30 &&
            height >= 170 &&
            petName.slice(-1) === 'y';

if (isSpy) {
  console.log("Welcome " + fname + "! You've passed the Spy Test");
}
