import random

options = ["Rock", "Paper", "Scissors"]
global user_point, pc_point, arr_user, arr_pc
user_point = 0
pc_point = 0
arr_user = []
arr_pc = []

after_rock = []
after_paper = []
after_scissors = []


def points(user, pc, arr_user, arr_pc):
    if pc == "Rock" and user == "Rock":
        print("tie...")
    elif pc == "Paper" and user == "Paper":
        print("tie...")
    elif pc == "Scissors" and user == "Scissors":
        print("tie...")

    elif pc == "Rock" and user == "Paper":
        arr_user.append(1)
        print("1 more point to the user what gives us:", user_point + 1, "points to user and", pc_point,
              "to the computer.")
    elif pc == "Paper" and user == "Scissors":
        arr_user.append(1)
        print("1 more point to the user what gives us:", user_point + 1, "points to user and", pc_point,
              "to the computer.")
    elif pc == "Scissors" and user == "Rock":
        arr_user.append(1)
        print("1 more point to the user what gives us:", user_point + 1, "points to user and", pc_point,
              "to the computer.")

    elif user == "Rock" and pc == "Paper":
        arr_pc.append(1)
        print("1 more point to the computer what gives us:", user_point, "points to user and", pc_point + 1,
              "to the computer.")
    elif user == "Paper" and pc == "Scissors":
        arr_pc.append(1)
        print("1 more point to the computer what gives us:", user_point, "points to user and", pc_point + 1,
              "to the computer.")
    elif user == "Scissors" and pc == "Rock":
        arr_pc.append(1)
        print("1 more point to the computer what gives us:", user_point, "points to user and", pc_point + 1,
              "to the computer.")


def after(last_try, user):
    if last_try == "Rock":
        after_rock.append(user)
    elif last_try == "Paper":
        after_paper.append(user)
    elif last_try == "Scissors":
        after_scissors.append(user)
    return


ask_loop = int(input("how many points to win? "))
while ask_loop < 1:
    ask_loop = int(input("it must be a positive number you silly. choose again. "))
user = input("Rock, Paper, Scissors? ")
pc = options[random.randint(0, 2)]
print(pc)
points(user, pc, arr_user, arr_pc)
user_point = sum(arr_user)
pc_point = sum(arr_pc)

while ask_loop > user_point and ask_loop > pc_point:
    last_try = user
    user = input("Rock, Paper, Scissors? ")
    after(last_try, user)
    if last_try == "Rock" and len(after_rock) > 0:
        pc = after_rock[random.randint(0, len(after_rock) - 1)]
        if pc == 'Rock':
            pc = 'Paper'
        elif pc == 'Paper':
            pc = 'Scissors'
        else:
            pc = 'Rock'
    elif last_try == "Paper" and len(after_paper) > 0:
        pc = after_paper[random.randint(0, len(after_paper) - 1)]
        if pc == 'Rock':
            pc = 'Paper'
        elif pc == 'Paper':
            pc = 'Scissors'
        else:
            pc = 'Rock'
    elif last_try == "Scissors" and len(after_scissors) > 0:
        pc = after_scissors[random.randint(0, len(after_scissors) - 1)]
        if pc == 'Rock':
            pc = 'Paper'
        elif pc == 'Paper':
            pc = 'Scissors'
        else:
            pc = 'Rock'
    else:
        pc = options[random.randint(0, 2)]
    print(pc)
    points(user, pc, arr_user, arr_pc)
    user_point = sum(arr_user)
    pc_point = sum(arr_pc)

print("the final result is:", user_point, "to the player and", pc_point, "to the computer")
print("")
print("statistics:")
if len(after_rock) > 0:
    print("after rock -", after_rock.count("Rock") * 100 / len(after_rock), "%", "Rock.",
          after_rock.count("Paper") * 100 / len(after_rock), "%", "Paper.",
          after_rock.count("Scissors") * 100 / len(after_rock), "%", "Scissors.")
if len(after_paper) > 0:
    print("after paper -", after_paper.count("Rock") * 100 / len(after_paper), "%", "Rock.",
          after_paper.count("Paper") * 100 / len(after_paper), "%", "Paper.",
          after_paper.count("Scissors") * 100 / len(after_paper), "%", "Scissors.")
if len(after_scissors) > 0:
    print("after sicsors -", after_scissors.count("Rock") * 100 / len(after_scissors), "%", "Rock.",
          after_scissors.count("Paper") * 100 / len(after_scissors), "%", "Paper.",
          after_scissors.count("Scissors") * 100 / len(after_scissors), "%", "Scissors.")
