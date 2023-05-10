seconds_unit = "seconds"
seconds_calculation= 24*60*60
user_input=input("enter the element\n >>")

def seconds_cal(user_input):
    return(f"the {user_input} days has {seconds_calculation} {seconds_unit}")

def validation_execute():
    try:
        if user_input.isdigit():
            usr_input_number=int(user_input)
        if usr_input_number>0:
            val=seconds_cal(int(user_input))
            print(val)
        elif usr_input_number==0:
            print("no zero's please..")
        elif usr_input_number<0:
            print("no negatives dattabayo..")
        else:
            print("invalid number entered")
    except UnboundLocalError:
        if user_input =="*"or"/"or"-"or"+"or"!"or"@"or"#"or"$"or"%"or"^"or"&"or"()"or"=":
            print("no characters please")
        else:
            print("hello")

validation_execute()
print("thanks for your time!!")



