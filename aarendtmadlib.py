#Amy Arendt

#madlib intro
print('Time to Sail the Seas! - A Pirate themed MadLib Generator')
print('')

#user input
pirate_name = input("Enter your pirate name: ")
secondmate = input("Enter the name of your second mate: ")
ship_name = input("Enter the name of your ship: ")
ocean = input("Enter an Ocean name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
past_verb = input("Enter a past tense verb: ")
fight = input("Enter a fighting move: ")
seamonster = input("Enter a type of sea animal: ")
treasure = input("Enter a type of treasure: ")
sound = input("Enter your pirate yell: ")
object1 = input("Enter an object: ")
adverb = input("Enter an adverb: ")
emotion = input("Enter an emotion: ")
action_verb = input("Enter an action verb: ")
booze = input("Enter a type of alcohol or drink: ")

#printing madlib
print('''
Ahoy, matey! %s stood proudly on the deck of the mighty ship, %s, sailing across the vast %s. 
Beside them, their loyal second mate, %s, adjusted their hat with a %s grin.

Suddenly, the sky turned %s, and a monstrous %s rose from the depths!

With a mighty %s, the crew prepared to %s that monster. %s bravely %s forward,
wielding a %s like a true sea legend.

After an intense battle, the monster retreated, leaving behind a chest full of %s.

The crew cheered %s, their hearts filled with %s.

That night, they %s in celebration, drinking barrels of %s, and toasting to another grand adventure!
'''
%(pirate_name, ship_name, ocean, secondmate, adjective1, adjective2, seamonster, sound, fight, pirate_name, past_verb, object1, treasure, adverb, emotion, action_verb, booze))
print('')
print('')
print('Press Enter to close.')
input('')
print('')
