import TicTacToe
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	return render(request,'index.html',{})
def getMove(request):
	m=request.GET.get('board')
	board=[]
	for i in m:
		if i=='-':
			board.append(None)
		else:
			board.append(int(i))
	move=TicTacToe.getBestPossibleMove(board,0,7)
	print board,move	
	return HttpResponse(move+1)