import sqlite3
import asyncio

import pandas
from singletonDecorator import singleton
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

"""
This class represents a DataBase that holds all the information about coins that founds by the program.
"""


@singleton
class CoinsTable:
    def __init__(self):
        # self.user_coins = pd.DataFrame([], columns=["Coin Name", "Invest", "First Value", 'Coins'])
        self.con = sqlite3.connect("./Resources/{}.sqlite".format('coins'), check_same_thread=False)
        self.cur = self.con.cursor()

    def add_coin(self, df: pd.DataFrame, name):
        return df.to_sql(name=str(name).lower(), con=self.con, if_exists='append')

    def delete_coin(self, chat_id, coin_id):
        exist_table = pandas.read_sql(sql='SELECT * FROM {}'.format(str(chat_id).lower()), con=self.con).copy()
        exist_table = exist_table.drop(labels=int(coin_id))
        self.cur.execute("DROP TABLE IF EXISTS {}".format(str(chat_id).lower()))
        e = exist_table.to_sql(name=chat_id, con=self.con, if_exists='append')
        return 1

    def get_coins(self, chat_id, coin_id):
        exist_table = pandas.read_sql(sql='SELECT * FROM {}'.format(str(chat_id).lower()), con=self.con)
        return exist_table.iloc[coin_id]

    def print_coins(self, name):
        """
        Prints the coins table.
        :return: None
        """
        # df = pd.read_sql("SELECT * FROM {}".format(chat_id), self.con)
        #pd.read_sql_table(table_name=str(chat_id), con=self.con,index_col=1)
        return pandas.read_sql(sql='SELECT * FROM {}'.format(str(name).lower()), con=self.con)

    # def export_coins(self, chat_id: str):
    #     df = self.user_coins
    #     df.to_sql("./Resources/coins.h5", chat_id, if_exists="replace")

    def close_connection(self):
        self.con.close()
