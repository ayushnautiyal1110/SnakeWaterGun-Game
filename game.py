import streamlit as st
st.write("=================== Welcome to Snake Water Gun Game =================")
import random
import math
no=random.randint(1,3)

You=0
Computer=0
while(True):
    if(inp==0):
        inp=st.number_input("Hey Please enter the number")
        st.markdown("Thanks For Playing the Game")
        st.markdown("Here is score")
        st.markdown(You)
        st.markdown("Here is Computer score")
        st.markdown(Computer)
        break;
    elif(no==inp):
        st.markdown("Draw")
    elif(no==1):
        if(inp==2):
            st.markdown("You Lost")
            Computer+=1
        else:
            st.markdown("You Won")
            You+=1
    elif(no==2):
        if(inp==1):
            st.markdown("You Won")
            You+=1
        else:
            st.markdown("You Lost")
            Computer+=1
    elif(no==3):
        if(inp==1):
            st.markdown("You Lost")
            Computer+=1
        else:
            st.markdown("You Won")
            You+=1
            
