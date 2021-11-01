def sample_response(input_text):
    user_message=str(input_text).lower()
    if user_message in ("hello","hi"):
        return "Hey! Hello"
    if user_message in ("who are you?","who are you"):
        return "I am an BOT created By Ramalingasamy M K (Security Researcher)"
    if user_message in ("creator?"):
        return "Ramalingsamy M K"
