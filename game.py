import streamlit as st
import random

def get_game_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Snake" and computer_choice == "Water") or (user_choice == "Water" and computer_choice == "Gun") or (user_choice == "Gun" and computer_choice == "Snake"):
        return "You Win"
    else:
        return "Computer Wins"

def main():
    st.title("Snake Water Gun Game")
    
    # Initialize score and game history
    user_score = 0
    computer_score = 0
    game_history = []
    user_choice = st.radio("Your Choice", ["Snake", "Water", "Gun"])
    c=1
    while st.button("Play",key=c):
        computer_choice = random.choice(["Snake", "Water", "Gun"])
        result = get_game_result(user_choice, computer_choice)
        game_history.append((user_choice, computer_choice, result))
            
        if result == "You Win":
            user_score += 1
        elif result == "Computer Wins":
            computer_score += 1
        st.write(f"Result: {result}")
        # st.write(f"You chose: {user_choice}")
        # st.write(f"Computer chose: {computer_choice}")
        
        
        # st.write("Current Score:")
        # st.write(f"You: {user_score}")
        # st.write(f"Computer: {computer_score}")
        
        # st.write("Game History:")
        # for user, computer, result in game_history:
        #     st.write(f"You: {user} - Computer: {computer} - Result: {result}")
        
        st.write("---")
        c+=1 
       
        
        
if __name__ == "__main__":
    main()
