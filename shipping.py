weight = 1.5
#Ground Shipping
if weight <= 2:
  cost = weight * 1.5 + 20
elif weight >= 2 and weight <=6:
  cost = weight * 3 + 20
elif weight >= 6 and weight <=10:
  cost = weight * 4 + 20
elif weight > 10:
  cost = weight * 4.75 + 20
print(cost)
# Premium Ground Shipping
cost = 125
print(cost)
#Drone Shipping
if weight <= 2:
  cost = weight * 4.5
elif weight >= 2 and weight <=6:
  cost = weight * 9
elif weight >= 6 and weight <=10:
  cost = weight * 12
elif weight > 10:
  cost = weight * 14.25
print(cost)