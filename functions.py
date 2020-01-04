import random
import requests, json
import config


def check_for_cursing(message):
    curse_words = ["fuck", "shit", "bitch", "dick", "slut", "whore", "ass", "asshole"]
    for item in curse_words:
        if item in message:
            return "Please, no cursing. Try again. This time, keep it classy. Type 'boto info' for more information."
        else:
            return check_type(message)


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
    if check_weather(message) is not None:
        return check_weather(message)
    if check_boto(message) is not None:
        return check_boto(message)
    array = message.split()
    if len(array) == 1:
        return counter_number_characters(message)
    else:
        return "Hmm. I don't understand. Have you tried searching Google or talking to your parents?"


def counter_number_characters(message):
    counter = 0
    for item in message:
        counter += 1
    if counter == 1:
        return check_vowel(message)
    else:
        return f"I love your name! I'm a robot, so I'm great with names. Yours is {message}." \
               f" Your name is {counter} letters. Are you from Kansas City, Chicago, New York, or Tel Aviv? If so, " \
               f"type the city's name. Otherwise, type, 'nope'."


def check_for_location(message):
    locations = ["tel aviv", "kansas city", "chicago", "new york", "nope"]
    for place in locations:
        if message.lower().find(place) != -1:
            return respond_location(place)


def respond_location(city):
    next_prompt = " Let's see if we have anything in common. Type the names of the following foods that you like. " \
                     "Peanut butter, chocolate, and sweet potato. Separate them with commas and a space. " \
                     "If you like none, type 'none'?"
    if city == "tel aviv":
        return "Really?! Great city. " + get_weather(city) + next_prompt
    elif city == "kansas city":
        return "No way! I grew up there. " + get_weather(city) + next_prompt
    elif city == "chicago":
        return "The windy city. I lived there for a long time. " + get_weather(city) + next_prompt
    elif city == "new york":
        return "There's no other place like NYC. " + get_weather(city) + next_prompt
    else:
        return "Shoot." + next_prompt


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
        return "Shoot. I guess we don't have that in common. Type 'boto info' to learn what I can do."
    else:
        return f"Alright! I also like {string}. Type 'boto info' to learn more about what I can do."


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


def check_weather(message):
    if message.lower().startswith("weather"):
        return get_weather(message[9:])


def get_weather(city):
    api_key = config.api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        return f"The weather in {city}: {x['weather'][0]['main']}, {x['weather'][0]['description']}" \
               f" with a temperature of {x['main']['temp']} K that feels like {x['main']['feels_like']} K and " \
               f"humidity of {x['main']['humidity']}%."
    else:
        return "Having technical difficulties. Please try again later."


def check_boto(message):
    if message.lower().startswith("boto info"):
        return get_boto_info(message)


def get_boto_info(message):
    return "I can do the following: " \
           "(1) return the maximum of two or three numbers - enter the numbers separated by a comma and space " \
           "(2) translate into robber's language - type 'robber's language' followed by what you want translated " \
           "(3) reverse - type 'reverse' followed by what you want reversed " \
           "(4) check for palindromes - type 'palindrome' followed by what you want checked " \
           "(5) check whether a letter is a vowel - type one letter " \
           "(6) get weather - type 'weather' and then the city " \
           "(7) respond to a hello, hi, shalom, or hola " \
           "(8) know whether someone asked a question or ended their input with an ! or a period " \
           "(9) detect certain curse words "


def select_animation(message):
    images_array = ["afraid", "bored", "confused", "crying", "dancing", "dog", "excited", "giggling", "heartbroke",
                    "inlove", "laughing", "money", "no", "ok", "takeoff", "waiting"]
    if message.lower().find("peanut butter") != -1:
        chosen_animation = "inlove"
    elif message.lower().find("chocolate") != -1:
        chosen_animation = "takeoff"
    elif message.lower().find("sweet potato") != -1:
        chosen_animation = "money"
    elif message.lower().find("kansas city") != -1:
        chosen_animation = "excited"
    elif message.lower().find("tel aviv") != -1:
        chosen_animation = "dancing"
    elif message.lower().find("chicago") != -1:
        chosen_animation = "heartbroke"
    elif message.lower().find("new york") != -1:
        chosen_animation = "giggling"
    elif message.lower().find("robber's language") != -1:
        chosen_animation = "waiting"
    elif message.lower().find("reverse") != -1:
        chosen_animation = "no"
    elif message.lower().find("palindrome") != -1:
        chosen_animation = "ok"
    elif message.lower().find("hello") != -1:
        chosen_animation = "dog"
    elif message.find("?") != -1:
        chosen_animation = "confused"
    elif message.find("!") != -1:
        chosen_animation = "crying"
    elif message.find(".") != -1:
        chosen_animation = "laughing"
    elif message.find("nope") != -1:
        chosen_animation = "bored"
    elif message.find("none") != -1:
        chosen_animation = "afraid"
    else:
        i = random.randint(0, len(images_array) - 1)
        chosen_animation = images_array[i]
    return chosen_animation
