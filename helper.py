def days_to_minute(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} hari sama dengan {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} hari sama dengan {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"



def validate_and_execute(days_and_unit_dict):
    try:
        user_input_num = int(days_and_unit_dict["days"])
        if user_input_num > 0:
            cal_result = days_to_minute(user_input_num, days_and_unit_dict["unit"])
            print(cal_result)
        elif user_input_num == 0:
            print("Anda memasukkan 0, silakan masukkan bilangan positif")
        else:
            print("you entered a negative number, please enter a valid number")
    except ValueError:
        print("input Anda bukan bilangan")



user_input_message = "Silakan masukkan bilangan dan unit konversi"