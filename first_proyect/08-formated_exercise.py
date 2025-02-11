def greet(name: str, age: int) -> str:
    formated_string = f'Hello, {name}! You are {age} years old'
    return formated_string
print(greet("Hamlet", 20))