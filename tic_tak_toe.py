def tic_tac_toe():

    print("Welcome to Tic-Tac-Toe!")

    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:

        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        player_symbol, ai_symbol = player_choice()

        turn = 'Player'

        game_on = True



        while game_on:

            display_board(board)

            if turn == 'Player':

                player_move(board, player_symbol)

                if check_win(board, player_symbol):

                    display_board(board)

                    print("Congratulations! " + player_name + ", you have won the game!")

                    game_on = False

                else:

                    if check_full(board):

                        display_board(board)

                        print("It's a tie!")

                        break

                    else:

                        turn = 'AI'

            else:

                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):

                    display_board(board)

                    print("AI has won the game!")

                    game_on = False

                else:

                    if check_full(board):

                        display_board(board)

                        print("It's a tie!")

                        break

                    else:

                        turn = 'Player'

        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != 'yes':

            print("Thank you for playing!")

            break
