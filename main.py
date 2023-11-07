import time

def connection_successful():
    print("A new window should have opened on your default browser.\nConnect through Spotify to begin your playlist creation journey")
    for i in range(1):
        print("Waiting...") 
        time.sleep(1) 
    # Upon successful connection:
    username = input("Enter username here: ")
    print("User connection successful\n")
    # return 1 if successful, 0 if not
    return username

def menu_options():
    while True:
        try:
            choice = int(input("1. Create a new, catered playlist just for you\n2. Modify an existing playlist\n3. Delete an existing playlist\n4. Learn more about options 1-3\n5. Exit the program & log out\n>> "))
            if 0 < choice < 6:
                break
            else:
                print("Invalid input. Enter a number 1-5")
        except ValueError:
            print("Invalid input. Enter a number 1-5")

    return choice

################################
# PLAYLIST GENERATION          #
################################

def generate_playlist():
    print("Generating playlist...")
    for i in range(1):
        print("Loading...") 
        time.sleep(1) 

    # will be it's own function: display_new_playlist()

    print("Newly Created Playlist: ")
    playlist = [
        {"Artist": "Drake", "Title": "Marvin's Room", "Album": "Take Care"},
        {"Artist": "Brent Faiyaz", "Title": "Trust", "Album": "Lost"},
        {"Artist": "Clairo", "Title": "Amoeba", "Album": "Sling"},
        {"Artist": "Weston Estate", "Title": "Sixty", "Album": "Maggie Valley"}
    ]

    print("{:<3} | {:<15} | {:<15} | {:<15}".format("#", "Artist", "Title", "Album"))
    for i, song in enumerate(playlist, start=1):
        print("{:<3} | {:<15} | {:<15} | {:<15}".format(i, song['Artist'], song['Title'], song['Album']))
    print("...")
    # will be own function ^
    return playlist

def create_new_playlist(): 
    new_playlist = generate_playlist() # generates a new playlist 
    while True:
        try:
            add_to_lib = str(input("Would you like to add this playlist to your library? (Y/N)\n>> "))
            if add_to_lib.lower() == "exit":
                print("Returning to menu\n") # exit line
                break
            elif add_to_lib.lower() == "menu":
                print("Returning to menu\n") # exit line
                break
            
            if add_to_lib.lower() == "y":
                # add it to user library
                # add_to_library(new_playlist)
                print("Successfully added to library.")
                again = input("Generate another one? (Y/N)\n>> ")
                if again.lower() == "exit":
                    print("Returning to menu\n") # exit line
                    break
                elif again.lower() == "menu":
                    print("Returning to menu\n") # exit line
                    break
                if again.lower() == "n":
                    return 1
                elif again.lower() == "y":
                    print("Generating new playlist...")
                    return 3
            elif add_to_lib.lower() == "n":
                again = input("Generate another one? (Y/N)\n>> ")
                if again.lower() == "exit":
                    print("Returning to menu\n") # exit line
                    break
                elif again.lower() == "menu":
                    print("Returning to menu\n") # exit line
                    break
                if again.lower() == "n":
                    return 0
                elif again.lower() == "y":
                    print("Generating new playlist...")
                    # return 2
                    return 2
                
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input. Try again")

    # return 0 = don't add, don't make new
    # returnh 1 = successfully added, don't make new
    # return 2 = don't add, generate another
    # return 3 = successfully added, generate another
    # return -1 = menu
    return -1

################################
# PLAYLIST MODIFICATION        #
################################

def playlist_print(playlist=""):
    playlist_name = "late night walks"
    playlist = [
        {"Artist": "Drake", "Title": "Marvin's Room", "Album": "Take Care"},
        {"Artist": "Brent Faiyaz", "Title": "Trust", "Album": "Lost"},
        {"Artist": "Clairo", "Title": "Amoeba", "Album": "Sling"},
        {"Artist": "Weston Estate", "Title": "Sixty", "Album": "Maggie Valley"}
    ]

    print("{:<3} | {:<15} | {:<15} | {:<15}".format("#", "Artist", "Title", "Album"))
    for i, song in enumerate(playlist, start=1):
        print("{:<3} | {:<15} | {:<15} | {:<15}".format(i, song['Artist'], song['Title'], song['Album']))
    print("...")
    return

# returns the number of playlist user has
def playlist_list(): 
    
    playlist = [
        {"Count": "45", "Playlist Title": "Party Playlist!!"},
        {"Count": "23", "Playlist Title": "foggy morning mood"},
        {"Count": "30", "Playlist Title": "study music"},
        {"Count": "10", "Playlist Title": "late night walks"},
        {"Count": "10", "Playlist Title": "LOUD"}
    ]
    # get user num_playlist count
    num_playlists = len(playlist)
    print("\nYour playlists: \n")
    print("{:<3} | {:<6} | {:<20}".format("#", "Count", "Playlist Title"))
    for i, song in enumerate(playlist, start=1):
        print("{:<3} | {:<6} | {:<20}".format(i, song['Count'], song['Playlist Title']))
    return num_playlists

def playlist_add_a_song(playlist=""):
    print("What song would you like to add?") # will be input - also very hard lol
    print("playlist_add_a_song not implemented yet.\n")
    return

def playlist_delete_a_song(playlist="default"):
    print("playlist_delete_a_song not finished yet.")
    while True:
        try:
            confirmation = input("Are you sure you want to delete the song \nSONG_TITLE_HERE\n? (Y/N)\n>> ")
            if confirmation == "Y":
                print(f"Deleting song\"SONG_TITLE_HERE\"!\n") # exit line 
                return 1
            elif confirmation == "N":
                print("Deletion aborted... returning to menu\n") # exit line
                break
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input. Try again")
    return 0 # return 0 means user did not delete the song

def playlist_change_title(playlist=""):

    print("Are you sure you want to change the playlist title? (Y/N)\n>> ") # will be input()
    print("playlist_delete_a_song not implemented yet.\n")
    return


def playlist_to_modify():
    # WOULD HAVE ACCESS TO A LIST OF PLAYLIST WITH A DETERMINATE LENGTH
    num_playlists = playlist_list()
    while True:
        try:
            choice = input("Select the playlist you would like to modify (using #): ")
            if choice.lower() == "menu":
                print("Returning to menu\n") # exit line
                break
            if choice.lower() == "exit":
                print("Returning to menu\n") # exit line
                break
            choice = int(choice)
            choice -= 1
            if 0 < choice < num_playlists:
                return choice # exit line
            else: 
                print("Invalid input. Try again with a number of a playlist, ex: 2")
        except ValueError:
            print("Invalid input. Try again with a number of a playlist, ex: 2")
    return -1

def modify_playlists_options():
    playlist_choice = playlist_to_modify()
    if playlist_choice == -1:
        return -1
    """""""""
    TODO: playlist_to_modify should return a playlist as json string from the user's spotify account
        playlist_print     should take a parameter of the playlist_choice returned from playlist_to_modify
    """""""""
    playlist_print() # print the playlist they chose (PARAMETER) 
    while True:
        try:
            choice = input("""Select option (1-3)\ntype \'back\' to edit a different playlist\ntype \'menu\' to return to options menu\n\n1. Add a new song\n2. Delete a song\n3. Change playlist title \n>> """)
            if choice.lower() == "menu":
                print("Returning to menu\n")
                break
            if choice.lower() == "exit":
                print("Returning to menu\n") # exit line
                break
            if choice.lower() == "back":
                return -2 # back
            choice = int(choice)
            if 1 <= choice <= 3:
                return choice
            else: 
                print("Invalid input. Try again with a number of a playlist, ex: 2")
        except ValueError:
            print("Invalid input. Try again with a number of a playlist, ex: 2")
    # return -1 return to menu
    return -1

def modify_playlists():
    while True:
        choice = modify_playlists_options()
        if choice == -1: # user "menu" option
            return
        elif choice == -2: # user "back" option
            continue
        elif choice == 1:
            playlist_add_a_song() # will return a variable to let me know if break or not
            continue
        elif choice == 2:
            x = playlist_delete_a_song() # will return a variable to let me know if break or not
            continue
        elif choice == 3:
            playlist_change_title() # will return a variable to let me know if break or not
            continue


################################
# PLAYLIST DELETION            #
################################

# DELETES A FULL PLAYLIST
def playlist_delete(playlist="default"):
    print("playlist_delete not finished yet.")
    while True:
        try:
            confirmation = input(f"Are you sure you want to delete the playlist {playlist}? (Y/N)\n>> ")
            if confirmation == "Y":
                print("Deleting playlist...")
                print(f"Successfully deleteed playlist \"{playlist}\"!\n") #exit line
                return 1
            elif confirmation == "N":
                print("Deletion aborted... returning to menu\n") # exit line
                break
            else:
                print("Invalid input. Try again")
        except ValueError:
            print("Invalid input. Try again")
    return 0 # return 0 means user did not delete the playlist

def playlist_to_delete():
    # WOULD HAVE ACCESS TO A LIST OF PLAYLIST WITH A DETERMINATE LENGTH
    num_playlists = playlist_list()
    while True:
        try:
            choice = input("Select the playlist you would like to delete (using # or \"menu\" to exit): ")
            if choice.lower() == "menu":
                print("Returning to menu\n") # exit line
                break
            if choice.lower() == "exit":
                print("Returning to menu\n") # exit line
                break
            choice = int(choice)
            choice -= 1;
            if 0 < choice < num_playlists:
                return choice # intended result int return
            else: 
                print("Invalid input. Try again with a number of a playlist, ex: 2")
        except ValueError:
            print("Invalid input. Try again with a number of a playlist, ex: 2")
    return -1 # return to menu

def delete_a_playlist():
    while True:
        choice = playlist_to_delete()
        if choice == -1:
            break
        else:
            playlist_delete(choice)

    return

################################
# DOCUMENTATION                #
################################

def documentation():
    print("Not yet implemented, as the functions are not set in stone -- will write once they are more ~finalized~\n")

def menu_execute(choice):
    if choice == 1:
        create_new_playlist()
    elif choice == 2:
        modify_playlists()
    elif choice == 3:
        delete_a_playlist()
    elif choice == 4:
        documentation()
    else: 
        NotImplemented
    return


def main():
    print("Welcome to __CS361_Project__")
    username = connection_successful()

    print(f"Welcome, {username}!\nEnter a number 1-5 to select an option\nYou can return to this menu at any time by typing \"menu\"\n")

    while True:
        choice = menu_options() # integer choice 1-5
        if choice == 5:
            break
        menu_execute(choice)
    
    return


if __name__ == "__main__":
    main()