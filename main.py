import Project5Start
game_data = Project5Start.get_project5_data()

user_input = input("What do you want to do:\n1. find recent games\n2. Find total copies sold\n3. Find average revenue per year\n4. Find the highest average revenue per year\n5. Find all the games that have sold at least X copies\n")
#user is asked to type a number 1-5. The number they type in answers the question related to that number
#/n is used to have each option on a different line
if user_input == "1":
    year = int(input("Enter a year:"))
    for game in game_data:
        if game["release"] >= year:
            print(f'{game["name"]} was released in {game["release"]}')
            #takes the game of the user and prints out name of every game

if user_input =="2":
    the_game= input("Enter a game:")
    for game in game_data:
        if game["name"]== the_game:
            print(f"{game['name']} has sold {game['total_sales']// game['price']} copies")

#finds the total copies by dividing total sales by the price of the game

if user_input =="3":
    the_game = input("Enter a game:")
    for game in game_data:
        if game["name"] == the_game:
            years_since_release = 2023 - game["release"]
            average_sales= (game["total_sales"])/ (years_since_release)
            print(f"{game['name']} makes {average_sales} dollars per year")
            #Takes the game the user enters and takes the total sales and divides by how many years the game has been out

if user_input =="4":
    for game in game_data:
        highest_avg_revenue= 0
        highest_avg_revenue_name = ""
        years_since_release = 2023 - game["release"]
        if years_since_release== 0:
           years_since_release = 1
        average_sales = (game["total_sales"]) / (years_since_release)

        if average_sales > highest_avg_revenue:
            highest_avg_revenue = average_sales
            highest_avg_revenue_name = game['name']
    print(f"{game['name']} has the highest average revenue with {average_sales} dollars per year")
# finds highest average sales per year for each game
# if the years_since_release variable is equal to 0, it will be changed to 1 to prevent program dividing by 0 and crashing
#If the average sales is highest, the number will be stored in highest_avg_revenue and the name will be stored in  highest_avg_revenue_name
#program then prints the name with the highest average revenue and the highest average revenue amount

if user_input == "5":
    for game in game_data:

        num_copies = (game["total_sales"] / game["price"])
        user_response= int(input("How many copies: "))
        games_with_x_copies_name= ""



        if num_copies >= user_response:
            games_with_x_copies_name= game["name"]
        print(games_with_x_copies_name)
        #I'm not sure why its not working right. I am trying to tell the program if the number of copies sold is greater or equal to the number the user types in, print the name of the game.














