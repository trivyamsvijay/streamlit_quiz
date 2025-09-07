import streamlit as st

st.title("Quiz App")

question1 = 0
question2 = 0
question3 = 0
question4 = 0
question5 = 0
question1 = st.radio("(1).Who wrote the play 'Hamlet",["Berlin", "Madrid", "Paris", "Rome"])

question2 = st.radio("(2).What is the capital of France?",["William Wordsworth", "William Shakespeare", "Leo Tolstoy", "Mark Twain"])

question3 = st.radio("(3).Which planet is known as the Red Planet?",["Venus", "Mars", "Jupiter", "Mercury"])

question4 = st.radio("(4).What is the largest mammal in the world?",["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"])

question5 = st.radio("(5).In which year did India gain independence?",["1945", "1947", "1950", "1962"])

answer1  = "Paris"
answer2  = "William Shakespeare"
answer3  = "Mars"   
answer4  = "Blue Whale"
answer5  = "1947"

if question1 == answer1 :
    question1 =1
else:
    question1=0


if question2 == answer2 :
    question2 =1
else:
    question2=0

if question3 == answer3 :
    question3 =1

else:
    question3=0

if question4 == answer4 :
    question4 =1

else:
    question4=0

if question5 == answer5 :
    question5 =1

else:
    question5=0

sum = question1+question2+question3+question4+question5

if st.button("Check It"):
    if sum >= 4 :
        st.success("aatha naa pass aaiten")
    
    else:
        st.warning("aatha naa pail aaiten")



