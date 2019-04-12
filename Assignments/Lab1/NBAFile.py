nba_tuple = [('Atlanta', 13933, '$20.06'),
            ('Los Angeles', 14539, '$50.16'),
            ('Milwaukee', 12098, '$23.43')]

for i in nba_tuple:
    print('The attendance at %s was %d and the ticket price was %s' % (i[0], i[1], i[2]))