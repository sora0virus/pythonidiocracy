name = 'Bob'
age = 3000

if name == 'Alice':
    print ('Hi Alice')
elif age < 12: #false
    print ('You are not ALICE.')
elif age > 2000: #true
    print ('Unlike you, alice is not an immortal vampire.')
elif age > 100: #skipped because the age > 200 is true and rest is skipped
    print('You are not Alice, grannie.')