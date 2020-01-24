import sqlite3
import os
from subprocess import check_output

def find_all(name, path):
    paths = [os.path.join(root, name) for root, dirs, files in os.walk(path) if name in files]
    return paths


def delete_history(browser_type, strings_to_be_deleted):
    # if strings_to_be_deleted in [[], [''], [""]]:
    # return 0

    if browser_type == 'chrome':
        table_name = 'urls'
        final_row = "str(row[1])+str(row[2])"
        paths = find_all('History', os.environ['LOCALAPPDATA']+'\Google\Chrome')
    elif browser_type == 'firefox':
        table_name = 'Moz_places'
        final_row = "str(row[1])+str(row[12])"
        paths = find_all('places.sqlite', os.environ['APPDATA']+'\Mozilla\Firefox\Profiles')
    elif browser_type == 'opera':
        table_name = 'urls'
        final_row = "str(row[1])+str(row[2])"
        paths = find_all('History', os.environ['APPDATA']+'\Opera Software')
    elif browser_type == 'safari':
        table_name = 'history_items'
        final_row = "str(row[1])"
        paths = find_all('History', os.environ['APPDATA']+'\Apple Computer')

    if paths == []:
        print('Browser not found: '+browser_type)

    for path in paths:
        result = True
        while result:
            result = False
            connection = sqlite3.connect(path, timeout=1)
            cursor = connection.cursor()
            try:
                ids=[]
                for row in cursor.execute("""SELECT * FROM """+table_name):
                    # print('row:', row)
                    temp = [row[0] for _ in strings_to_be_deleted if _ in eval(final_row)]
                    if len(temp) > 0:
                        ids.append(temp)
                if browser_type == 'safari':
                    for row in cursor.execute("""SELECT * FROM history_visits"""):
                        # print('row_v:', row)
                        temr = [row[0] for _ in strings_to_be_deleted if _ in row[3]]
                        if len(temr) > 0:
                            ids.append(temr)
                try:
                    # cursor.executemany('DELETE FROM urls WHERE id=?', ids)
                    print('Number of rows deleted: '+str(len(ids))+' - '+browser_type)
                except:
                    print("Deletion error!")
                connection.commit()
            except sqlite3.OperationalError:
                print("Database locked, please close "+browser_type)

        connection.close()
        
    return 0


# [] means all
strings_to_be_deleted = ['google', 'wiki']
print('strings_to_be_deleted:', strings_to_be_deleted, '\n')


def ie_clear():
    try:
        check_output("RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 1", shell=True)
        return 0
    except:
        return 1


for _ in ['chrome', 'firefox', 'opera', 'safari']:
    delete_history(_, strings_to_be_deleted)
    print('IE cleared!')
    
ie_clear()

