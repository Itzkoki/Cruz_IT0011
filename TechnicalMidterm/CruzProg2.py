year_month = {1:'January', 2:'February', 3:'March', 4:'April',5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

date_str = input("Enter the date in MM/DD/YYYY format: ")

if len(date_str) == 10 and date_str[2] == '/' and date_str[5] == '/' and date_str[:2].isdigit() and date_str[3:5].isdigit() and date_str[6:].isdigit():
    month, date, year = map(int, date_str.split('/'))
    y = year_month.get(month, "Invalid month")
    
    if y != "Invalid month" and 1 <= date <= 31:
        print(f"{y} {date}, {year}")
    else:
        print("Invalid date format!")
else:
    print("Invalid input format! Use MM/DD/YYYY")