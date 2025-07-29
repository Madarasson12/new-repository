from datetime import datetime

with open('sammple.txt', 'w') as file:
    input_text = input("Enter some text to write to the file: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{input_text} ({current_time})\n")

    