import art

print(art.logo)
bid_status = True
bid_list = {}

def find_highest_bid(bid_dictionary):
    max_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner of the auction is: {winner} with a bid of ${max_bid}")

while bid_status:
    # TODO-1: Ask the user for input
    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid: "))
    # TODO-2: Save data into dictionary {name: price}
    bid_list[name]  = bid
    # TODO-3: Whether if new bids need to be added
    is_bid_ongoing = input("Is someone else bidding?").lower()
    print("\n" * 20)
    if is_bid_ongoing == "no":
        bid_status = False
        find_highest_bid(bid_list)

    # TODO-4: Compare bids in dictionary





