def madlib():
    print("🎉 Welcome to the Ultimate Crazy Mad Libs Game! 🎉")
    print("Fill in the blanks below with your own wacky words!\n")

    name = input("👤 Give me a name: ")
    place = input("📍 Give me a  place: ")
    funny_adj = input("🤣 Give me a funny adjective (like smelly, bouncy): ")
    random_obj = input("📦 Name a totally random object: ")
    animal = input("🐾 Name an animal (real or made-up!): ")
    action_verb = input("🏃 Give me an action verb (like dance, scream): ")
    funny_exclamation = input("😲 Shout out a funny exclamation (like 'Yikes!', 'Boing!', 'Aaoooga!'): ")

    story = f"""
    🎭 Here comes your crazy Mad Libs story! 🎭

    One sunny day in {place}, a totally {funny_adj} creature named {name} woke up inside a giant {random_obj}.
    Confused and slightly sticky, {name} stepped outside only to be greeted by a breakdancing {animal}.

    "{funny_exclamation}!" yelled {name}, as the {animal} threw glitter into the air and began to {action_verb} like no one was watching.

    Suddenly, the sky turned purple, and a squad of flying toasters surrounded them shouting,
    "All hail the {funny_adj} {random_obj}!"

    {name} just blinked and said, "Well, that escalated quickly..."

    And they all {action_verb} into the sunset, leaving behind only a trail of marshmallows.

    🎉 The End... or is it? 🎉
    """

    print("\nHere is your 🤪 Totally Random Mad Libs Story:\n")
    print(story)


if __name__ == "__main__":
    madlib()