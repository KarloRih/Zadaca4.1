import datetime
import json
import random

secret = random.randint(1, 100)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Pogodi tajni broj (Između 1 i 100): "))
    attempts += 1

    if guess == secret:
        score_list.append({"Pokušaji": attempts, "Datum": str(datetime.datetime.now())})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Čestitamo, pogodili ste broj, broj je  " + str(secret))
        print("Broj pokušaja: " + str(attempts))
        break
    elif guess > secret:
        print("Tvoj pokušaj nije točan. Probaj s manjim brojem!")
    elif guess < secret:
        print("Tvoj pokušaj nije točan. Probaj s većim brojem!")