def restaurant_bill_calculator():
    
    num_people = int(input("Enter the number of people: "))
    
    cost_per_meal = float(input("Enter the cost of each meal: $"))
    
    sales_tax_percentage = float(input("Enter the sales tax percentage: "))
    
    tip_percentage = float(input("Enter the tip percentage: "))

    total_cost_of_food = num_people * cost_per_meal

    total_sales_tax = total_cost_of_food * (sales_tax_percentage / 100)

    total_tip_amount = total_cost_of_food * (tip_percentage / 100)

    total_bill_per_person = (total_cost_of_food + total_sales_tax + total_tip_amount) / num_people

    print(f"\nTotal Cost of Food: ${total_cost_of_food:.2f}")
    
    print(f"Total Sales Tax: ${total_sales_tax:.2f}")
    
    print(f"Total Tip Amount: ${total_tip_amount:.2f}")
    
    print(f"Total Bill Amount Per Person: ${total_bill_per_person:.2f}")

restaurant_bill_calculator()