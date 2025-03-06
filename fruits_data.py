def main():
    # Initialize an empty dictionary to store fruit data
    fruit = {}

    # Get the number of fruits to input (input statement). This will be the 
    # number of sets of data you need to collect.

    num = int(input("Please enter how many fruits you'd like to index: "))

    # Collect data for the number of fruits above from the user. Should include name, color, 
    # weight in lbs, and price. Once each set of data points is collected
    # Think about what kind of control structure to create to complete this process
    for fruits in range(num):
        fruity = input("What is the name of your fruit: ")
        fruit['name'].append(fruity)
        color = input("What is the color of your fruit: ")
        fruit['color'].append(color)
        weight = float(input("What is the weight of your fruit in pounds: "))
        fruit['weight'].append(weight)
        price = float(input("What is the price of your fruit: "))
        fruit['price'].append(price)
        # After each set of input statements, store the data in the dictionary

    # Output each of the fruit's data as a vertical list. This happens one time
    # for each of the fruits in the dictionary. 
    

if __name__ == "__main__":
    main()