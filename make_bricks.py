#   We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
#   Return True if it is possible to make the goal by choosing from the given bricks.


#make_bricks(3, 1, 8)  True
#make_bricks(3, 1, 9)  False
#make_bricks(3, 2, 10)  True

def make_bricks(small, big, goal):
    resultSmall = goal - small
    resultBig = goal%5
    if resultSmall < 1:
        return True
    else:
        if resultBig == 0:
            if big >= (goal/5):
                return True

    Bneeded = goal / 5
    Sneeded = goal % 5
    if big >= Bneeded:
        goal -= Bneeded*5
        if small >= Sneeded:
            if goal - small < 1:
                return True
    else:
        goal -= big*5
        Sneeded += ((Bneeded - big)*5)
        if small >= Sneeded:
            if goal - small < 1:
                return True

    return False

print make_bricks(3, 1, 8)
print make_bricks(3, 1, 9)
print make_bricks(3,2,10)
print make_bricks(6, 1, 11)
print make_bricks(43, 1, 46)


