

var webSocket;
var WebSocket1	;

var usr;
var usr1;
$(function(){
	webSocket= new WebSocket("ws://localhost:8080/ws");
	$('#userbtn').click(function(e){
		usr = $("#username").val()
		$("#user").html("Welcome "+usr)

	})
	$('#send').click(function(e){
		var msg = $("#chatInput").val()
        //var to = self.get
		//webSocket.send(msg)
		webSocket.send(JSON.stringify({
   			id: usr,
   			messag: msg
		}));

		$("#chatInput").val('')
	})

	webSocket.onmessage = function(e){
		console.log(e.data)
		var obj =JSON.parse(e.data);
		$("#chatContent").append("</br>"+obj.id+":"+obj.messag+"</br>")
	}
	webSocket.onclose = function(e){
		 console.log(e);
	}
})

// New WebSocket for each new joinned member
$(function(){
	webSocket1= new WebSocket("ws://localhost:8080/ws1");

	$('#userbtn').click(function(e){
		usr1 = usr
		console.log(usr1)
		webSocket1.send(usr1)

	})
	webSocket1.onopen = function(e){
		console.log(e);
		//webSocket1.send("new user added")
	}

	webSocket1.onmessage = function(e){
		$("#newUser").append(e.data+" Joined </br>")

	}
})

// $(function(){

// 	var http = new XMLHttpRequest();
// 	var url = 'http://localhost:8080/page1';
// 	http.open("POST", url, true);
// 	http.onload=function(){
		
// 	}

// })