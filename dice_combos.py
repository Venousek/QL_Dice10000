class Has3():
    def __init__(self, n):
        self.num = n
    def __call__(self, dice_list):
        count = sum([1 if d == self.num else 0 for d in dice_list])
        if(count > 2):
            remaining = [d for d in dice_list if d != self.num] + ([self.num] * (count - 3))
            points = self.num * 100 if self.num != 1 else 1000
            return (points, remaining)
        return None

class Has4():
    def __init__(self, n):
        self.num = n
    def __call__(self, dice_list):
        count = sum([1 if d == self.num else 0 for d in dice_list])
        if(count > 3):
            remaining = [d for d in dice_list if d != self.num] + ([self.num] * (count - 4))
            points = self.num * 200 if self.num != 1 else 2000
            return (points, remaining)
        return None

class Has5():
    def __init__(self, n):
        self.num = n
    def __call__(self, dice_list):
        count = sum([1 if d == self.num else 0 for d in dice_list])
        if(count > 4):
            remaining = [d for d in dice_list if d != self.num] + ([self.num] * (count - 5))
            points = self.num * 400 if self.num != 1 else 4000
            return (points, remaining)
        return None

class Has6():
    def __init__(self, n):
        self.num = n
    def __call__(self, dice_list):
        count = sum([1 if d == self.num else 0 for d in dice_list])
        if(count > 5):
            remaining = []
            points = self.num * 800 if self.num != 1 else 8000
            return (points, remaining)
        return None

class HasM_Ns():
    def __init__(self, m, n):
        self.points = (n*10 if n != 1 else 100) * m
        self.countGoal = m
        self.num = n
    def __call__(self, dice_list):
        count = 0
        remaining = []
        for dice in dice_list:
            if(dice == self.num and count < self.countGoal):
                count+=1
            else:
                remaining.append(dice)
        
        if(count == self.countGoal):
            return (self.points, remaining)

        return None

def has3Pairs(dice_list):
    counts = [0]*6
    for di in dice_list:
        counts[di-1] += 1
    pairs = sum([1 for count in counts if count == 2])
    if pairs == 3:
        return (1000, [])
    return None

def hasStraight(dice_list):
    return sorted(dice_list) == list(range(1, 7))