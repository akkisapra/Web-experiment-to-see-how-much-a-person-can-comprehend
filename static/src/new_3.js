
var radios = document.forms["quiz"].elements["question1"];
        for(var i = 0, max = radios.length; i < max; i++) {
            radios[i].onclick = function() {
                if (this.value != "Scatter Plot"){
                    alert("You have chosen wrong option, Pick again");
                }

            }
}
var radios = document.forms["quiz"].elements["question2"];
        for(var i = 0, max = radios.length; i < max; i++) {
            radios[i].onclick = function() {
                if (this.value != "False"){
                    alert("You have chosen wrong option, Pick again");
                }

            }
}
var radios = document.forms["quiz"].elements["question3"];
        for(var i = 0, max = radios.length; i < max; i++) {
            radios[i].onclick = function() {
                if (this.value !== "2"){
                    alert("You have chosen wrong option, Pick again");
                }

            }
}


//var a1= document.quiz.question1.value;
//var a2= document.quiz.question2.value;
//var a3= document.quiz.question3.value;
//
//var cor =0;
//
//if a1=='Line Graph'{
//    cor++;
//}
//if a2 == 'True'{
//    cor++;
//}
//if a3===1{
//    cor++;
//}
//console.log(cor)