import matplotlib.pyplot as plt
import seaborn as sns

def plot_summary(df, column, output_file):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=column, y='best', data=df)
    plt.title(f'Summary of TB Cases by {column}')
    plt.savefig(output_file)
    