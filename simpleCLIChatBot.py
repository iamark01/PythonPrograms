print("Welcome to Simple Command-line Chatbot")

def extract_from_text(text):
    l = []
    for t in text.split(' '):
         try:
              l.append(float(t))
         except ValueError:
              pass
    return l

def add(a, b):
    return a + b

def sub(a, b):
    if b > a:
        result = b - a
    else:
        result = a - b
    return result

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def endChat():
    print("Thank you for using our services!!")
    exit()

def sorry():
     print("It's okay, I can understand")

def others():
     print("I didn't understand, could you please elaborate or refine your question")

def startAgain():
    print("You are welcome")
    start()

def start():
    while True:
        text = input("Hello user, how may I help you?\n")
        for word in text.strip().split(' '):
            if word.upper() in operations.keys():
                try:
                    l = extract_from_text(text)
                    r = operations[word.upper()] (l[0],l[1])
                    print(f"Here you go!\nYour answer is {r}")
                except:
                    print('Oops!! Something went wrong please enter again')
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
        else:
            others()

if __name__ == '__main__':

    operations = {'ADD':add, 'PLUS':add, 'SUM':add, 'ADDITION':add,
              'MINUS':sub, 'SUB':sub, 'SUBTRACT':sub, 'SUBTRACTION':sub,'DIFFERENCE':sub,
              'DIVISION':divide, 'DIVIDE':divide, 
              'PRODUCT':multiply, 'MULTIPLICATION':multiply, 'MULTIPLY':multiply}

    commands = {'EXIT':endChat, 'END':endChat,'CLOSE':endChat,'BYE':endChat,'BBYE':endChat,
            'THANKS':startAgain,'THANK':startAgain,'SORRY':sorry,'OOPS':sorry, 'BAD':sorry}
    start()