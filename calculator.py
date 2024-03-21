import streamlit as st 

# a simple calculator 
def calculator(a, b, op="+"):
    match op:
        case'+':return a+b
        case '-':return a-b
        case '/':return a/b
        case'*': return a*b
        case'**':return a**b

st.title("calculator")
st.markdown("very simple and cheap example of streamlit")

c1,c2 ,c3 =st.columns(3) # create three columns 
num1=c1.number_input("enter first number",value=62)
num2=c2.number_input("enter second number",value=12)
action=c3.selectbox("select operation",["+","-","/","*","**"])

try:
    result=calculator(num1,num2,action)
    st.success(f"result:{result}")
except Exception as e:
    st.error(f"error:{e}")
