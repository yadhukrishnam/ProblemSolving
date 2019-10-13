input()
st = str(input())
while ("01" in st or "10" in st):
    st = st.replace("01","")
    st = st.replace("10", "")
    
print (len(st))

