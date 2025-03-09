#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5
import random

# Generate two lists of 10 random numbers between 1 and 50
player_one = [random.randint(1, 50) for _ in range(10)]
player_two = [random.randint(1, 50) for _ in range(10)]

# Initialize counters for wins
player_one_wins = 0
player_two_wins = 0

# Compare the lists in order
for i in range(10):
    if player_one[i] > player_two[i]:
        player_one_wins += 1
    elif player_two[i] > player_one[i]:
        player_two_wins += 1

# Find the highest number and its index for each player
player_one_max = max(player_one)
player_one_max_index = player_one.index(player_one_max)

player_two_max = max(player_two)
player_two_max_index = player_two.index(player_two_max)

# Find the lowest number and its index for each player
player_one_min = min(player_one)
player_one_min_index = player_one.index(player_one_min)

player_two_min = min(player_two)
player_two_min_index = player_two.index(player_two_min)

# Display the lists
print("Player One =", player_one)
print("Player Two =", player_two)

# Report the results
print(f"Player one won {player_one_wins} times")
print(f"Player two won {player_two_wins} times")
print(f"Player one's highest number is {player_one_max} at index {player_one_max_index}")
print(f"Player two's highest number is {player_two_max} at index {player_two_max_index}")
print(f"Player one's lowest number is {player_one_min} at index {player_one_min_index}")
print(f"Player two's lowest number is {player_two_min} at index {player_two_min_index}")
