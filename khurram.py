import string
import random
import streamlit as st
def generate_passward(length):...
def check_passward_strength(passward):
    score = 0
    if passward in common_passward = ["12345678","abc123","khan123"]
    return "* this passward is too common.choose a more unique one.",
    feedback = [
        if len(passward) >= 8:
            score += 1
            else:
                feedback.append("+ passward shold be atleast 8 charectors long.")
                if re.search(r"[A.Z]",passward)and re.search("r[a-z]",passward):
                    score += 1
                    else:
                        feedback.append("+ include both uppercase and lowercase letters.")
                        if re.search(r"\d,passward"):
                            score += 1
                            else:
                                feedback.append("+ add atleast one number (0-9).")
                                if re.search (r"[!@#$%&"]",passward):
                                    score += 1
                                    else:
                                        feedback.apend("+ include atleast one special character (!@#$%^&*).")
                                         if score == 4:
                                            return "\ strong passward!","strong"
                                            elif score == 3:
                                                return "| moderate passward . consider adding more security features.","moderate"
                                                else:
                                                    return "/n".join(feedback),"weak"




                                                    check_passward = st.text_input("enter your passward",type="passward")
                                                    if st.button("check strength"):
                                                        if check_passward:
                                                          result,strength = check_passward_strength(check_passward)
                                                            elif:
                                                                st.warning("please enter a passward")

                        if strength == "strong":
                            st.success(result)
                            st.balloons()
                            elif strength == "moderate":
                                st.warning(result)
                                else:
                                    st.error("weak passward = improve it using these tips:")
                                    else:
                                        st.warning("please enter a passward")
                                        for tip in result.split("/n"):
                                            st.warning(tip)
                        

    ]
    passward_length = st.number_input("enter the length of passward",min_value=8,max_value=20,value=10)
    if st.button("generate passward"):...