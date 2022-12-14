"""Soccer Trivia"""
__author__ = "Anthony Saravia"


# It is a quiz/trivia about soccer related things for an audience with basic knowledge of the game.
def greet():
    junk_two = 3 % 2
    print("Greetings fellow human: Subject No.", junk_two, '\n' * 2)


# * is the multiplication operations for the strings.
# % is the modulus divider which when used, gives us the remainder of the result.
def intro():
    """This function introduces the quiz."""
    name = input("Enter your name: ")
    print("Hello " + name + ", welcome to my soccer quiz!")
    print("This is your chance to prove your a huge soccer fan")
    print('There are:', '10 questions', sep='\n')
    play = input("Are you up for the task?\n Yes or No ")
    play = play.replace(" ", "")
    play = play.lower()
    if play == "yes":
        junk = 1 ** 1
        print("Question ", junk, " begins in..", sep="")
        countdown_num3 = int(1 * 3)
        countdown_num2 = int(4 - 2)
        countdown_num1 = int(3 // 2)
        # ** is the exponent operation for numbers. It creates the integer into the power of what the number is given.
        # - is the subtraction operation. It subtracts the first number from the second one.
        # // is the floor division operator that when dividing, it results in the whole number being the answer only.
        print(countdown_num3)
        print(countdown_num2)
        print(countdown_num1)
        print("Let's...", end="\n")
        print("GO!")
    else:
        quit()


def main_questions(score):
    """Questions"""
    # score = 0  # Starting at zero until we add when they get a question correct

    answer = input("Which country has won the most World Cups?\na. Brazil\nb. Germany\nc. Argentina\nd. France ")
    if answer == "a" or answer == "A":
        print('Correct!')
        score += 1  # Adds a point
    else:
        print(not True)

    answer = input("What country is hosting the up and coming World Cup?\na. Denmark \nb. England\nc. Japan\nd. Qatar ")
    if answer == "d" or answer == "D":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input("How many national teams compete in the World Cup?\na. 16\nb. 32\nc. 64\nd. 4 ")
    if answer == "b" or answer == "B":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input("Which country won the World Cup in 2010?\na. France\nb. Spain\nc. Netherlands\nd. United States  ")
    if answer == "b" or answer == "B":
        print('Correct!')
        score += 1
    else:
        print(not True)

    if score >= 3:
        print("You're doing great! Keep it up!")

    answer = input(
        "Which player is the all-time leading goal scorer in World Cup history?\na. Lionel Messi\nb. Cristiano "
        "Ronaldo\nc. Miroslav Klose\nd. Pele ")
    if answer == "c" or answer == "C":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input("What year did the World Cup competition start?\na. 1950  \nb. 1940 \nc. 1930 \nd. 1965 ")
    if answer == "c" or answer == "C":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input(
        "Which goalkeeper has the most saves in a single World Cup match?\na. Tim Howard\nb. Manuel Neuer\nc. Iker "
        "Casillas\nd. Petr Čech ")
    if answer == "a" or answer == "A":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input(
        "What is the name of Diego Maradona’s infamous first goal against England in 1986?\na. The Golden Boot\nb. "
        "Hand of God\nc. Maradona Miracle\nd. None of the above ")
    if answer == "b" or answer == "B":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input(
        "When does the World Cup take place?\na. Every two years\nb. Every four years\nc. Every six years\nd. Every "
        "eight years ")
    if answer == "b" or answer == "B":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input("What country won the 2020 / 2021 European Championship?\na. Russia\nb. Spain\nc. Italy\nd. France ")
    if answer == "c" or answer == "C":
        print('Correct!')
        score += 1
    else:
        print(not True)
    return score


def bonus_questions(score):
    """These would come into play when the user failed to get more than a 70%"""
    answer = input(
        "What award is given to the year’s best footballer by French news magazine France Football?\na. The Ballon "
        "d'Or\nb. The Emmy Award\nc. The Footballer Grammy  \nd. The Pele Award ")
    if answer == "a" or answer == "A":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input(
        "English rock star Elton John was twice the owner of which football club?\na. FC Barcelona\nb. Watford\nc. "
        "Chelsea\nd. Liverpool ")
    if answer == "b" or answer == "B":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input(
        "Which manager is credited with introducing FC Barcelona to the famous tiki-taka style of play?\na. Jurgen "
        "Klopp\nb. Pep Guardiola\nc. Xavi\nd. Erik Ten Hag ")
    if answer == "b" or answer == "B":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input("What is the nickname for Lionel Messi?\na. La Pulga\nb. El Bicho\nc. Messidihno\nd. Bob ")
    if answer == "a" or answer == "A":
        print('Correct!')
        score += 1
    else:
        print(not True)

    answer = input(
        "What is the name of the top division in Italy?\na. La Liga \nb. Ligue 1 \nc. Premeier League \nd. Serie A ")
    if answer == "d" or answer == "D":
        print('Correct!')
        score += 1
    else:
        print(not True)
    return score


def bonus_results(score):
    print("You got " + str(score) + " questions correct!")
    print("You got a " + "{0:.0%}".format(score / 15))  # diving the total score with the total amount of questions
    print("You did your best!")
    return score


def main():
    greet()
    intro()
    total = 0
    total = main_questions(total)
    if total >= 7:
        print("You got " + str(total) + " questions correct!")
        # + is the concatenated operator that adds two strings together
        print("You got a " + "{0:.0%}".format(total / 10))  # diving the total score with the total amount of questions
        print('End of Quiz.')
    else:
        print("Bonus Questions!")
        total = bonus_questions(total)
        total = bonus_results(total)


main()
