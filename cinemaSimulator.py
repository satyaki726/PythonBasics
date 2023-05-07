films = {
    "Finding Dory":[3,5],
    "Bourne": [18,5],
    "Trazan": [15,5],
    "Ghost Buster": [12,5]
}

while True:
    choice = input("Which film do you want to see: ").strip().title()
    if choice in films:
        age = int(input("How old are you: ").strip())
        
        #check user age
        if age>=films[choice][0]:
            #check enough seats
            if films[choice][1]> 0 :
                print("Enjoy the film")
                films[choice][1] = films[choice][1]-1
                print("Latest Number Of Seats:" ,films[choice][1])
            else:
                print("Sorry not enough seats")
        else:
            print("Not eligible to watch")    
    else:
        print("We don't have that film")