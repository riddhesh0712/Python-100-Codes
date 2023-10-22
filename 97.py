import string

def remove_punctuation(input_string):
    
    translator = str.maketrans("", "", string.punctuation)
    
    
    result_string = input_string.translate(translator)
    
    return result_string


input_string = "Hello, World! This is an example string."
result = remove_punctuation(input_string)
print(result)
