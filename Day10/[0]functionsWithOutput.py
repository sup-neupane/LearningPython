#Functions with output: These typr of functions return some output
#e.g.
def format_name(first_name,last_name):  #A function that converts name to title case
    formatted_first = first_name.title()
    formatted_last = last_name.title()
    return f"{formatted_first} {formatted_last}"


print(format_name("Suparna","nEUPANE"))


#We have built in functions with output such as len(),title() etc


#Multiple return values
# When computer encounters a line with return keyword then it indicates end of function we may use multiple return to terminate function

def change_name(first_name,last_name):  #A function that converts name to title case
    if first_name == "" or last_name == "":
        return                          #This returns None if any of input is empty and terminate program early.You may also return a message
    formatted_first = first_name.title()
    formatted_last = last_name.title()
    return f"{formatted_first} {formatted_last}"

print(change_name("","nEUPANE"))   #This prints None



#Challenge: Days in a Month
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(input_year,input_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
     return "Invalid Month"
  if is_leap(input_year) and month == 2:     
    return 29
  return month_days[month -1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
