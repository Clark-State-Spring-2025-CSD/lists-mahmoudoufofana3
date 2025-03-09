#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#You must use a list for this assignment. Not using a list will result in an automatic 0.
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#[pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken] 
#You entered a total of 62 characters
# Create a list to store the foods
foods = []

# Prompt the user to enter five foods
for i in range(5):
    food = input("Enter a food: ")
    foods.append(food)

# Display the list on one line, each item separated by commas
print("\nYour entered foods are:")
print(", ".join(foods))

# Calculate the total number of characters entered
total_characters = sum(len(food) for food in foods)

# Display the total number of characters to the user
print(f"You entered a total of {total_characters} characters.")
