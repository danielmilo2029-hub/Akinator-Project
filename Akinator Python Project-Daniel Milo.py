print("Welcome to my Akinator Game")
name = input("What is your name? ")
print("Hi " + name)
print("My Name is Daniel, Nice to meet you!")
print("So here is what is going to happen, think of any baseball team and I am going to guess what team you are thinking of")

# Easter egg, if the user has the same name as me
if name == "Daniel":
    print("Wait... that is MY name too! Are you me?!")

# Question 1-Asking if their team is in the AL or NL

q1 = input("Question 1: Is your team in the American League? (yes/no): ")

if q1 == "yes":

    print("Ok so your team is in the American League!")

    q2 = input("Question 2: Is your team in the AL East? (yes/no): ")

#AL East
    if q2 == "yes":

        # Now asking about specific AL East teams 
        q3 = input("Question 3: Is your team the New York Yankees? (yes/no):")

        if q3 == "yes":

            # Yankees are my favorite team so i had to say something
            print("THE NEW YORK YANKEES! That is my favorite team too!! Great pick " + name + "!")

        else:
            q4 = input("Question 4: Is your team the Boston Red Sox? (yes/no):")

            if q4 == "yes":

                # Red Sox are my least favorite so i had to say something about that too
                print("Ugh... THE BOSTON RED SOX?! Really " + name + "? That is my LEAST favorite team!")

            else:
                q5 = input("Question 5: Is your team the Toronto Blue Jays? (yes/no): ")

                if q5 == "yes":
                    print("I KNEW IT! THE TORONTO BLUE JAYS!")

                else:
                    q6 = input("Question 6: Is your team the Baltimore Orioles? (yes/no): ")

                    if q6 == "yes":
                        print("I KNEW IT! THE BALTIMORE ORIOLES!")

                    else:

                        # Only AL East team left
                        print("Then it must be... THE TAMPA BAY RAYS!")

#AL Central
    else:

        q2b = input("Question 3: Is your team in the AL Central? (yes/no): ")

        if q2b == "yes":

            # Now asking about specific AL Central teams
            q3 = input("Question 4: Is your team the Chicago White Sox? (yes/no): ")

            if q3 == "yes":
                print("I KNEW IT! THE CHICAGO WHITE SOX!")

            else:
                q4 = input("Question 5: Is your team the Cleveland Guardians? (yes/no): ")

                if q4 == "yes":
                    print("I KNEW IT! THE CLEVELAND GUARDIANS!")

                else:
                    q5 = input("Question 6: Is your team the Minnesota Twins? (yes/no): ")

                    if q5 == "yes":
                        print("I KNEW IT! THE MINNESOTA TWINS!")

                    else:
                        q6 = input("Question 7: Is your team the Detroit Tigers? (yes/no): ")

                        if q6 == "yes":
                            print("I KNEW IT! THE DETROIT TIGERS!")

                        else:

                            # Only AL Central team left
                         print("Then it must be... THE KANSAS CITY ROYALS!")

        else:

            # Process of elimination, must be AL West
            print("Ok so your team must be in the AL West!")

            # Now asking about specific AL West teams
            q3 = input("Question 4: Is your team the Houston Astros? (yes/no): ")

            if q3 == "yes":
                print("I KNEW IT! THE HOUSTON ASTROS!")

            else:
                q4 = input("Question 5: Is your team the Seattle Mariners? (yes/no): ")

                if q4 == "yes":
                    print("I KNEW IT! THE SEATTLE MARINERS!")

                else:
                    q5 = input("Question 6: Is your team the Texas Rangers? (yes/no): ")

                    if q5 == "yes":
                        print("I KNEW IT! THE TEXAS RANGERS!")

                    else:
                        q6 = input("Question 7: Is your team the Los Angeles Angels? (yes/no): ")

                        if q6 == "yes":
                            print("I KNEW IT! THE LOS ANGELES ANGELS!")

                        else:

                            # Only AL West team left
                            print("Then it must be... THE OAKLAND ATHLETICS!")

else:

    qNL = input("Question 2: Is your team in the National League? (yes/no): ")

#Their team is in the NL
    if qNL == "yes":

        print("Ok so your team is in the National League!")

        # Asking which NL division their team is in
        q2 = input("Question 2: Is your team in the NL East? (yes/no): ")

        if q2 == "yes":

            # Now asking about specific NL East teams 
            q3 = input("Question 3: Is your team the Atlanta Braves? (yes/no): ")

            if q3 == "yes":
                print("I KNEW IT! THE ATLANTA BRAVES!")

            else:
                q4 = input("Question 4: Is your team the New York Mets? (yes/no): ")

                if q4 == "yes":
                    print("Are we serious! Why choose the mets??!! They suck")

                else:
                    q5 = input("Question 5: Is your team the Philadelphia Phillies? (yes/no): ")

                    if q5 == "yes":
                        print("I KNEW IT! THE PHILADELPHIA PHILLIES!")

                    else:
                        q6 = input("Question 6: Is your team the Miami Marlins? (yes/no): ")

                        if q6 == "yes":
                            print("I KNEW IT! THE MIAMI MARLINS!")

                        else:

                            # Only NL East team left
                            print("Then it must be... THE WASHINGTON NATIONALS!")

#NL Central
        else:

            q2b = input("Question 3: Is your team in the NL Central? (yes/no): ")

            # NL CENTRAL 
            if q2b == "yes":

                # Now asking about specific NL Central teams
                q3 = input("Question 4: Is your team the Chicago Cubs? (yes/no): ")

                if q3 == "yes":
                    print("I KNEW IT! THE CHICAGO CUBS!")

                else:
                    q4 = input("Question 5: Is your team the St. Louis Cardinals? (yes/no): ")

                    if q4 == "yes":
                        print("I KNEW IT! THE ST. LOUIS CARDINALS!")

                    else:
                        q5 = input("Question 6: Is your team the Milwaukee Brewers? (yes/no): ")

                        if q5 == "yes":
                            print("I KNEW IT! THE MILWAUKEE BREWERS!")

                        else:
                            q6 = input("Question 7: Is your team the Pittsburgh Pirates? (yes/no): ")

                            if q6 == "yes":
                                print("I KNEW IT! THE PITTSBURGH PIRATES!")

                            else:

                                # Only NL Central team left
                                print("Then it must be... THE CINCINNATI REDS!")

            else:

                # Process of elimination, must be NL West
                print("Ok so your team must be in the NL West!")

                # Now asking about specific NL West teams 
                q3 = input("Question 4: Is your team the Los Angeles Dodgers? (yes/no): ")

                if q3 == "yes":
                    print("I KNEW IT! THE LOS ANGELES DODGERS!")

                else:
                    q4 = input("Question 5: Is your team the San Francisco Giants? (yes/no): ")

                    if q4 == "yes":
                        print("I KNEW IT! THE SAN FRANCISCO GIANTS!")

                    else:
                        q5 = input("Question 6: Is your team the San Diego Padres? (yes/no): ")

                        if q5 == "yes":
                            print("I KNEW IT! THE SAN DIEGO PADRES!")

                        else:
                            q6 = input("Question 7: Is your team the Arizona Diamondbacks? (yes/no): ")

                            if q6 == "yes":
                                print("I KNEW IT! THE ARIZONA DIAMONDBACKS!")

                            else:

                                # Only NL West team left
                                print("Then it must be... THE COLORADO ROCKIES!")

    else:

        # Give up ending
        print("I give up! You either did not pick an MLB team or answered incorrectly.")

print("Thanks for playing my Akinator Game " + name + "! I really hope you enjoyed playing it!")
