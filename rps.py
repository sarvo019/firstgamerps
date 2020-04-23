from random import randint

# wining counts of player
p1_win_count = 0
p2_win_count = 0
tie_count = 0
rounds_to_play = int(input("How many rounds you need to play :"))
player1 = input("Player1 Enter your name: ").upper()
option = input("Do want play with computer Y or N: ").lower()
if option == "y" or option == "yes":
    player2 = "COMPUTER"
    print(f"You choosed to play vs {player2} \n **** ALL THE BEST ****")
else:
    player2 = input("Player2 Enter your name: ").upper()
    print(f"You choosed to play vs {player2} \n **** ALL THE BEST****")

while p1_win_count < rounds_to_play and p2_win_count < rounds_to_play:

    # if computer , computer moves as per game.
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    # Game moves.
    print("YOUR MOVES")
    print("...rock...")
    print("...paper...")
    print("...scissors...")        

    # Players input.
    player1_input = input(f"{player1} make a move: ").lower()
    if option == "y" or option == "yes":
        player2_input = computer
    else:
        player2_input = input(f"{player2} make a move: ").lower()

    # The game starts
    if player1_input == player2_input:
        print("Ended up in tie.")
        tie_count += 1

    elif player1_input == "rock":
        if player2_input == "paper":
            print(f"{player2} wins")
            p2_win_count += 1
        else:
            print(f"{player1} wins")
            p1_win_count += 1

    elif player1_input == "paper":
        if player2_input == "scissors":
            print(f"{player2} wins")
            p2_win_count += 1
        else:
            print(f"{player1} wins")
            p1_win_count += 1

    elif player1_input == "scissors":
        if player2_input == "rock":
            print(f"{player2} wins")
            p2_win_count += 1
        else:
            print(f"{player1} wins")
            p1_win_count += 1

    else:
        print("Enter a valid choice")

    # Players score card after each round. 
    print(
        f"{player1}: {p1_win_count} {player2}: {p2_win_count} Tie Score: {tie_count}")        

# Winner declaration
print("*********************************")
print("{0} :: {1} vs {2} :: {3}".format(player1, p1_win_count, player2, p2_win_count))
print("*********************************")
if p1_win_count > p2_win_count:
    print(f"{player1} WINS")
elif p1_win_count == p2_win_count:
    print("Match ended up in Tie")
else:
    print(f"{player2} WINS")
