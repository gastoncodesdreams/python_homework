
##################TASK 1
def hello():
    return "Hello!"

print(hello())

##################TASK 2
def greet(name):
    return f"Hello, {name.capitalize()}!"

print(greet("james")) 

##################TASK 3
def calc(x, y, operation="multiply"):
    try:
        if operation == "add":
            return x + y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y
        elif operation == "divide":
            return x / y
        elif operation == "modulo":
            return x % y
        elif operation == "int_divide":
            return x // y
        elif operation == "power":
            return x ** y
        else:
            return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    

print(calc(5, 6))  
print(calc(5, 6, "add"))  
print(calc(20, 5, "divide"))  

print(calc(14, 2.0, "multiply"))  
print(calc(12.6, 4.4, "subtract"))  

print(calc(9, 5, "modulo"))  
print(calc(10, 0, "divide"))  

##################TASK 4

def data_type_conversion(value, given_type):
    # int check
    if given_type == "int":
        try:
            # convert value to int
            return int(value)
        except:
            # if conversion fails
            return f"You can't convert {value} into a int."
    
    # float check
    elif given_type == "float":
        try:
            # convert value to float
            return float(value)
        except:
            # if conversion fails
            return f"You can't convert {value} into a float."
    
    # str check
    elif given_type == "str":
        try:
            # convert value to str
            return str(value)
        except:
            # if conversion fails
            return f"You can't convert {value} into a string."
    

print(data_type_conversion("110", "int")) 
print(data_type_conversion("5.5", "float"))  
print(data_type_conversion(7, "float")) 
print(data_type_conversion(91.1, "str"))  
print(data_type_conversion("banana", "int"))  


##################TASK 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    except ZeroDivisionError: 
        return "Invalid data was provided."
    
    
print(grade(75, 85, 95))  
print(grade("three", "blind", "mice")) 

##################TASK 6
def repeat(string, count):
    #empty string
    result = ""
    #loop count times
    for _ in range(count):
        result += string # add string to result
    return result

print(repeat("up,", 4)) 

##################TASK 7
def student_scores(parameter, **kwargs):
    if not kwargs:
        return "No students provided."
    
    if parameter == "best":
        #high score
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif parameter == "mean":
        #avg score
        average_score = sum(kwargs.values()) / len(kwargs)
        return average_score
    else:
        return "Invalid"
    

print(student_scores("mean", Tom=75, Dick=89, Angela=91)) 
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50)) 

##################TASK 8

def titleize(text):
    #little words not capitalized
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    
    #split input string
    words = text.split()
    
    #loop thru words to get index and word
    for i, word in enumerate(words):
        # capitalize first and last
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        #capitalize all words unless little word
        elif word.lower() not in little_words:
            words[i] = word.capitalize()
        # leave little
        else:
            words[i] = word.lower()
    
    #join words back
    return " ".join(words)

print(titleize("war And peace")) 
print(titleize("a separate peace"))  
print(titleize("after on"))  

#########################TASK 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter  #correct guess
        else:
            result += "_"  #underscore
    return result

print(hangman("difficulty", "ic")) 

##################################TASK 10
def pig_latin(text):
    vowels = "aeiou"
    result = []
    
    # split input 
    words = text.split()
    
    for word in words:
        # qu
        if word.startswith("qu"):
            pig_word = word[2:] + "quay"
        # qu as in "square"
        elif "qu" in word:
            qu_index = word.find("qu")
            pig_word = word[qu_index + 2:] + word[:qu_index + 2] + "ay"
        # words start with vowels
        elif word[0] in vowels:
            pig_word = word + "ay"
        # words start with consonants
        else:
            first_vowel_index = 0
            for i, char in enumerate(word):
                if char in vowels:
                    first_vowel_index = i
                    break
            pig_word = word[first_vowel_index:] + word[:first_vowel_index] + "ay"
        
        # add pig word to result
        result.append(pig_word)
    
    # join into single string
    return " ".join(result)

print(pig_latin("apple"))                # appleay
print(pig_latin("banana"))               # ananabay
print(pig_latin("cherry"))               # errychay
print(pig_latin("quiet"))                # ietquay
print(pig_latin("square"))               # aresquay
print(pig_latin("the quick brown fox"))  # ethay ickquay ownbray oxfay