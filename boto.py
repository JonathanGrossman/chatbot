from bottle import request, route, run, static_file, template
import json


def check_starts_with(user_input):
    if user_input.startswith("Hello"):
        return "Hello. "
    elif user_input.startswith("Hey"):
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
    boto_response = check_starts_with(user_message) + check_ends_with(user_message)
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
