import datetime
import random

class Player():
    def __init__(self, player_name, secret_number, date):
        self.player_name = player_name
        self.secret_number=secret_number
        self.date=date


player_name = input("Please enter your name: ")

secret_number = random.randint(1, 30)

while True:
    guess = int(input("Hello {0}, help me guess the secret number (between 1 and 30): ".format(player_name)))

    if guess == secret_number:
        player_data = Player(
            player_name=player_name,
            secret_number=int(secret_number),
            date=str(datetime.datetime.now())
        )

        with open("results.txt", "w") as player_info:
            player_info.write(str(player_data.__dict__))

        print("Congratulations, you guessed the number. Your info: {0}".format(player_data.__dict__))

        break

    if guess > secret_number:
        print("Your guess is not correct... try something smaller")
    elif guess < secret_number:
        print("Your guess is not correct... try something bigger")

