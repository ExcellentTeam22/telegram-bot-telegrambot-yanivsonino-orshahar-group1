import sqlite3

import pandas
from singletonDecorator import singleton

import pandas as pd

"""
This class represents a DataBase that holds all the information about coins that founds by the program.
"""


@singleton
class CoinsTable:
    def __init__(self):
        # self.user_coins = pd.DataFrame([], columns=["Coin Name", "Invest", "First Value", 'Coins'])
        self.con = sqlite3.connect("./Resources/{}.sqlite".format('coins'))

    def add_coin(self, df: pd.DataFrame, name):
        return df.to_sql(name=str(name).lower(), con=self.con, if_exists='append')

    def delete_coin(self, chat_id, coin_id):
        exist_table = pandas.read_sql_table(table_name=str(chat_id), con=self.con,index_col=coin_id)
        exist_table = exist_table.drop(index=coin_id)
        exist_table.to_sql(name=chat_id, con=self.con, if_exists='replace')

    def get_coins(self, chat_id, coin_id):
        exist_table = pandas.read_sql(sql=str(chat_id), con=self.con, index_col=chat_id)
        return exist_table.iloc[coin_id]

    def print_coins(self, name):
        """
        Prints the coins table.
        :return: None
        """
        # df = pd.read_sql("SELECT * FROM {}".format(chat_id), self.con)
        #pd.read_sql_table(table_name=str(chat_id), con=self.con,index_col=1)
        query = 'SELECT * FROM {}'.format(str(name).lower())
        exist_table = pandas.read_sql(sql=query, con=self.con)
        return exist_table

    # def export_coins(self, chat_id: str):
    #     df = self.user_coins
    #     df.to_sql("./Resources/coins.h5", chat_id, if_exists="replace")

    def close_connection(self):
        self.con.close()
