responses = [
    "Hello, my name is robot",
    "What may I help you with?",
    "Thank you so much",
    "Bye-bye",
    "I don't know about this",
    "But next time surely I will do it for you"
]

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def end():
    print(responses[2])
    print(responses[3])

def extract_number(tokens):
    numbers = []
    for token in tokens:
        try:
            numbers.append(float(token))
        except ValueError:
            pass
    return numbers

def annu():
    print("Annu is a student of B.Tech")

operations = {
    "ADD": add,
    "ADDITION": add,
    "PLUS": add,
    "SUM": add,
    "MINUS": sub,
    "SUBTRACTION": sub,
    "MULTIPLY": mul,
    "DIVISION": div,
    "+": add
}

commands = {
    "ANNU": annu,
    "BYE": end,
    "BYE-BYE": end,
    "EXIT": end
}

# Main loop
print(responses[0])
while True:
    user_input = input("Enter your command: ").upper().split()
    if not user_input:
        continue

    # Check for command first
    command = user_input[0]
    if command in commands:
        commands[command]()
        if command in ["BYE", "BYE-BYE", "EXIT"]:
            break
        continue

    # Check for operations
    for word in user_input:
        if word in operations:
            numbers = extract_number(user_input)
            if len(numbers) >= 2:
                result = operations[word](numbers[0], numbers[1])
                print("Result:", result)
            else:
                print(responses[4])
            break
    else:
        print(responses[5])
