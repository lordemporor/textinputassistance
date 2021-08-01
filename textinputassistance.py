class TextAssistanceInfo:
    def __init__(self):
        self.version = "0.0.1"
        self.version_nickname = "Piotr"


def clarify(txt_in, rmv_txt=".!?"):
    for char in list(rmv_txt):
        txt_in = txt_in.replace(char, '')
    return str.lower(txt_in).strip()


def while_input(question, accepted_responses, clarifyBool=True, invalid_response="Entered input is not valid"):
    if clarifyBool:
        usr_in = clarify(input(question))
    else:
        usr_in = input(question)
    while usr_in not in accepted_responses:
        print(invalid_response)
        if clarifyBool:
            usr_in = clarify(input(question))
        else:
            usr_in = input(question)
