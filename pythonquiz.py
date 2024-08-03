questions = [
    {
        "prompt": "This deep-sea creature has a bioluminescent lure dangling from its head to attract prey. What is it?",
        "options": ["A. Dumbo Octopus", "B. Anglerfish", "C. Giant Squid"],
        "answer": "B"
    },
    {
        "prompt": "Known for its translucent body and the ability to change color, this deep-sea dweller can camouflage itself effortlessly. What is it?",
        "options": ["A. Barreleye Fish", "B. Glass Squid", "C. Vampire Squid"],
        "answer": "B"
    },
    {
        "prompt": "This massive crustacean, often compared to a giant woodlouse, scavenges on the ocean floor. What is it?",
        "options": ["A. Giant Isopod", "B. Deep-Sea Dragonfish", "C. Goblin Shark"],
        "answer": "A"
    },
    {
        "prompt": "With its elongated, telescoping body and large, menacing teeth, this shark is a fearsome predator. What is it?",
        "options": ["A. Goblin Shark", "B. Frilled Shark", "C. Sixgill Shark"],
        "answer": "A"
    },
    {
        "prompt": "This deep-sea jellyfish has a unique bell-shaped body and long, trailing tentacles. What is it?",
        "options": ["A. Crown Jellyfish", "B. Atolla Jellyfish", "C. Moon Jellyfish"],
        "answer": "B"
    },
    {
        "prompt": "This deep-sea jellyfish is one of the rarest jellyfish on the planet, and resembles a firework. Whih one is it?",
        "options": ["A: Portugese Man o' War", "B. Black Sea Nettle Jellyfish", "C. Halitrephes Jellyfish"],
        "answer": "C"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:  # Access options in the current question
            print(option)
        answer = input("Enter answer A, B, or C:").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong.")
    print(f"You scored {score} out of {len(questions)}")

run_quiz(questions)
