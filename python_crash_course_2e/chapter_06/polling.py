# polling.py

# favorite_languages.py

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'Ina':'R'
    }

print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# building a set
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

people = ['jen','James','Ina','Georgia','Betty','Bella','Laser']
for person in people:
    if person in favorite_languages.keys():
        print(f"\n{person.title()}, thank you for responding to the languages"\
        " poll.")
    else:
        print(f"\n{person.title()}, please complete this poll.")