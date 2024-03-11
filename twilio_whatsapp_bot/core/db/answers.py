#!/usr/bin/python

from twilio_whatsapp_bot.core.db.db import DB
from typing import Any


class Answers(DB):

    def __init__(self):
        pass

    def insert_data(self, datas: Any) -> Any:
        insert_params = []
        insert_values = []
        i = 0
        for key_ in datas:
            insert_params.append("question_" + str(i))
            insert_values.append("'" + datas[key_] + "'")
            i += 1

        sql = "INSERT INTO answers (" + ",".join(insert_params) + ") "
        sql += "VALUES (" + ",".join(insert_values) + ")"
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                self.connection.commit()
        except Exception as exception:
            print("Erreur lors de l'execution : ", exception)
        self.deconnect()
