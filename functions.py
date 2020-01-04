import random


def check_for_cursing(message):
    curse_words = ["fuck", "shit", "bitch", "dick", "slut", "whore", "ass", "asshole"]
    for item in curse_words:
        if item in message:
            return "Please, no cursing. Try again. This time, keep it classy. Type boto for more information."
        else:
            return check_type(message)
            # return check_type(message) + " Type 'boto' for more information."


def check_type(message):
    type_check = message.split(", ")
    if type_check[0].isdigit() and type_check[1].isdigit() and len(type_check) == 2:
        return return_max_of_two(type_check)
    if type_check[0].isdigit() and type_check[1].isdigit() and type_check[2].isdigit() and len(type_check) == 3:
        return return_max_of_three(type_check)
    else:
        check_start = check_starts_with(message)
        check_end = check_ends_with(message)
        return check_start + check_end


def check_starts_with(message):
    words_array = message.split()
    first_word = words_array[0].lower()
    if first_word == "hello " or first_word == "hello" or first_word == "hello," \
            or first_word == "hello!" or first_word == "hello." or first_word == "hello?":
        return "Hello. "
    if first_word == "hi " or first_word == "hi" or first_word == "hi," \
            or first_word == "hi!" or first_word == "hi." or first_word == "hi?":
        return "Hi to you. "
    elif first_word.startswith("shalom"):
        return "Shalom alechem. "
    elif first_word.startswith("hola"):
        return "Hola. Hablo un poquito espanol. "
    elif first_word == "hey ":
        return "Hey is for horses. "
    else:
        return ""


def check_ends_with(user_input):
    additional_response = additional_processing(user_input)
    if user_input.endswith("?"):
        resp = "Great question. " + additional_response
        return resp
    elif user_input.endswith("!"):
        resp = "I'm excited too. " + additional_response
        return resp
    elif user_input.endswith("."):
        resp = "OK. Let me respond. " + additional_response
        return resp
    else:
        return additional_response


def additional_processing(message):
    if check_for_location(message) is not None:
        return check_for_location(message)
    if check_for_food(message) is not None:
        return check_for_food(message)
    if check_for_translate_to_robbers(message) is not None:
        return check_for_translate_to_robbers(message)
    if check_for_reverse(message) is not None:
        return check_for_reverse(message)
    if check_for_palindrome(message) is not None:
        return check_for_palindrome(message)
    return counter_number_characters(message)


def counter_number_characters(message):
    counter = 0
    for item in message:
        counter += 1
    if counter == 1:
        return check_vowel(message)
    else:
        return f"I love your name! I'm a robot, so I'm great with names. Yours is {message}. As a side note, " \
               f" your name is {counter} letters. Are you from Kansas City, Chicago, New York, or Tel Aviv? If so, " \
               f"type the city's name. Otherwise, type, 'nope'."


def check_for_location(message):
    locations = ["tel aviv", "kansas city", "chicago", "new york", "nope"]
    for place in locations:
        if message.lower().find(place) != -1:
            return respond_location(place)


def respond_location(city):
    next_prompt = "Let's see if we have anything in common. Type the names of the following foods that you like. " \
                     "Peanut butter, chocolate, and sweet potato. If you like none, type 'none'?"
    if city == "tel aviv":
        return "Really?! Great city. " + next_prompt
    elif city == "kansas city":
        return "No way! I grew up there. " + next_prompt
    elif city == "chicago":
        return "The windy city. I lived there for a long time. " + next_prompt
    elif city == "new york":
        return "There's no other place like NYC. " + next_prompt
    else:
        return "Shoot. " + next_prompt


def check_for_food(message):
    foods = ["peanut butter", "chocolate", "sweet potato", "none"]
    for item in foods:
        if message.lower().find(item) != -1:
            return respond_food(message)


def respond_food(message):
    foods = ["peanut butter", "chocolate", "sweet potato"]
    array = message.split(", ")
    foods_in_common = []
    for item in foods:
        for entry in array:
            if item == entry.lower():
                foods_in_common.append(item)
    string = ", ".join(foods_in_common)
    if string == "":
        return "Shoot. I guess we don't have that in common. Type 'boto' to learn what I can do."
    else:
        return f"Alright! I also like {string}. Type 'boto' to learn more about what I can do."


def return_max_of_two(numbers):
    first = int(numbers[0])
    second = int(numbers[1])
    if first > second:
        return f"{first} is greater than {second}."
    elif second > first:
        return f"{second} is greater than {first}."
    else:
        return "You entered the same number twice!"


def return_max_of_three(numbers):
    first = int(numbers[0])
    second = int(numbers[1])
    third = int(numbers[2])
    if first > second and first > third:
        return f"{first} is greater than {second} and {third}."
    elif second > first and second > third:
        return f"{second} is greater than {first} and {third}."
    elif third > first and third > second:
        return f"{third} is greater than {first} and {second}."
    else:
        return "You entered the same number three times!"


def check_for_translate_to_robbers(message):
    array = message.split()
    if message.lower().startswith("robber's language"):
        new = array[2:]
        joined = " ".join(new)
        return translate_to_robbers(joined)


def translate_to_robbers(message):
    translated = ""
    if message == "":
        return "You forgot to enter what you wanted me to translate."
    else:
        for l in message:
            if l in ["a", "e", "i", "o", "u", " "]:
                translated += l
            else:
                translated += f"{l}o{l}"
        return translated


def check_for_reverse(message):
    array = message.split()
    new = array[1:]
    joined = " ".join(new)
    if message.lower().startswith("reverse"):
        return reverse_message(joined)


def reverse_message(message):
    if message == "":
        return "You forgot to enter what you wanted me to reverse."
    else:
        reversed_message = ""
        for l in message:
            reversed_message = l + reversed_message
        return reversed_message


def check_for_palindrome(message):
    print(message)
    array = message.split()
    new = array[1:]
    joined = " ".join(new)
    if message.lower().startswith("palindrome"):
        return palindrome(joined)


def palindrome(message):
    if message == "":
        resp = "You forgot to enter what you wanted me to check."
    else:
        backwards = ""
        for l in message:
            backwards = l + backwards
        if message == backwards:
            resp = f"Yes, {message} is a palindrome!"
        else:
            resp = f"No, {message} is NOT a palindrome."
    return resp


def check_vowel(message):
    if message.lower() in ["a", "e", "i", "o", "u"]:
        return f"{message} is a vowel."
    elif message.lower() == "y":
        return f"Sometimes {message} is a vowel."
    else:
        return f"{message} is not a vowel."


def select_animation():
    images_array = ["afraid", "bored", "confused", "crying", "dancing", "dog", "excited", "giggling", "heartbroke",
                    "inlove", "laughing", "money", "no", "ok", "takeoff", "waiting"]
    i = random.randint(0, len(images_array) - 1)
    return images_array[i]
