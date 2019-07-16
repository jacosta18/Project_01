#Exersice 3

story = {
    'Hero': 'There was once a hero called Sparticus.',
    'beginning': 'His wife, Dany, was take from him by his soon to be king, Glactus.',
    'middle':"He formed an army of rebels, 3000 strong and marched towards the capital and fought outside the city's gates.",
    'End': 'Both Glactus and Sparticus fell on the battlefield, making Dany queen of the entire kingdom.',
    'Sub_End': "\U0001F602"
  }

print(story['Hero'])
print(story['beginning'])
print(story['middle'])
print(story['End'])
print(story['Sub_End'])

print()

story['Hero'] = 'There was once a LEGEND called Sparticus, ' \
                'He had a brother, Adam, who was taken as a hostage after winning one his hardest battles.'
print(story['Hero'])
story['beginning'] = 'Sparticus was a well-trained spy and warrior, he set out on secret mission with ten other men.'
print(story['beginning'])
story['middle'] = 'They climbed the mountains directing them towards the enemy fortress, where they found Adam dancing around a fire.'
print(story['middle'])
story['End'] = 'To be continued ...'
print(story['End'])
print(story['Sub_End'])

choose_hero = input('Would you like to change your hero?')
if (choose_hero.upper() == 'Y'):
    input('What would you like your Hero to be called?')
