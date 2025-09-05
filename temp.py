temp_unit = input("Are you converting from farrenheit (F) or celcius (C)?")
temp = input("How many degrees " + temp_unit + " are you converting?")

if temp_unit == "C":
    c_temp_int = int(temp)
    result = (c_temp_int * 1.8 ) + 32
    final_result = str(result)
    print(final_result + " degrees farrenheit")
elif temp_unit == "F":
    f_temp_int = int(temp)
    result = (f_temp_int - 32 ) / 1.8
    final_result = str(result)
    print(final_result + " degrees celcius")
else:
    print("error")