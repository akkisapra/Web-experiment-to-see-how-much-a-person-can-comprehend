
var radios = document.forms["quiz"].elements["question1"];
        for(var i = 0, max = radios.length; i < max; i++) {
            radios[i].onclick = function() {
                if (this.value != "Node Link Diagram"){
                    alert("You have chosen wrong option, Pick again");
                }

            }
}
var radios = document.forms["quiz"].elements["question2"];
        for(var i = 0, max = radios.length; i < max; i++) {
            radios[i].onclick = function() {
                if (this.value != "True"){
                    alert("You have chosen wrong option, Pick again");
                }

            }
}
var radios = document.forms["quiz"].elements["question3"];
        for(var i = 0, max = radios.length; i < max; i++) {
            radios[i].onclick = function() {
                if (this.value !== "4"){
                    alert("You have chosen wrong option, Pick again");
                }

            }
}
