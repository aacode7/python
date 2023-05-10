seconds_count=24*60
name_of_unit="hours"
def no_of_seconds(no_of_days):
    return(f"{no_of_days} days has {no_of_days*seconds_count} {name_of_unit}")
    
def validation_and_execute():
    if user_input.isdigit():
        user_input_number=int(user_input)
        if user_input_number >0:
            cal_value=no_of_seconds(int(user_input_number))
            print(cal_value)
        elif user_input_number==0:
            print("No zeros please..")
    else:
        print("Invalid input.Only positive numbers please >w<")
user_input=input("Hello,fill details\n")
validation_and_execute()




