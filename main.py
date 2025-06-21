import art

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder

    print(f"The Winner is {winner} with the Bidding Price of {highest_bid}")

# TODO-0: Print the logo

print(art.logo)

# TODO-1: Ask the user for input

user_dict = {}
continue_bidding = True
while continue_bidding:
    user_name = input ("Enter your name: ")
    user_bid_price = int(input("Enter your Price $: "))


    # TODO-2: Save data into dictionary {name: price}

    user_dict.update({user_name: user_bid_price}) # Updating the Dictionary using update() method
    # user_dict[user_name] = user_bid_price  # Updating the Dictionary in other way

    # TODO-3: Whether if new bids need to be added
    should_continue = input("Aare there any other bidders ? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(user_dict)
    elif should_continue == "yes":
        print("\n" * 20)


