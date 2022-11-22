from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
bidding_finished = False

# find highest bidder and declare winner
def find_highest_bidder(bidding_record):
    highest_bid = 0
   #bidding_record = {"Angela": 123, "James": 321} 
    for bidder in bidding_record: # bidder is "Angela"
        bid_amount = bidding_record[bidder] # accesing value and labeling it bid_amount
        # print(bid_amount)
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is the {winner} with a bid of ${highest_bid}')

            
while not bidding_finished: # if the user says yes keep looping
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))
    bids[name] = price # add name and bid into dict.
    # print(bids)
    should_continue = input('Are there any other bidders? Type "yes" or "no": ')
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()