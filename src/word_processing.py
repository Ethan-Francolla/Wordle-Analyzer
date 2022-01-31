# Define a function to collect the corresponding data for the first word entered
def get_first_word_data():
    # Globalize data variables that will be used in other modules
    global word_1_char_1_data,word_1_char_2_data,word_1_char_3_data,word_1_char_4_data,word_1_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word Adieu as the your first guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_1_data = str(input("A: "))
        if word_1_char_1_data == 'g' or word_1_char_1_data == 'y' or word_1_char_1_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's second character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_2_data = str(input("D: "))
        if word_1_char_2_data == 'g' or word_1_char_2_data == 'y' or word_1_char_2_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's third character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_3_data = str(input("I: "))
        if word_1_char_3_data == 'g' or word_1_char_3_data == 'y' or word_1_char_3_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fourth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_4_data = str(input("E: "))
        if word_1_char_4_data == 'g' or word_1_char_4_data == 'y' or word_1_char_4_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fifth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_5_data = str(input("U: "))
        if word_1_char_5_data == 'g' or word_1_char_5_data == 'y' or word_1_char_5_data == 'gr':
            continue_with_loop = 1


# Define a function to process the first word data
def process_first_word_data():
    # Out put a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list
    possible_char_1_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_2_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_3_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_4_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_5_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # Create a list of letters that are known to be in the word
    global known_letters_list
    known_letters_list =[]

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_1_data == 'g':
        if 'a' in possible_char_1_list:
            possible_char_1_list.remove('a')
        if 'a' in possible_char_2_list:
            possible_char_2_list.remove('a')
        if 'a' in possible_char_3_list:
            possible_char_3_list.remove('a')
        if 'a' in possible_char_4_list:
            possible_char_4_list.remove('a')
        if 'a' in possible_char_5_list:
            possible_char_5_list.remove('a')
    if word_1_char_1_data == 'y':
        if 'a' in possible_char_1_list:
            possible_char_1_list.remove('a')
        if 'a' not in known_letters_list:
            known_letters_list.append('a')
    if word_1_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append('a')
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_2_data == 'g':
        if 'd' in possible_char_1_list:
            possible_char_1_list.remove('d')
        if 'd' in possible_char_2_list:
            possible_char_2_list.remove('d')
        if 'd' in possible_char_3_list:
            possible_char_3_list.remove('d')
        if 'd' in possible_char_4_list:
            possible_char_4_list.remove('d')
        if 'd' in possible_char_5_list:
            possible_char_5_list.remove('d')
    if word_1_char_2_data == 'y':
        if 'd' in possible_char_2_list:
            possible_char_2_list.remove('d')
        if 'd' not in known_letters_list:
            known_letters_list.append('d')
    if word_1_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append('d')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_3_data == 'g':
        if 'i' in possible_char_1_list:
            possible_char_1_list.remove('i')
        if 'i' in possible_char_2_list:
            possible_char_2_list.remove('i')
        if 'i' in possible_char_3_list:
            possible_char_3_list.remove('i')
        if 'i' in possible_char_4_list:
            possible_char_4_list.remove('i')
        if 'i' in possible_char_5_list:
            possible_char_5_list.remove('i')
    if word_1_char_3_data == 'y':
        if 'i' in possible_char_3_list:
            possible_char_3_list.remove('i')
        if 'i' not in known_letters_list:
            known_letters_list.append('i')
    if word_1_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append('i')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_4_data == 'g':
        if 'e' in possible_char_1_list:
            possible_char_1_list.remove('e')
        if 'e' in possible_char_2_list:
            possible_char_2_list.remove('e')
        if 'e' in possible_char_3_list:
            possible_char_3_list.remove('e')
        if 'e' in possible_char_4_list:
            possible_char_4_list.remove('e')
        if 'e' in possible_char_5_list:
            possible_char_5_list.remove('e')
    if word_1_char_4_data == 'y':
        if 'e' in possible_char_4_list:
            possible_char_4_list.remove('e')
        if 'e' not in known_letters_list:
            known_letters_list.append('e')
    if word_1_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append('e')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_5_data == 'g':
        if 'u' in possible_char_1_list:
            possible_char_1_list.remove('u')
        if 'u' in possible_char_2_list:
            possible_char_2_list.remove('u')
        if 'u' in possible_char_3_list:
            possible_char_3_list.remove('u')
        if 'u' in possible_char_4_list:
            possible_char_4_list.remove('u')
        if 'u' in possible_char_5_list:
            possible_char_5_list.remove('u')
    if word_1_char_5_data == 'y':
        if 'u' in possible_char_5_list:
            possible_char_5_list.remove('u')
        if 'u' not in known_letters_list:
            known_letters_list.append('u')
    if word_1_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append('u')


# Define a function to collect the corresponding data for the first word entered
def get_second_word_data():
    # Globalize data variables that will be used in other modules
    global word_2_char_1_data,word_2_char_2_data,word_2_char_3_data,word_2_char_4_data,word_2_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word Cloys as the your second guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_1_data = str(input("C: "))
        if word_2_char_1_data == 'g' or word_2_char_1_data == 'y' or word_2_char_1_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's second character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_2_data = str(input("L: "))
        if word_2_char_2_data == 'g' or word_2_char_2_data == 'y' or word_2_char_2_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's third character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_3_data = str(input("O: "))
        if word_2_char_3_data == 'g' or word_2_char_3_data == 'y' or word_2_char_3_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fourth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_4_data = str(input("Y: "))
        if word_2_char_4_data == 'g' or word_2_char_4_data == 'y' or word_2_char_4_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fifth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_5_data = str(input("S: "))
        if word_2_char_5_data == 'g' or word_2_char_5_data == 'y' or word_2_char_5_data == 'gr':
            continue_with_loop = 1


# Define a function to process the second word data
def process_second_word_data():
    # Out put a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_1_data == 'g':
        if 'c' in possible_char_1_list:
            possible_char_1_list.remove('c')
        if 'c' in possible_char_2_list:
            possible_char_2_list.remove('c')
        if 'c' in possible_char_3_list:
            possible_char_3_list.remove('c')
        if 'c' in possible_char_4_list:
            possible_char_4_list.remove('c')
        if 'c' in possible_char_5_list:
            possible_char_5_list.remove('c')
    if word_2_char_1_data == 'y':
        if 'c' in possible_char_1_list:
            possible_char_1_list.remove('c')
    if word_2_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append('c')
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_2_data == 'g':
        if 'l' in possible_char_1_list:
            possible_char_1_list.remove('l')
        if 'l' in possible_char_2_list:
            possible_char_2_list.remove('l')
        if 'l' in possible_char_3_list:
            possible_char_3_list.remove('l')
        if 'l' in possible_char_4_list:
            possible_char_4_list.remove('l')
        if 'l' in possible_char_5_list:
            possible_char_5_list.remove('l')
    if word_2_char_2_data == 'y':
        if 'l' in possible_char_2_list:
            possible_char_2_list.remove('l')
    if word_2_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append('l')

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_3_data == 'g':
        if 'o' in possible_char_1_list:
            possible_char_1_list.remove('o')
        if 'o' in possible_char_2_list:
            possible_char_2_list.remove('o')
        if 'o' in possible_char_3_list:
            possible_char_3_list.remove('o')
        if 'o' in possible_char_4_list:
            possible_char_4_list.remove('o')
        if 'o' in possible_char_5_list:
            possible_char_5_list.remove('o')
    if word_2_char_3_data == 'y':
        if 'o' in possible_char_3_list:
            possible_char_3_list.remove('o')
    if word_2_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append('o')

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_4_data == 'g':
        if 'y' in possible_char_1_list:
            possible_char_1_list.remove('y')
        if 'y' in possible_char_2_list:
            possible_char_2_list.remove('y')
        if 'y' in possible_char_3_list:
            possible_char_3_list.remove('y')
        if 'y' in possible_char_4_list:
            possible_char_4_list.remove('y')
        if 'y' in possible_char_5_list:
            possible_char_5_list.remove('y')
    if word_2_char_4_data == 'y':
        if 'y' in possible_char_4_list:
            possible_char_4_list.remove('y')
    if word_2_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append('y')

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_5_data == 'g':
        if 's' in possible_char_1_list:
            possible_char_1_list.remove('s')
        if 's' in possible_char_2_list:
            possible_char_2_list.remove('s')
        if 's' in possible_char_3_list:
            possible_char_3_list.remove('s')
        if 's' in possible_char_4_list:
            possible_char_4_list.remove('s')
        if 's' in possible_char_5_list:
            possible_char_5_list.remove('s')
    if word_2_char_5_data == 'y':
        if 's' in possible_char_5_list:
            possible_char_5_list.remove('s')
    if word_2_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append('s')
