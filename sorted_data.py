from sys import argv

script, filename = argv

scores = {}

in_file = open(filename)

for line in in_file:
    input_list = line.strip().split(':')
    scores[input_list[0]] = input_list[1]

list_of_keys = scores.keys()
sorted_list_of_keys = sorted(list_of_keys)

for restaurant in sorted_list_of_keys:
    print 'Restaurant', restaurant, 'is rated at ', scores[restaurant], '.'

in_file.close()