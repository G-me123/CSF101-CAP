# Name: Jigme Namgyel
# Department: 1st Electrical
# std ID: 02230064

# REFERENCES for assignment
# Chat gpt

# SOLUTION
# Solution Score is: 49524
# input_4_cap1.txt(49524)

# initialize the programme
def read_input(Input_your_file_name):
    x = []
    with open(Input_your_file_name, 'r') as files:
        for y in files:
            opponent_choice, outcome = y.split()
            x.append((opponent_choice, outcome))
    return x

# Calculating the score for each round
def calculate_score(Total_Number_of_rounds):
    Score = 0
    for opponent_choice, outcome in Total_Number_of_rounds:
        if outcome == 'X':  # inorder to lose(here, we have to lose and opponent has to win)
            if opponent_choice == 'A':
                Score += 3  # if rock defeats scissor(here, if opponent show rock, inorder to lose we need to show scissor)
            elif opponent_choice == 'B':
                Score += 1  # if Paper defeats rock(here, if opponent show paper, inorder to lose we need to show rock)
            elif opponent_choice == 'C':
                Score += 2  # if Scissors defeats paper(here, if opponent show scissor, we need to show paper to lose )
        elif outcome == 'Y':  # inorder to draw(here, we need to get draw with opponent)
            if opponent_choice == 'A':
                Score += 4  # if Rock draws with Rock(here, when opponent show rock ,we need to show rock for draw )
            elif opponent_choice == 'B':
                Score += 5  # if Paper draws with Paper(here, when opponent show paper ,we need to show paper for draw) 
            elif opponent_choice == 'C':
                Score += 6  # if Scissors draws with Scissors(here, when opponent show scissor ,we need to show scissor for draw )
        elif outcome == 'Z':  # inorder to win(here, we need to win over opponent)
            if opponent_choice == 'A':
                Score += 8  # if paper win over rock, the score will be;
            elif opponent_choice == 'B':
                Score += 9  # if scissor wins over paper, the score will be;
            elif opponent_choice == 'C':
                Score += 7  # if rock wins over scissor, the score will be;
    print(f"The total score is:{Score}")


# To executed a program
Input_your_file_name = "CSF101CAP/input_4_cap1.txt" 
calculate_score(read_input(Input_your_file_name))