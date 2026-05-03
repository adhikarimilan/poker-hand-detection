def find_poker_hand(hand):
    ranks=[]
    suits=[]
    possible_ranks=[]
    hand_ranks={10:" Royal Flush", 9:"Straight Flush", 8:"Four of a Kind", 7:"Full House", 6:"Flush", 5: "Straight", 4:"Three of a Kind", 3:"Two pair", 2:"pair", 1:"High Card"}
    card_ranks={'A':14,'K':13,'Q':12,'J':11,'10':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    for card in hand:
        if len(card)==3:
            ranks.append(card_ranks[card[0:2]])
        else:
            ranks.append(card_ranks[card[0].upper()])
        suits.append(card[len(card)-1].upper())
    sorted_ranks=sorted(ranks)
    hand_unique_rank_val=list(set(sorted_ranks))

    #check for royal flush, straight flush and flush
    if suits.count(suits[0])==5:
       if 14 in ranks and 13 in ranks and 12 in ranks and 11 in ranks and 10 in ranks:
           possible_ranks.append(10)
       elif all(sorted_ranks[i]==sorted_ranks[i-1]+1 for i in range(1,len(sorted_ranks))):
           possible_ranks.append(9)
       else:
           possible_ranks.append(6) #flush
    else:
    #four of kind and full house
     if len(hand_unique_rank_val) ==2:
         for val in hand_unique_rank_val:
             if sorted_ranks.count(val)==4:
                 possible_ranks.append(8) #four of a kind
             else:
                 possible_ranks.append(7) #full house

    #three of a kind and two pair
     elif len(hand_unique_rank_val) ==3:
         for val in hand_unique_rank_val:
             if sorted_ranks.count(val)==3:
                 possible_ranks.append(4) #three of a kind
             else:
                 possible_ranks.append(3) #two pair
     #pair
     elif len(hand_unique_rank_val) == 4:
         possible_ranks.append(2)

     else:
        possible_ranks.append(1)

    print(sorted_ranks, suits, hand_ranks[max(possible_ranks)])
    return  hand_ranks[max(possible_ranks)]

if __name__=="__main__":
    find_poker_hand(["KH", "Ah", "QH", "JH", "10H"])    # Royal Flush
    find_poker_hand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    find_poker_hand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    find_poker_hand(["2H", "2D", "2s", "10H", "10C"])  # Full House
    find_poker_hand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    find_poker_hand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    find_poker_hand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    find_poker_hand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    find_poker_hand(["2D", "2S", "9C", "KD", "10C"]) # Pair
    find_poker_hand(["KD", "5H", "2D", "10C", "JH"]) # High Card