"""Restaurant rating lister."""

def get_scores():
    #Reads the ratings in from the file
    scores_text = open('scores.txt')
    #Assign scores to dicitonary
    scores = {}
    #Using a for loop, we iterate through each line in scores.txt, stripping all trilling characters, 
    for line in scores_text:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)
    
    return scores

def sort_scores(scores):
    for restaurant, score in sorted(scores.items()):
        print(f"{restaurant} was rated {score}.")

def add_restaurant(scores):
    print("Add a restaurant you went to recently along with your review score:")
    restaurant = input("Restaurant > ")
    rating = input("Your score > ")
    scores[restaurant] = rating

scores = get_scores()
add_restaurant(scores)
sort_scores(scores)