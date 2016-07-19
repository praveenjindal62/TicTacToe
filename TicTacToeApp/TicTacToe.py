
def getNextPossibleMoves(board):
	return [i for i in range(len(board)) if board[i] is None]

def gameEnd(board):
	if None in board:
		return False
	else:
		return True

def togglePlayer(player):
	if player==1:
		return 0
	return 1
def getScore(board,player):
	winner=getWinner(board)
	#print "Winner ",winner
	if winner==Player:
		return 10
	elif winner==Opponent:
		return -10
		raw_input("Opponent Winning here")
	else:
		return 0
		
def nextMove(board,player,depth=1):
	possibleMoves=getNextPossibleMoves(board)
	score=[None for i in possibleMoves]
	j=0
	for i in possibleMoves:
		board_clone=board[:]
		board_clone[i]=player
		#print "Move: ",i," Depth: ",depth," Player:",player
		#print board_clone
		temp_score=getScore(board_clone,player)
		#print temp_score
		# if not temp_score==-2:
			# score[j]=temp_score
		# else:
		#print temp_score
		if depth==Level or gameEnd(board_clone) or temp_score!=0:
			score[j]=depth+temp_score
		elif depth%2==1:
			d=depth+1
			score[j]=min(nextMove(board_clone,togglePlayer(player),d)[1])
		else:
			d=depth+1
			score[j]=max(nextMove(board_clone,togglePlayer(player),d)[1])
		j+=1
	#print score,possibleMoves
	return possibleMoves,score
	
def getWinner(board):
	if board[0]==board[1] and board[0]==board[2]: return board[0]
	elif board[0]==board[3] and board[0]==board[6]: return board[0]
	elif board[0]==board[4] and board[0]==board[8]: return board[0]
	elif board[2]==board[5] and board[2]==board[8]: return board[2]
	elif board[2]==board[4] and board[2]==board[6]: return board[2]
	elif board[6]==board[7] and board[6]==board[8]: return board[6]
	elif board[1]==board[4] and board[1]==board[7]: return board[1]
	elif board[3]==board[4] and board[3]==board[5]: return board[3]
	return None

def validPlayer(board,player):
	c1=c2=0
	if player==Player:
		c1=1
		c2=0
	else:
		c2=1
		c1=0
	for i in range(len(board)):
		if board[i]==Player:
			c1+=1
		elif board[i]==Opponent:
			c2+=1
	if abs(c1-c2)>1:
		return False
	return True
def getBestPossibleMove(board,player,level):
	#init(player,level)
	if validPlayer(board,player) and not gameEnd(board):
		moves,score=nextMove(board,player)
		print moves,score
		return moves[score.index(max(score))]
	else:
		return -1
def init(player,level):
	Level=level
	Player=player
	Opponent=togglePlayer(Player)


def printBoard(board):
	s=""
	for i in range(len(board)):
		if board[i]==None:
			s+=" _ "
		else:
			s+=" "+str(board[i])+" "
		if (i+1)%3==0:
			print s
			s=""
def startGame():
	while not gameEnd(tictactoeboard):
		if not getWinner(tictactoeboard)==None:
			print "Winner is ",getWinner(tictactoeboard)
			break
		m=getBestPossibleMove(tictactoeboard,Player,Level)
		print "Computer Move: ",m+1
		tictactoeboard[m]=Player
		printBoard(tictactoeboard)
		n=int(raw_input("Enter your Move: "))
		if tictactoeboard[n-1]==None:
			tictactoeboard[n-1]=1
		else:
			print "Invalid Move"
			continue
Player=0
Opponent=togglePlayer(Player)
Level=7
#tictactoeboard=[None,None,None,None,None,None,None,None,None]
#startGame()
#print getBestPossibleMove(tictactoeboard,Player,Level)
