from bottle import request, route, run, static_file, template
import json


def check_for_cursing(message):
    curse_words = ["fuck", "shit", "bitch", "dick", "slut", "whore", "ass", "asshole"]
    for item in curse_words:
        if item in message:
            return "Please, no cursing. Try again. This time, keep it classy."
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
        response = "Great question. " + additional_response
        return response
    elif user_input.endswith("!"):
        response = "I'm excited too. " + additional_response
        return response
    elif user_input.endswith("."):
        response = "OK. Let me respond. " + additional_response
        return response
    else:
        return additional_response


def additional_processing(message):
    if "where" in message:
        return "where"
    else:
        counter = 0
        for item in message:
            counter += 1
        if counter == 1:
            return check_vowel(message)
        else:
            return f"Your message is {counter} characters."


def check_vowel(message):
    if message.lower() in ["a", "e", "i", "o", "u"]:
        return f"{message} is a vowel."
    elif message.lower() == "y":
        return f"Sometimes {message} is a vowel."
    else:
        return f"{message} is not a vowel."

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    boto_response = check_for_cursing(user_message)
    return json.dumps({"animation": "inlove", "msg": boto_response})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
