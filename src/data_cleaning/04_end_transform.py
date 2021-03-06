import pandas as pd 

dfmatch = pd.read_csv(f"data/02transform_data/dataclear.csv",index_col=0) 
number_of_champ = 10

def get_total_sbire_by_champ(df,number_of_champ):
    """
    Add columns that count sbire kills of each players
    Parameters : df => Dataframe, number_of_champ => number of champions
    Return : Modified dataframe
    """
    for i in range(1,(number_of_champ + 1)):
        df[f'total_sbire_kill_{i}'] = df[f'sbireskill_{i}'] + df[f'jungsbirekill_{i}']
        df.drop([f'sbireskill_{i}',f'jungsbirekill_{i}'], axis=1)
    return df

def get_total_item_score_by_champ(df,number_of_champ):
    """
    Add columns that count the total item score of each players
    Parameters : df => Dataframe, number_of_champ => number of champions
    Return : Modified dataframe
    """
    for i in range(1,(number_of_champ +1 )):
        df[f'item_total_score_{i}'] = df[f'item1_{i}'] ** 2 + df[f'item2_{i}'] ** 2 + df[f'item3_{i}'] ** 2 + df[f'item4_{i}'] ** 2 + df[f'item5_{i}'] ** 2 + df[f'item6_{i}'] ** 2
        df.drop([f'item1_{i}',f'item2_{i}',f'item3_{i}',f'item4_{i}',f'item5_{i}',f'item6_{i}',], axis=1)
    return df

dfmatch = get_total_sbire_by_champ(dfmatch,number_of_champ)
dfmatch = get_total_item_score_by_champ(dfmatch,number_of_champ)

dfmatch.to_csv("data/03cleaned_data/cleaned_data.csv")