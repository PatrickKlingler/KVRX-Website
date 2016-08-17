//Class for KVRX player
class KVRXPlayer {
	constructor() {
		//Create player audio element
		console.log("Creating player element");
		this.audioElement = document.createElement('audio');
		this.audioElement.setAttribute("preload", "auto");
		this.audioElement.setAttribute("title", "KVRX Livestream");
		this.audioElement.autobuffer = true;
		
		//Add player source and properties to element
		console.log("Adding player source");
		var source1 = document.createElement('source');
		source1.type = 'audio/mpeg';
		source1.src = 'http://tstv-stream.tsm.utexas.edu:8000/kvrx_livestream';
		this.audioElement.appendChild(source1);
		
		//Load the player
		console.log("Loading player");
		this.audioElement.load;
	}
	play() {
		console.log("Playing the tunes");
		this.audioElement.play();
	}
	pause() {
		console.log("Pausing the tunes");
		this.audioElement.pause();
	}
}

//Create new instance of the KVRX player
console.log("Instantiating new player class");
var player = new KVRXPlayer();

function play() {
	document.getElementById('buttonholder').innerHTML = '<a onclick="pause()"><span class="glyphicon glyphicon-pause"></span></a>'
	player.play();
}
function pause() {
	document.getElementById('buttonholder').innerHTML = '<a onclick="play()"><span class="glyphicon glyphicon-play"></span></a>'
	player.pause();
}