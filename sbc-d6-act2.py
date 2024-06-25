ro = int(input("Rows: "))
col = int(input("Column: "))

row = 1
column = 1

while row <= ro:
    if row == 1 or row == ro:
        print('*' * ro)
    
    elif column == 1 or column == col:
        print('*' + ' ' * (col - 2) + '*')
    else:
        ...
    row += 1