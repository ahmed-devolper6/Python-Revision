def multiplication_table(start,end,end_mull):
    for x in range(start,end+1):
        print('_______________')
        print(f'{x}:multiplication_table')
        print('______________')
        for y in range(1,end_mull+1):
            print(f'{x} X {y} = {x*y}')


multiplication_table(1,10,8)

'''
i simple problem we want to create multiplication_table 
define i functions take 3 parmters
the start and end and multiplication_table end number
'''