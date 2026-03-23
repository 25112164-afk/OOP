#1 
pi = 3.14159
radius = 5
volume = (4 / 3) * pi * (radius ** 3)
print(f"1. Volume of the sphere: {volume}")
print("-" * 30) 
#2
cover_price = 24.95
discount = 0.40
discounted_price = cover_price * (1 - discount)
total_books = 60
shipping_first = 3.00
shipping_rest = 0.75 * (total_books - 1)
total_shipping = shipping_first + shipping_rest
total_cost = (discounted_price * total_books) + total_shipping
print(f"2. Total wholesale cost: ${total_cost}")
print("-" * 30)
#3
start_hour = 6
start_minute = 52
easy_pace_sec = (8 * 60) + 15
tempo_pace_sec = (7 * 60) + 12
total_run_sec = (easy_pace_sec * 2) + (tempo_pace_sec * 3)
run_minutes = total_run_sec // 60
run_seconds = total_run_sec % 60
final_minute = start_minute + run_minutes
final_hour = start_hour + (final_minute // 60) 
final_minute = final_minute % 60 
print(f"3. Time to get home: {final_hour}:{final_minute}:{run_seconds} AM")