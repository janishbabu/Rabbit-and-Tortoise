import random
generate = str(random.randint(1000, 10000))
print(generate)
guess_number = (input('Guess Your  4 digit  number'))
guess_number = str(guess_number)

if len(guess_number) == 4:
    if generate == guess_number:
        print('congratulations,You are win')

    else:
        ctr = 0
        while guess_number != generate:
            ctr = ctr + 1
            count = 0
            rabbit = 0
            tortoise = 0
            guess_number = str(guess_number)
            correct_answer = []
            for i in range(0, 4):
                if guess_number[i] == generate[i]:
                    count = count + 1
                    rabbit = rabbit + 1
                    correct_answer.append(guess_number[i])
                elif guess_number[i] in generate:
                    tortoise = tortoise+1
                    correct_answer.append(guess_number[i])
                else:
                    continue

            print('count of rabbit is :', str(rabbit))
            print('count of tortoise is :', str(tortoise))
            print('\n')
            if (count < 4) and (count != 0):
                """rint('Rabbit count is:', str(rabbit))"""
                for k in correct_answer:
                    print(k, end='')
                print('\n')
                guess_number = int(input('Enter Your next choice'))
            elif count == 0:
                print('No match your input')
                print('\n')
                guess_number = int(input('Enter Your next choice'))

else:
    print('Invalid input')

