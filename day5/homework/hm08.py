#  მომხმარებელს შემოაყვანინეთ წიგნის გვერდების რაოდენობა, რამდენ გვერდს კითხულობს ერთ დღეში და  გამოთვალეთ რამდენი დღე დასჭირდება წიგნის წასაკითხად


pages = int(input("Enter book pages "))
daily = int(input("Enter pages per day "))

days = pages / daily

print("days", days)