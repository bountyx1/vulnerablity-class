# Prototype Pollution

## Objects

---

- Ways to create objects

  ```javascript
  let obj1 = {}

  let person1 = new Object();
  as instance
  let foo = Object.create(null)
  ```

- Object Created with .create function dont have prototype/constructor safe from prototype pollution

- Using Object Constructor

```javascript
let person1 = new Object({
  name: 'Chris',
  age: 38,
  greeting: function() {
    alert('Hi! I\'m ' + this.name + '.');
  }
});

```

- Using Constructor
- creating an object instance from a class is called instantiation
- This reference to object itself eg this=person

proto type is like we create objects in javascript ?

every object we create has a special property attached to it  
yea i read about these in java , is it similary to that
like every object in java have toString propery , hash , equals , and some more??

n

```javascript
var person: {name:1 ,
greeting: function() {
  alert('Hi! I\'m ' + this.name.first + '.');
}

}
```

- Constructor Function
- A constructor function name usually starts with a capital letter — this convention is used to make constructor functions easier to recognize in code.

```javascript
function Person(name) {
  this.name = name;
  this.greeting = function() {
    alert('Hi! I\'m ' + this.name + '.');
  };
}
var teacher = new Person("Navjeet")
teacher.name;
```

## Prototypes

- Object in js has internal p"aaaa".constructorroperty called prototype
- it is reference to another object and contain property/methods
- eg when we create string string() constructor is called and create our string and it shares that STRING() object properties like x.tostring() xyz

```javascript
var x = "string"
x.toString()
x.__proto__
```

- eg 2 The Array object has a prototype Array.prototype and the object instance, num, inherits the properties of the Array object.

```javascript
let numArray = [1,2,-8,3,-4,7];

```

## Prototype chain

- create person constructor it has two

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}
console.log(Person.prototype)

// constuctor
// __proto__
console.log(Person.prototype.constuctor)
//constuctor -- points to above function we created
Person.prototype.constructor === Person
Person.prototype === Person.prototype.constructor.prototype
```

- defined our constructor function Person.
- added methods to its prototype object.
- When we add functions or properties (you also can add properties) to the any function’s prototype object it will be available to its instances through the prototype object.

```javascript

function Person(name, age) {
  this.name = name;
  this.age = age;
}
Person.prototype.eat = function () {
    console.log(`${this.name} is eating.`)
}
Person.prototype.sleep = function () {
    console.log(`${this.name} is sleeping.`)
}
Person.prototype.walk =function () {
    console.log(`${this.name} is walking.`)
}

const bob = Person("navjeet",21)

```

- We created an object called Bob with two attributes using the Person function with the new keyword.
- Then behind the scene from the JavaScript engine, it adds a new property called **proto** to that instance which is a getter/setter for the above Function’s prototype object. (Hope you read my article on Constructor Functions in JavaScript if you are not familiar with JavaScript constructor functions.)

- Polluting global object

```javascript
var x = {};
var y = {};
//both same
x.__proto__ === y.constructor.prototype;

x.__proto__.test="hello";
x.test;
y.test;
// x,y object output hello as inheritence as we wrote in global variable
```

- function constructor

```javascript
function Person(name) {this.name=name}
var x = new Person("navjeet")
x.constructor == Person
x.constructor.prototype.constructor.prototype.constructor.prototype.constructor.prototype.constructor === Person
so on goes


Person.prototype.eat = function() { console.log("hello world")}
x.eat === x.constructor.prototype.eat
```

- Overwridding functions

```javascript
"hello".constructor.prototype.toString = function () {console.log("hello world")}

"aa".toString()

```

- Object merge
- second argument has more priority

