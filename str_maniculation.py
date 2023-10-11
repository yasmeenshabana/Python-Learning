def str_maniculate(text):
    reverse=text[::-1]
    uppercase=reverse.upper()
    return uppercase

final_string=str_maniculate("Shabana Yasmeen")
print("String after maniculation is", final_string)