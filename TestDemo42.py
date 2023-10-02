from ortools.sat.python import cp_model


# pylint: disable=too-many-statements
def solve_zebra():
    """Solves the zebra problem."""

    # Create the model.
    model = cp_model.CpModel()

    red = model.NewIntVar(1, 5, 'red')
    green = model.NewIntVar(1, 5, 'green')
    yellow = model.NewIntVar(1, 5, 'yellow')
    blue = model.NewIntVar(1, 5, 'blue')
    ivory = model.NewIntVar(1, 5, 'ivory')

    englishman = model.NewIntVar(1, 5, 'englishman')
    spaniard = model.NewIntVar(1, 5, 'spaniard')
    japanese = model.NewIntVar(1, 5, 'japanese')
    ukrainian = model.NewIntVar(1, 5, 'ukrainian')
    norwegian = model.NewIntVar(1, 5, 'norwegian')

    dog = model.NewIntVar(1, 5, 'dog')
    snails = model.NewIntVar(1, 5, 'snails')
    fox = model.NewIntVar(1, 5, 'fox')
    zebra = model.NewIntVar(1, 5, 'zebra')
    horse = model.NewIntVar(1, 5, 'horse')

    tea = model.NewIntVar(1, 5, 'tea')
    coffee = model.NewIntVar(1, 5, 'coffee')
    water = model.NewIntVar(1, 5, 'water')
    milk = model.NewIntVar(1, 5, 'milk')
    fruit_juice = model.NewIntVar(1, 5, 'fruit juice')

    old_gold = model.NewIntVar(1, 5, 'old gold')
    kools = model.NewIntVar(1, 5, 'kools')
    chesterfields = model.NewIntVar(1, 5, 'chesterfields')
    lucky_strike = model.NewIntVar(1, 5, 'lucky strike')
    parliaments = model.NewIntVar(1, 5, 'parliaments')

    model.AddAllDifferent(red, green, yellow, blue, ivory)
    model.AddAllDifferent(englishman, spaniard, japanese, ukrainian, norwegian)
    model.AddAllDifferent(dog, snails, fox, zebra, horse)
    model.AddAllDifferent(tea, coffee, water, milk, fruit_juice)
    model.AddAllDifferent(parliaments, kools, chesterfields, lucky_strike,
                          old_gold)

    model.Add(englishman == red)
    model.Add(spaniard == dog)
    model.Add(coffee == green)
    model.Add(ukrainian == tea)
    model.Add(green == ivory + 1)
    model.Add(old_gold == snails)
    model.Add(kools == yellow)
    model.Add(milk == 3)
    model.Add(norwegian == 1)

    diff_fox_chesterfields = model.NewIntVar(-4, 4, 'diff_fox_chesterfields')
    model.Add(diff_fox_chesterfields == fox - chesterfields)
    model.AddAbsEquality(1, diff_fox_chesterfields)

    diff_horse_kools = model.NewIntVar(-4, 4, 'diff_horse_kools')
    model.Add(diff_horse_kools == horse - kools)
    model.AddAbsEquality(1, diff_horse_kools)

    model.Add(lucky_strike == fruit_juice)
    model.Add(japanese == parliaments)

    diff_norwegian_blue = model.NewIntVar(-4, 4, 'diff_norwegian_blue')
    model.Add(diff_norwegian_blue == norwegian - blue)
    model.AddAbsEquality(1, diff_norwegian_blue)

    # Solve and print out the solution.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        people = [englishman, spaniard, japanese, ukrainian, norwegian]
        water_drinker = [
            p for p in people if solver.Value(p) == solver.Value(water)
        ][0]
        zebra_owner = [
            p for p in people if solver.Value(p) == solver.Value(zebra)
        ][0]
        print('The', water_drinker.Name(), 'drinks water.')
        print('The', zebra_owner.Name(), 'owns the zebra.')
    else:
        print('No solutions to the zebra problem, this is unusual!')


solve_zebra()