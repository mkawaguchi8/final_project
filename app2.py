import random

def omikuji():
    fortunes = [
        "Great fortune awaits you!",
        "Good luck is coming your way!",
        "Be cautious, bad luck is near.",
        "A surprise is waiting for you!",
        "Your hard work will pay off soon.",
        "Take care of your health.",
        "Unexpected visitors will bring you joy.",
        "Today is your lucky day!",
        "Stay positive and good things will happen.",
        "Be patient, good things take time."
    ]

    return random.choice(fortunes)

def main():
    print("Welcome to the Omikuji app!")
    print("Shake the virtual Omikuji box to receive your fortune.")

    while True:
        user_input = input("Shake the box? (y/n): ")

        if user_input.lower() == 'y':
            print("\nYour fortune: ", omikuji())
        elif user_input.lower() == 'n':
            print("Thank you for using the Omikuji app. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()
