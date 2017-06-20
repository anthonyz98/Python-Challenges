from random import randint # This is what helps me to create a random generator

class Die:

    def roll_die(self, number_of_sides):

        for number in range(10):

            random_number = randint(1, number_of_sides)

            if number < 10:
                print("The first few choices were: " + str(random_number))

            elif number == 10:
                print("The final choice is: " + str(random_number))

        return "The final choice is " + str(random_number)


roll_dice = Die().roll_die(20)

print(roll_dice)