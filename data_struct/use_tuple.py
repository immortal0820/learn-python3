#!/usr/bin/env python3

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo is', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Numbers of animals in the new zoo is', len(new_zoo) - 1 + len(zoo))
