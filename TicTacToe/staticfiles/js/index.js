firstMove=null
turn=0
function set(m){
	if(firstMove==null)
		firstMove=m;
	
	//alert(firstMove);
}

function loadMove(board) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      var n=parseInt(xhttp.responseText);
	  row=Math.ceil(n/3);
	  col=n%3;
	  if (col==0)
		col=3;
		turn++;
	  id="block"+turn+"-"+row+"-"+col;
	  alert(id);
	  document.getElementById(id).checked=true;
    }
  };
  xhttp.open("GET", "move?board="+board, true);
  xhttp.send();
}


function getMove(_id)
{
	
	if (_id==1){
		set(0);
	}
	else{
		if(document.getElementById(_id).checked==true)
			return false;
		set(1);
		turn++;
		document.getElementById(_id).checked=true;
	}
	board="";
	for (i=1;i<=3;i++)
		for (j=1;j<=3;j++){
			l=0;
			for (k=1;k<=9;k++){
				l++;
				id="block"+k+"-"+i+"-"+j;
				if (document.getElementById(id).checked==true){
					player="";
					if(firstMove==0)
						if(k%2==0)
							player="1";
						else
							player="0";
					else
						if(k%2==0)
							player="0";
						else
							player="1";
					board+=player;
					//alert(id);
					break;
				}
			if(l==9)
			}
				board+="-";
		}
	alert(board);
	if(board.indexOf('-') == -1)
	{
	  return false;
	}
	loadMove(board);
}

function doMove(n){	
}