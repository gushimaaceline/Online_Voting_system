candidate1 = input("Enter the name of the 1st candidate: ")
candidate2 = input("Enter the name of the 2nd candidate: ")

cand1_votes = 0
cand2_votes = 0

voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_of_voters = len(voter_id)

while True:
    if voter_id == []:  # to check when voter list is completed
        print("voting session is over !!")
        if cand1_votes > cand2_votes:
            percentage1 = (cand1_votes / no_of_voters) * 100  # Calculating number of votes in percentage
            print(f"{candidate1}, has won the election with,{percentage1}% of votes")
            break  # to get rid of of infinite loop

        elif cand2_votes > cand1_votes:
            percentage2 = (cand2_votes / no_of_voters) * 100  # Calculating number of votes in percentage
            print(f"{candidate2},has won election with, {percentage2}% votes")
            break

        else:
            print("Both have equal number of votes !! Government will decide who will rule")

    voter = int(input("Enter your id: "))

    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)

        print(".........................")
        print(f"To give vote to,{candidate1}, Press 1")
        print(f"To give vote to,{candidate2}, Press 2")
        print(".........................")

    vote = int(input("Enter your vote:"))
    if vote == 1:
        cand1_votes += 1
        print(f"{candidate1},thank you for your precious vote ")

    elif vote == 2:
          cand2_votes += 1
          print(f"{candidate2},thank you for your precious vote ")
    elif vote > 2:
          print("Check your press key!!")
    else:
           print("You have already voted")





