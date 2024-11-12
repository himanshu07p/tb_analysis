def summarize_data(df):
    return df.describe()

def group_by_column(df, column):
    return df.groupby(column)['best'].describe()