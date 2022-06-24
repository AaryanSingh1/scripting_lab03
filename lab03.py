# defining main function
def main() :
    student_details = dict(
        'student_name' : 'Aaryan Singh', 

        'student_id' : '10274906', 

        'pizza_toppings' :
        [
            'pineapple', 
            'onions',
            'olives' 
        ], 

        'movies' : 
        [
            dict(
                'title' : 'Hangover (I, II, III)', 
                'genre' : 'Comedy'
            ), 
            dict(
                'title' : 'Bubble' 
                'genre' : [
                'anime',
                'parkour',
                'adventure']
            )
        ]

    )

    # adding a new movie
    new_movie = {'title' : 'Django Unchained', 'genre' : ['Comedy', 'Brutal']}
    student_details['movies'].append(new_movie)
   
    # adding a new topping 
    new_topping = ['pizza seasoning']
    student_details['pizza_toppings'].append(new_topping)

# **How to add to and modify each element in a list
def adding_topping(details, new_topping) :

    #adding new topping 
    details['topping'].extend(new_topping)

    #lowercasing the letters
    for i,p in enumerate(details['topping']) :
        details['topping'][i] = p.lower()
    
    #sorting the toppings in alphabetical order
    details['topping'].sort()

#to print a sentence using data from main
def printing_sentence(details) : 
    sentence = f"My name is" + {details['student_name']} + "but you can call me Sir" + {details['student_name'].removesuffix('Singh')} + '.\n'
    "My student ID is" + {details['student_id']}  
    print(sentence, "end = '\n\n'")

#printing the toppings with bullets
def bullets_toppings(details) :
    print("My favourite toppings are:")

    for p in details['topping']:
        print(f"- {p}")
    print()

#printing genres
def comma_genre(details) :
    print(f"My goto genres are", end='')
    for i,g in enumerate(details['movies']) :
        print(g['genre'], end='')
        if i < len(details['movies'])-1:
            print(', ', end='')
    print('.', end='\n\n')

#printing movies
def comma_genre(details) :
    print(f"My favourite movies are", end='')
    for i,g in enumerate(details['movies']) :
        print(g['title'], end='')
        if i < len(details['movies'])-1:
            print(', ', end='')
    print('.', end='\n\n')

#calling main function
main()
