def converter(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    return hour_str + minute_str

# Test cases
print(converter(12, 15, "am"))  
print(converter(9, 30, "pm"))  



    
