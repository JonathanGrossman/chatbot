from bottle import request, route, run, static_file, template
import json


def check_for_cursing(message):
    curse_words = ["fuck", "shit", "bitch", "dick", "slut", "whore", "ass", "asshole"]
    for item in curse_words:
        if item in message:
            return "Please, no cursing. Try again. This time, keep is classy."
        else:
            return check_type(message)


def check_type(message):
    type_check = message.split(", ")
    if type_check[0].isdigit() and type_check[1].isdigit():
        return return_max(type_check)
    else:
        check_start = check_starts_with(message)
        check_end = check_ends_with(message)
        return check_start + check_end


def return_max(numbers):
    first = int(numbers[0])
    second = int(numbers[1])
    print(first)
    print(second)
    if first > second:
        return second
    elif second > first:
        return second
    else:
        return first


def check_starts_with(current_response):
    words_array = current_response.split()
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
    if user_input.endswith("?"):
        response = "Great question."
        return response
    elif user_input.endswith("!"):
        response = "I'm excited too."
        return response
    elif user_input.endswith("."):
        response = "OK. Let me respond."
        return response
    else:
        return ""


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
