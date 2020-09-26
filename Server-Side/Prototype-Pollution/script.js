function sendData() {
  let name = document.querySelector("#name").value;
  let password = document.querySelector("#password").value;

//'{"__proto__" : {"admin" : "true"}}'

// * username : "__proto__"  & password : {"admin" : "true"} 
  var userData = `{${name} : ${password}}`;
  var jsonData = JSON.parse(userData);
  var someData = { foo: "bar" };
  var obj = merge(someData, jsonData);
   if (obj.admin == "true") {
    alert("success");
  } else {
    alert(JSON.stringify(obj));
  } 
}
var merge = function (target, source) {
  for (var attr in source) {
    if (typeof target[attr] === "object" && typeof source[attr] === "object") {
      merge(target[attr], source[attr]);
    } else {
      target[attr] = source[attr];
    }
  }
  return target;
};

function clone(a) {
  return merge({}, a);
}

/*
 function sendData() {
  let name = document.getElementById("name");
  let password = document.getElementById("password");
  let display = document.querySelector(".display");

  let xhr = new XMLHttpRequest();
  let url = "backend.php";

  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
      display.innerHTML = this.responseText;
    }
  };

  var data = JSON.stringify({ name: name.value, password: password.value });
  xhr.send(data);
}
*/

/*
# Live Editor(not so efficient though)
setInterval(function () {
    $("#btn").click();
}, 100);
*/
