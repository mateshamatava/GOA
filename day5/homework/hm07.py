# მომხმარებელს შემოაყვანინეთ სულ პროდუქტების ფასი და ფასდაკლების პროცენტი, გამოთვალეთ ფასდაკლების თანხა და საბოლოო ფასი
#   ფასდაკლება = ფასი x პროცენტი / 100
#   საბოლოო ფასი = საწყისი ფასი - ფასდაკლება

price = float(input("Enter price "))
percent = float(input("Enter discount percent "))

discount = price * percent / 100
total = price - discount

print("Discount:", discount)
print("Final price:", total)