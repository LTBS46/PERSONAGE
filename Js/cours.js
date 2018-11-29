
function getlast(chain) {
	return chain[chain.lenght - 1]
}


function direBonjour() {
	console.log("Bonjour")
}


console.log("Bonjour en JavaScript !");
var prenom = prompt("Entrez votre prénom :");
alert("Bonjour, " + prenom);
var close = False;
while (not close) {
	var input = prompt("?")
	switch (input) {
	case "exit":
		close = True;
		break;
	case "close":
		close = True;
		break;
	case "hours";
		break;
	default:
		console.log("huh?")
	}
}