let wsearch = window.location.search;
let param = new URLSearchParams(wsearch).get("username");

/*  
    # DOM-XSS using XHR
     var xhr = new XMLHttpRequest();
     xhr.onreadystatechange = function(){
         if(this.readyState == 4 && this.status == 200){
             document.getElementById("demo").innerHTML = "<p>Hello : " + param + "</p>";
             eval(`var test = '${param}'`);
            someFunc(test);
        }
    
     };
     xhr.open("GET","index.html", true);
     xhr.send();

     function someFunc(t){
         let elem = document.getElementById("demo");
         element.onEvent()                                                //* onEvent() => onclick , onload, onerror , etc.
         elem.insertAdjacentHTML('beforebegin', param);                  //* Node.insertAdjacentHTML(position , text) :-> positions : beforebegin , beforeend ;
         elem.outerHTML = t;
         elem.innerHTML = t;
         document.writeln(t);
         elem.innerText = " search results for '" + t + "'";
         document.body.appendChild(h1); 
     }
*/

//# DOM-XSS based append child
// let p = document.createElement('p');
// p.innerHTML = "Hello : " + param;
// document.body.appendChild(p);

//# DOM-XSS based on jQuery function
// $(document).ready(function(){
//     $("#back-btn").attr("href",param);
// })

//# DOM-XSS based on innerHTML
// let val = document.getElementById("p-tag");
// val.innerHTML = "Welcome " + param;
