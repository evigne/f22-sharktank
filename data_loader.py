import csv
import os
import sqlite3
from traceback import format_exc

def remove_charaters_from_number(value):
    return filter(lambda x: x.isdigit(), value)
def remove_characters(value):
    value = value.replace(',', '')
    value = value.replace('%', '')
    return value

if __name__ == '__main__':
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    try:
        c.execute(
        '''
        CREATE TABLE IF NOT EXISTS "stpdata_product" (
        "id" integer PRIMARY KEY, 
        "company" varchar(140) NOT NULL, 
        "industry" varchar(140) NOT NULL, 
        "entrepreneur_gender" varchar(140) NOT NULL, 
        "amount" integer NOT NULL, 
        "corcoran" bool NOT NULL, 
        "cuban" bool NOT NULL, 
        "deal" varchar(140) NOT NULL, 
        "episode" integer NOT NULL, 
        "equity" real NOT NULL, 
        "greiner" bool NOT NULL, 
        "guests" bool NOT NULL, 
        "harrington" bool NOT NULL, 
        "herjavec" bool NOT NULL, 
        "investPer_shark" integer NOT NULL, 
        "john" bool NOT NULL, 
        "no_of_sharks" integer NOT NULL, 
        "note" text NOT NULL, 
        "olary" bool NOT NULL, 
        "season" integer NOT NULL, 
        "valuation" integer NOT NULL)
        '''
        )
        with open(os.path.abspath('shark_tank_data.csv')) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                # c.execute("""
                # INSERT INTO stpdata_product VALUES("AVA","","")""")
                c.execute(
                    '''
                        INSERT INTO stpdata_product VALUES (
                            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                        )
                    ''',(
                        row['Row'],
                        row['Company'],
                        row['Industry'],
                        row['Entrepreneur Gender'],
                        remove_characters(row['Amount']),
                        row['Corcoran'],
                        row['Cuban'],
                        row['Deal'],
                        row['No. in series'],
                        remove_characters(row['Equity']),
                        row['Greiner'],
                        row['Guest'],
                        row['Harrington'],
                        row['Herjavec'],
                        remove_characters(row['per shark']),
                        row['John'],
                        row['Sharks'],
                        row['Details / Notes'],
                        row["O'Leary"],
                        row['Season'],
                        remove_characters(row['Valuation'])
                    )
                )
                conn.commit()


        conn.close()
    except Exception:
        print(format_exc())
        conn.close()
