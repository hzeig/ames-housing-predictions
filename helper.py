def fill_house_nan(col = None, val = None, col_lst = None, val_lst = None):
    '''
    Has 2 modes
    
    mode 1 takes in a column and a value and uses fillna on the column of housing
    
    mode 2 takes in a list of columns and a list of values to use and iterates through them.
    '''
    if col:
        housing[col] = housing[col].fillna(val)
    elif col_lst:
        for new_col, new_val in zip(col_lst, val_lst):
            housing[new_col] = housing[new_col].fillna(new_val)

def pickle_it(model, filename):
    ''' 
    Takes in a model and a file name and saves a pickel file of the model.
    Meant to clean the code a bit
    '''
    import pickle
    with open(filename, 'wb') as file:
        pickle.dump(model, file)