def check_finished(c):
    finished = False
    for i in range(0, 9):
        for j in range(0, 9):
            if c[i][j].current_value > 10:
                finished = False
                break
            else:
                finished = True
    return finished


def check_validity(c):
    valid = False
    checked_set = []
    # checking row validity:
    for i in range(0, 9):
        for j in range(0, 9):
            checked_set.append(c[i][j].current_value)
        if len(checked_set) == len(set(checked_set)):
            valid = True
            # print("Passed ROW validity")
        else:
            valid = False
            # print("Failed ROW validity")
            return valid
            break
        checked_set.clear()
    # checking column validity:
    for i in range(0, 9):
        for j in range(0, 9):
            checked_set.append(c[j][i].current_value)
        if len(checked_set) == len(set(checked_set)):
            valid = True
            # print("Passed COLUMN validity")
        else:
            valid = False
            # print("Failed COLUMN validity")
            return valid
            break
        checked_set.clear()
    # checking square validity:
    for i in range(0, 3):
        for j in range(0, 3):
            checked_set.append(c[i * 3][j * 3].current_value)
            checked_set.append(c[i * 3][j * 3 + 1].current_value)
            checked_set.append(c[i * 3][j * 3 + 2].current_value)
            checked_set.append(c[i * 3 + 1][j * 3].current_value)
            checked_set.append(c[i * 3 + 1][j * 3 + 1].current_value)
            checked_set.append(c[i * 3 + 1][j * 3 + 2].current_value)
            checked_set.append(c[i * 3 + 2][j * 3].current_value)
            checked_set.append(c[i * 3 + 2][j * 3 + 1].current_value)
            checked_set.append(c[i * 3 + 2][j * 3 + 2].current_value)
            if len(checked_set) == len(set(checked_set)):
                valid = True
                # print("Passed SQUARE validity")
            else:
                valid = False
                # print("Failed SQUARE validity")
                return valid
                break
            checked_set.clear()
    return valid
