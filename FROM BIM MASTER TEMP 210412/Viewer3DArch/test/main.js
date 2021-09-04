// const myHeading = document.querySelector('h1')
// myHeading.textContent = 'Hello world'

// let iceCream = 'chocolate';
// if(iceCream === 'chocolate') {
//   alert('Yay, I love chocolate ice cream!');
// } else {
//   alert('Awwww, but chocolate is my favorite...');
// }

// //// EVENT
// document.querySelector('html').onclick = function() {
//     alert('Ouch! Stop poking me!');
// }

let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'img1.jpg') {
      myImage.setAttribute('src','img2.jpg');
    } else {
      myImage.setAttribute('src','img1.jpg');
    }
}

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h2');


function setUserName() {
  let myName = prompt('Please enter your name.');
  if(!myName) {
    setUserName();
  } else {
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Hello, ' + myName;
  }
}

if(!localStorage.getItem('name')) {
    setUserName();
    } else {
    let storedName = localStorage.getItem('name');
    myHeading.textContent = 'Hello, ' + storedName;
    }
myButton.onclick = function() {
    setUserName();
  }