def choose(prompt, options):
    while True:
        print(f"\n{prompt}")
        for number, option in enumerate(options, start=1):
            print(f"{number}. {option}")

        answer = input("> ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print(f"Please enter a number from 1 to {len(options)}.")


def play():
    print("THE TINY ADVENTURE")
    print("You wake up at the edge of a quiet forest.")

    path = choose("Where do you go?", ["Follow a forest path", "Walk toward a cave"])

    if path == 1:
        choice = choose("The path leads to a river. What do you do?", ["Cross the bridge", "Follow the river"])
        if choice == 1:
            print("\nYou cross safely and find a sunny village. You win!")
        else:
            print("\nYou follow the river to a cozy picnic spot. A lovely ending!")
    else:
        choice = choose("Inside the cave, you spot a sleeping dragon.", ["Sneak past", "Say hello"])
        if choice == 1:
            print("\nYou sneak by and discover a pile of treasure. You win!")
        else:
            print("\nThe dragon wakes up and offers you tea. Best friends forever!")


if __name__ == "__main__":
    play()
