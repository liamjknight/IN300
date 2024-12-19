# grade = int(input('Enter a score between 0 and 100: '))
#
# if 90 <= grade <= 100:
#     print('You got an A')
# elif 80 <= grade <= 89:
#     print('You got a B')
# elif 70 <= grade <= 79:
#     print('You got a C')
# elif 60 <= grade <= 69:
#     print('You got a D')
# elif 0 <= grade <= 59:
#     print('You got an F')
# else:
#     print('Incorrect Input')

# import sys
# while True:
#     print('1: SciFi')
#     print('2: Comp Tech')
#     print('3: Cooking')
#     print('4: Business')
#     print('5: Comics')
#     print('6: Exit')
#
#     category = int(input('Make a selection by entering an integer: '))
#
    # if category == 1:
    #     print('You chose SciFi')
    # elif category == 2:
    #     print('You chose Comp Tech')
    # elif category == 3:
    #     print('You chose Cooking')
    # elif category == 4:
    #     print('You chose Business')
    # elif category == 5:
    #     print('You chose Comics')
    # elif category == 6:
    #     print('You chose to Exit')
    #     sys.exit(0)
    # else:
    #     print('Incorrect Input')

input = int(input('Enter a Number: '))
inputDivided = int(input/2)

for i in range(1,input+1):
    print('\nOuter loop value: ', i)
    for j in range(1,inputDivided+1):
        print('\nInner loop value: ', j)