import random
import string
import streamlit as st
import qrcode

st.title("Ratty")

st.write(" ")

st.header("Check Your Password Strength")

stage = "main"

if "stage" not in st.session_state:
    st.session_state.stage = "main"


password= st.text_input("Enter password", type="password")

special = "?!()&#@<>^%[]"

score = 0

def main():
    if st.button("Check Entropy", type="primary"):
        st.session_state.stage = "entropy"

    st.write(" ")

    if st.button("Time to Crack", type="primary"):
         st.session_state.stage = "crack"

    st.write(" ")

    if st.button("Generate Password", type="primary"):
         st.session_state.stage = "generate"

    st.write(" ")

    if st.button("Make Qr", type="primary"):
         st.session_state.stage = "qr"
         

def length():
    if len(password) >= 8:
        st.success("Length is Good")
        return 1

    else:
        st.error("Minimum 8 digits Allowed....")
        return 0

def upper():
    
    if any(letter.isupper() for letter in password):
            st.success("Uppercase letter ")

            return 1 

    else:
            st.error("Atleast one Uppercase Required !!")
            return 0


def lower():
    st.write(" ")

    if any(letter.islower() for letter in password):

            st.success("Lowercase Letter available")
            return 1

        
        
    else:
            st.error("Min 1 lowercase letter Required")
            return 0

def number():
    st.write(" ")

    if any(letter.isdigit() for letter in password):
            st.success("Number is in Password")

            return 1


    else:
            st.error("Number in password Required")
            return 0


def specials():
    st.write(" ")

    if any(letter in special for letter in special):

            st.success("Special numerics Is in Password")

            return 1
    else:
            st.error("Special Characters Required")

            return 0


def generate():
    char = string.ascii_letters + string.digits + "!?%@^"

    passw = " ".join(random.choice(char)  for _ in range(10))
    st.write(" ")

    st.code(passw)

    if st.button("New One", type="primary"):
         st.session_state.stage = "generate"

    st.write(" ")

    if st.button("return to home"):
         st.session_state.stage = "main"

def crack():
    if score <= 2:
        st.write("It can Easily Crack in Few minutes")

    elif score == 3:
        st.write("Can Crack Few Hours")

    elif score >= 4:
        st.write("Its Good one maybe Takes Days and years To Crack It")

    
    if st.button("Return to Home"):
         st.session_state.stage = "main"


def entropy():
    st.write(" ")

    ent = len(password) * 4

    st.metric("Entropy Score", ent)

    if st.button(" Return To home"):
        st.session_state.stage = "main"

def qr():
     st.write("Your Password Qr")

     st.write(" ")

     new = qrcode.make(password)

     new = new.get_image()

     

     st.write(" ")

     st.image(new)

     st.write(" ")
    
     if st.button("Return to home"):
       st.session_state.stage = "main"
     


score += int(upper())
score += int(lower())

score += int(specials())
score += int(number())
score += int(length())

#if st.session_state.stage == "main":
   # length()
    #lower()
  #  upper()
   # number()
   # specials()
if st.session_state.stage == "main":
     main()

elif st.session_state.stage == "entropy":
    entropy()

elif st.session_state.stage == "crack":
     crack()


elif st.session_state.stage == "generate":
     generate()
elif st.session_state.stage == "qr":
     qr()




