hook = "You are walking through the woods with the queens" \
"precious cargo. You hear a loud thump in the trail in front of you." \
" What do you do? A Run and hide B. Turn around courageously C. Run towards the noise." \

decision_a = "You hide behind a tree and fall into a reality warping hole. " \
"You land on Tatoonine. What do you do? D. Get on the pod racer E. Call for help F. Cry." \

decision_b = "You face agiant snaggletoothed rat. It is hungry. What do you do?" \
" G. Fight the rat H. Run and hide I. Be friends"

decision_c = "You find a kind old man who tripped. He offers you a wish." \
" What do you do. J. Run and hide " \
"K. Ask about the conditions of the wish. L. Wish for BYU chocolate milk. "

decision_d = "You are challenged to a race.  What do you do? M. Win the race N. Lose the race."

decision_e = "Sand people come to eat you. What do you do? O. Fight P. Run and hide"

decision_f = "You keep crying. What do you do? Q. Cry more R. Stoop crying."

decision_g = "You die from the rat"

decision_h = decision_a

decision_i = "The rat is now your bestie. You win."

decision_j = decision_a

decision_k = "The old man gets andgry. You die."

decision_l = "You recieve a cold glass of BYU choclate milk. You win."

decision_m = "You win."

decision_n = "You die."

decision_o = decision_n

decision_p = decision_a

decision_q = decision_n

decision_r = decision_m

decision = input(hook)     # Collect the decision from the user
decision = decision.upper()    # Convert the decision to uppercase

# Write what happens when you choose...
decision_2 = ""
if decision == "A": 
    decision2 = input(decision_a)
elif decision == "B": 
    decision2 = input(decision_b)
elif decision == "C": 
    decision2 = input(decision_c)
else:
    print("You are dead")

if decision == "A" or decision == "B" or decision == "C":
    decision_2 = decision2.upper()
    if decision_2 == "D":
        decision_3 = input(decision_d)
    elif decision_2 == "E":
        decision_3 = input(decision_e)
    elif decision_2 == "F":
        decision_3 = input(decision_f)
    elif decision_2 == "G":
        print(decision_g)
    elif decision_2 == "H":
        decision_3 = input(decision_h)
    elif decision_2 == "I":
        print(decision_i)
    elif decision_2 == "J":
        decision_3 = input(decision_j)
    elif decision_2 == "K":
        print(decision_k)
    elif decision_2 == "L":
        print(decision_l)
        



