#Program to Remove Punctuations From a String

def remove_punctuations(string):
    rp_string = ""
    for i in string:
        if i.isdigit() or i.isalpha() or i == " ":
            rp_string += i
        else:
            continue
    return rp_string

user_string = "Hi, this is a demo program!"

result = remove_punctuations(user_string)

print(result)
