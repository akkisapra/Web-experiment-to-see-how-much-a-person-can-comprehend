var prev
var rad = document.getElementsByName('mygroup1');
	prev = document.getElementById('never');
	
	for (var i = 0; i < rad.length; i++) {
		rad[i].addEventListener('change', function() {
			(prev) ? console.log(prev.value): null;
			if (this !== prev) {
				if(this.value == 'seldom' || this.value == 'often') {
					document.getElementById('elaboration_wrapper').style.visibility = "visible";
				}
				else {
					document.getElementById('elaboration_wrapper').style.visibility = "hidden";
				}
				prev = this;
			}
			console.log(this.value)
		});
	}

