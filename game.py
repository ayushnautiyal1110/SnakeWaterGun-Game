import streamlit as st
st.write("=================== Welcome to Snake Water Gun Game =================")
import random
import math
no=random.randint(1,3)
st.write("Hey Please enter the number")
inp=int(input())
You=0
Computer=0
while(True):
    if(inp==0):
        st.write("Thanks For Playing the Game")
        st.write("Here is score")
        st.write(You)
        st.write("Here is Computer score")
        st.write(Computer)
        break;
    elif(no==inp):
        st.write("Draw")
    elif(no==1):
        if(inp==2):
            st.write("You Lost")
            Computer+=1
        else:
            st.write("You Won")
            You+=1
    elif(no==2):
        if(inp==1):
            st.write("You Won")
            You+=1
        else:
            st.write("You Lost")
            Computer+=1
    elif(no==3):
        if(inp==1):
            st.write("You Lost")
            Computer+=1
        else:
            st.write("You Won")
            You+=1
            
