from twilio.rest import Client
import keys

print("                               😎  ^_^ WELCOME IN ELECTION ^_^  😎")
print()
print(" 🌟 Starting by Administration Portal 🌟")
print()
v=int(input("Please enter the no. of approximate Voters : "))
B =input("Enter 1st Candidate:")
T =input("Enter 2nd Candidate:")
print()
print(" 🌟 Let's Start the Vote 🌟")
print("       Here is your Precious VOTE .....")
print("          ⭐  you have to give VOTE between", B ,"&" ,T)
print("          ⭐  Press s to stop the vote 🚫")
print("          ⭐  Press Enter To Start The Voting System 🤏")
a=input()
main_list = []
vote_list = []

for g in range(1, v):
     user = input("Enter your VOTER ID 🪪: ")
     number = input("Enter your Mobile Number 📲: ")
     target_number = '+91'+number
     if user =="s":
         break
     for h in range(1, 2):
         main_list.append(user)
         s = main_list.count(user)
         if s != 1:
            print("""This is Not Your VOTER ID ❌
Please check your ID! Sorry. """)
            break
         print("*****************************************")
         print("(To give your VOTE to", B, "press A or a)")
         print("(to give your VOTE to", T, "press B or b)")
         print("*****************************************")
         user_vote = input("Enter Your Precious VOTE :")
         if user_vote == "A" or user_vote =="a":
             print("        Thanks for vote 🤗", B)
         elif user_vote == "B" or user_vote =="b":
             print("        Thanks for vote 🤗", T)
         else:
             print("You should enter a valid VOTE for giving Vote, Sorry!!! 😥")
         print("Your Voting session is over !!! 🔚")

         client = Client(keys.account_sid, keys.auth_token)
         message = client.messages.create(
         body = "Vote has been completed, Thanks for participation  ",
         from_ = keys.twilio_number,
         to = target_number
         )

         print()
         print()

         vote_list.append(user_vote)

count_1=vote_list.count("A")
count_2=vote_list.count("a")
count_3=vote_list.count("b")
count_4=vote_list.count("B")

result_1=(count_1+count_2)
result_2=(count_3+count_4)
#final_result=result_1+result_2

vote_length=count_1+count_2+count_3+count_4

if result_1>result_2:
    z=(result_1/vote_length)*100
    print(B,"has won the election with", z, "% of VOTES")
elif result_2>result_1:
    w=(result_2/vote_length)*100
    print(T,"has won the election with", w, "% of VOTES")
elif result_1==result_2:
    print("both have equal no. of vote with each 50% ")

print()
print("voting session is over....(●'◡'●) ")

