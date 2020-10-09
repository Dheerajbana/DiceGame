import random


class DiceGame:

    def __init__(self):
        user_input = str(input())
        user_input_split = user_input.split(" ")
        self.no_of_players = int(user_input_split[0])
        self.max_points = int(user_input_split[1])
        self.players_list = []
        self.player_score_dict = {}
        self.report_dict = {}
        self.last_value_dict = {}
        self.skip_chance_list = []
        self.complete_count = 0

    def start_game(self):

        rank_count = 1
        for i in range(1,self.no_of_players+1):
            player = "Player-"+str(i)
            self.players_list.append(player)

        print("********************** We have "+str(self.no_of_players)+" players in the game ********************************")
        print("**************************** Lets Start The Game ************************************")
        # shuffling players
        random.shuffle(self.players_list)
        everyone_completed_flag = False
        while everyone_completed_flag is not True:
            for player in self.players_list:
                if player == "Completed Game":
                    continue
                dice_input = False
                while dice_input is not True:
                    if player in self.skip_chance_list:
                        print("**** Sorry " + player + " You wont get next chance as you got two 1's consecutively ****")
                        self.skip_chance_list.remove(player)
                        dice_input = True
                        print()
                    else:
                        dice_input = input(player + " its your turn (press 'r' to roll the dice)")
                        if dice_input == "r":
                            res = str(self.roll_dice())
                            if int(res) == 6:
                                print(" Horray you got a 6 you will get one more chance to roll dice")
                            print(player+" got "+res)
                            if player not in self.last_value_dict:
                                self.last_value_dict[player] = int(res)
                            else:
                                if self.last_value_dict[player] == 1 and int(res) == 1:
                                    self.skip_chance_list.append(player)
                                self.last_value_dict[player] = int(res)

                            if player not in self.player_score_dict:
                                self.player_score_dict[player] = int(res)
                            else:
                                self.player_score_dict[player] += int(res)

                            print()
                            print(player + " Total Score: " + str(self.player_score_dict[player]))
                            if self.player_score_dict[player] >= self.max_points:
                                self.report_dict[player] = [rank_count, self.player_score_dict[player]]
                                print()
                                print("Dice Game completed for "+player+" with Rank "+str(rank_count)+" and Score "+str(self.player_score_dict[player]))
                                self.players_list[self.players_list.index(player)] = "Completed Game"
                                rank_count += 1
                            print()
                            self.display_players_table(self.report_dict)
                            if self.player_score_dict[player] >= self.max_points:
                                dice_input = True
                            elif int(res) == 6:
                                dice_input = False
                            else:
                                dice_input = True
                        else:
                            print("Wrong input please Press 'r' to roll the dice")
                            print()

            self.complete_count = self.players_list.count("Completed Game")
            if len(self.players_list) == self.complete_count:
                everyone_completed_flag = True

    def roll_dice(self):
        no = random.randint(1, 6)
        print()
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        if no == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        if no == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        if no == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        if no == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        if no == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
        print()
        return no

    def display_players_table(self, report_dict):
        if len(report_dict) == self.no_of_players:
            print("***************************** Final Standings ********************************")
            print()
            for player_result in report_dict:
                print("******************** " + player_result + " on Rank: " + str(report_dict[player_result][0]) + " with " + str(report_dict[player_result][1])+" Points ***********************")
            print()
            print("********************* Game Has Ended Thanks For Playing **********************")
            return
        else:
            if len(report_dict) > 0:
                print("****************************** Current Standings *****************************")
                for player_result in report_dict:
                    print("******************** "+ player_result+" on Rank: " + str(report_dict[player_result][0]) + " with " + str(report_dict[player_result][1])+" Points ***********************")
                print()
            else:
                print("************************** No one completed the game yet *************************")
                print()


if __name__ == "__main__":
    print()
    print("***************************** Welcome to the Dice Game ******************************")
    print("Please Enter Number Of Players separated by a space with Maximum Points to Accumulate")
    start_playing = DiceGame()
    start_playing.start_game()

