//Make calls to the Python Django Server
//Authors: Justin Ross and Emma Brunell

//Check if the "Crack" button was clicked. If it was, execute callPython()
document.getElementById("cracked").addEventListener("click", function(){
				callPython()},true);
									
	function callPython(){
	//console.log("Called");
	//Parse the text data and send a request with custom query parameters
		var query = document.getElementById("myText").value;
		var url = "http://127.0.0.1:8000/crack?pass="+query;
		if(query != ""){
			//console.log(url);
			var xhttp;
			xhttp = new XMLHttpRequest();
			xhttp.onreadystatechange = function() {
				//If the server responds with a ready state, write the results
				//On the page. If not, show the user that the server is currently cracking your password
				if (xhttp.readyState== 4) {
					document.getElementById("stat").innerHTML = "";
					//console.log(xhttp.responseText);
					var obj = JSON.parse(xhttp.responseText);
					//console.log(obj);
					document.getElementById("pass").innerHTML = obj.password;
					document.getElementById("att").innerHTML = obj.attempts;						
				}else{
					document.getElementById("stat").innerHTML = "Cracking";
				}
			}				
		};
		//Send the get request
		xhttp.open("GET", url, true);
		xhttp.send();
	}