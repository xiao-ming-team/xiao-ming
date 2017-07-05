# -*- coding: utf-8 -*-

import sqlite3

list_db_accounts_field = ('id', 'first_name', 'second_name')
list_db_history_field = ()
list_db_log_field = ()

class Patients(object):
    def __init__(self, file_path='data_patients.sqlite'):
        # connect the database file
        self._db = sqlite3.connect(file_path)

        # create cursor object for the database
        self._db_c = self._db.cursor()

        # account database table
        self._db_c.execute(
            'CREATE TABLE {table} ({fn0} {ft0} PRIMARY KEY, {fn1} {ft1}, {fn2} {ft2})'.format(
                table='accounts',
                fn0='id',
                ft0='INTEGER',
                fn1='first_name',
                ft1='TEXT',
                fn2='second_name',
                ft2='TEXT'
            )
        )

        # history database table
        self._db_c.execute(
            'CREATE TABLE {tn} ({fn0} {ft0}, {fn1} {ft1}, {fn2} {ft2})'.format(
                tn='history',
                fn0='time',
                ft0='INTEGER',
                fn1='account',
                ft1='TEXT',
                fn2='product',
                ft2='TEXT'
            )
        )


        self._db.commit()

    def create_account(self, **kwargs):
        self._db_c.execute(
            'INSERT INTO {tn} ({fn0}, {fn1}, {fn2}) VALUES ({fv0}, "{fv1}", "{fv2}")'.format(
                tn='accounts',
                fn0='id',
                fn1='first_name',
                fn2='second_name',
                fv0=kwargs['id'],
                fv1=kwargs['first_name'],
                fv2=kwargs['second_name']
            )
        )

        self._db.commit()

    def modify_account(self, **kwargs):
        pass

    def terminate(self):
        self._db.commit()
        self._db.close()

my_patients = Patients()
my_patients.create_account(**{'id': 11111, 'first_name': 'zaiyang', 'second_name': 'li'})
