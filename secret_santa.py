import random
import sys
import os
from datetime import datetime


def generate_html_page(gifter: str, giftee: str, dir: str):
    page = """
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Santa</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(to bottom, #ffcccb, #ff6f61);
            background-repeat: repeat;
            color: white;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }

        h1 {
            font-size: 4em;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        }
        audio {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
</head>

<body>
    <h1>GIFTER, tu offres à GIFTEE</h1>
    <audio controls autoplay loop>
        <source src="https://upload.wikimedia.org/wikipedia/commons/d/da/S%5EulPO2020_Jingle_Bell.wav" type="audio/wav">
        Your browser does not support the audio element.
    </audio>
</body>

</html>
    """
    with open(os.path.join(dir, f"{gifter}.html"), "w") as gifter_file:
        gifter_file.write(page.replace(
            'GIFTER', gifter).replace('GIFTEE', giftee))


def find_giftee(gifters: list, dir: str, debug: bool):
    random.shuffle(gifters)
    giftees = gifters.copy()
    gifters_who_found_a_giftee = []
    giftees_who_found_a_gifter = []
    for gifter in gifters:
        giftee_found = False
        while not giftee_found:
            random_giftee = random.choice(giftees)
            if random_giftee == gifter:
                if len(giftees) == 1:
                    print("\nOops, dead end. Retry.")
                    sys.exit(1)
                print(
                    f"... Picking another giftee, gifter and giftee are {random_giftee}.")
            else:
                giftee_found = True
                giftees.remove(random_giftee)
                gifters_who_found_a_giftee.append(gifter)
                giftees_who_found_a_gifter.append(random_giftee)
        if debug:
            print(f"{gifter} gives a present to {random_giftee}")
        generate_html_page(gifter, random_giftee, dir)

    print("")
    print(f'Checking:')
    if len(set(giftees_who_found_a_gifter)) != len(giftees_who_found_a_gifter):
        print("Oops, one giftee has been 'chosen' twice by two gifters :(")
        sys.exit(1)
    if len(set(gifters_who_found_a_giftee)) != len(gifters_who_found_a_giftee):
        print("Oops, one gifter gives TWO presents????")
        sys.exit(1)
    if len(giftees_who_found_a_gifter) != len(gifters):
        print("Oops, one giftee has no gifter!!!!!!!")
        print(giftees_who_found_a_gifter)
        sys.exit(1)
    if len(gifters_who_found_a_giftee) != len(gifters):
        print("Oops, one gifter gives nothing!!!! Rat!")
        sys.exit(1)
    print("Everything seems ok!")


def main():
    # To replace
    who = "Pierre Paul Jacques Flora Emilie Pauline".split(
        ' ')
    debug = False

    now = datetime.now()
    dir = now.strftime("%H%M%S")
    os.mkdir(now.strftime(dir))
    print('Who:')
    print(f'{who}\n')
    find_giftee(who, dir, debug)


if __name__ == '__main__':
    main()
