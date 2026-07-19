
import streamlit as st

st.title("Ratty")

st.write(" ")

st.header("Check Your Password Strength")


password= st.text_input("Enter password", type="password")

special = "?!()&#@<>^%[]"

score = 0

def length():
    if len(password) >= 8:
        st.succes("Length is Good")
        score += 1

    else:
        st.error("Minimum 8 digits Allowed....")

def upper():
    for letter in password :

        if letter.isupper():
            st.success("Uppercase letter ")

            score += 1

        else:
            st.error("Atleast one Uppercase Required !!")


def lower():
    st.write(" ")

    for letter in password:
        if letter.islower():

            st.success("Lowercase Letter available")
            score += 1

        else:
            st.error("Min 1 lowercase letter Required")

def number():
    st.write(" ")

    for letter in password:
        if letter.isdigit():
            st.success("Number is in Password")

            score += 1


        else:
            st.error("Number in password Required")


def special():
    st.write(" ")

    for letter in password:
        if letter in special:

            st.success("check")

            score +=1
        else:
            st.error("Special Characters Required")


def generate():
    pass 

def crack