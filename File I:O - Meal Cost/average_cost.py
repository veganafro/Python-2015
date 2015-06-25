#This program uses file I/O to tell users the cost of eating over a specified time.

cost_per_day = open('daily_meal_spending.txt', 'r')

line = cost_per_day.readline()

dictionary = {}

daily_total = 0

while len(line) != 0:
    line = line.strip()
    line = line.split(',')
    for index in range(len(line)):
        line[index] = line[index].lstrip('$')
        if line[index].isalpha() == False:
            daily_total += float(line[index])
    dictionary[line[0]] = daily_total / len(line[1:])
    daily_total = 0
    line = cost_per_day.readline()

answer = input('Enter (day), (a)ll or (q)uit\n>')

while answer != 'q':
    try:
        if answer == 'a':
            for key, value in dictionary.items():
                print("Average for %s: $%.2f" % (key, value))
        else:
            print("Average for %s: $%.2f" % (answer, dictionary[answer]))
    except KeyError:
        print("That's not a valid day")
    answer = input('Enter (day), (a)ll or (q)uit\n>')

cost_per_day.close()
