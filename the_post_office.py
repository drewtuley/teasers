# After a local Post Office burglary, five suspects were being interviewed.
# Below is a summary of their statements.
# Police know that each of them told the truth in one of their statements and lied in the other.
# From this information can you tell who committed the crime?

Alan = 1
Brian = 2
Charles = 3
Derek = 4
Eric = 5

suspects = ['Alan', 'Brian', 'Charles', 'Derek', 'Eric']

statements = [
    # Brian said:
    (['!= Charles', '==Alan']),
    # Derek said:
    (['==Charles', '!= Alan']),
    # Charles said:
    (['==Brian', '!=Eric']),
    # Alan said:
    (['==Eric', '!=Brian']),
    # Eric said:
    (['==Derek', '==Alan'])

]
if __name__ == "__main__":
    # test each suspect against the statements
    for suspect in suspects:
        found_suspect = True
        for statement in statements:
            if eval(suspect + ' ' + statement[0]) == eval(suspect + ' ' + statement[1]):
                # both statements are True or False, either way its invalid for this suspect
                print('invalid statement - it wasn\'t {0}'.format(suspect))
                found_suspect = False
                break
        if found_suspect:
            print('***all statements are correct - so it was {0}***'.format(suspect))
