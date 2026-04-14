def calculate_restaurant_bill(meal_cost):

    service_charge = meal_cost * 0.10
    amount_after_service = meal_cost + service_charge
    tax = amount_after_service * 0.05
    tips = amount_after_service * 0.05
    total_bill = amount_after_service + tax + tips

    print(f"Meal Cost: {meal_cost}")
    print(f"Service Charge (10%): {service_charge:.2f}")
    print(f"Amount after Service Charge: {amount_after_service}")
    print(f"Tax (5%) : {tax:.2f}")
    print(f"Tips (5%) : {tips:.2f}")
    print(f"Total Bill: {total_bill}")
    print("Return:", total_bill)

#meal_cost_calc = float(input("Enter the meal cost: "))

#calculate_restaurant_bill(meal_cost_calc)

while True:
    try:
        meal_cost_calc = float(input("Enter the meal cost: "))
        calculate_restaurant_bill(meal_cost_calc)
        break
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the meal cost.")

    
