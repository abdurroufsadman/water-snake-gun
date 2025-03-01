p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is a scam")
else:
    print("this coomment is not a spam")