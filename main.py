import pandas as pd
import matplotlib.pyplot as plt


def create_df():
    df = pd.read_csv("heart.csv")
    pd.set_option('display.max_columns', None)
    return df

def create_graph(df):
    for column_name in list(df.columns):
        unique_values_in_col = sorted(list(set(df[column_name])))
        fig, ax = plt.subplots()
        count_of_not_unique_values = []

        for unique_value in unique_values_in_col:
            count_of_not_unique_values.append(len(df[df[column_name] == unique_value]))

        ax.bar(unique_values_in_col, count_of_not_unique_values, color='red', edgecolor='white', label="avg salary", alpha=0.8)
        ax.legend(column_name)
        plt.savefig(f'images/{column_name}.png', transparent=True)


def check_gipotis(df):
    num_of_people_older_than_50 = len(df[(df['age'] > 50) & (df['thal'] == 1)])
    num_of_people_yunger_than_50 = len(df[(df['age'] < 50) & (df['thal'] == 1)])
    if num_of_people_older_than_50>num_of_people_yunger_than_50:
        return True
    return False

def main():
    df = create_df()
    create_graph(df)
    print(check_gipotis(df))


if __name__=='__main__':
    #drop_tables()
    main()
    #print(get_config_args()['BOTOKEN'])
