import os
import sys
import logging
import sqlite3
from subprocess import check_output

logging.basicConfig(format='%(message)s')

logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

def find_all(name, path):
    paths = [os.path.join(root, name) for root, dirs, files in os.walk(path) if name in files]
    return paths


def delete_history_non_ie(browser_type, strings_to_be_deleted):
    # if strings_to_be_deleted in [[], [''], [""]]:
    # return 0

    if browser_type == 'chrome':
        table_name = 'urls'
        final_row = "str(row[1])+str(row[2])"
        paths = find_all('History', os.environ['LOCALAPPDATA']+'\Google\Chrome')
        # logger.info('Info:: 1:', paths)
    elif browser_type == 'firefox':
        table_name = 'Moz_places'
        final_row = "str(row[1])+str(row[12])"
        paths = find_all('places.sqlite', os.environ['APPDATA']+'\Mozilla\Firefox\Profiles')
        # logger.info('Info:: 2:', paths)
    elif browser_type == 'opera':
        table_name = 'urls'
        final_row = "str(row[1])+str(row[2])"
        paths = find_all('History', os.environ['APPDATA']+'\Opera Software')
        # logger.info('Info:: 3:', paths)
    elif browser_type == 'safari':
        table_name = 'history_items'
        final_row = "str(row[1])"
        paths = find_all('History', os.environ['APPDATA']+'\Apple Computer')
        # logger.info('Info:: 4:', paths)

    if paths == []:
        logger.info('Info:: Browser not found: '+browser_type)
        return

    for path in paths:
        result = True
        while result:
            result = False

            try:
                connection = sqlite3.connect(path, timeout=1)
                cursor = connection.cursor()
                try:
                    ids=[]

                    if browser_type == 'safari':
                        for row in cursor.execute("""SELECT * FROM history_visits"""):
                            # logger.info('Info:: row_v:', row)
                            temr = [row[0] for _ in strings_to_be_deleted if _ in row[3]]
                            if len(temr) > 0:
                                ids.append(temr)
                    else:
                        # logger.info('Info:: browser_type:', browser_type)
                        
                        for row in cursor.execute("""SELECT * FROM """+table_name):
                            # logger.info('Info:: row:', row)
                            temp = [row[0] for _ in strings_to_be_deleted if _ in eval(final_row)]
                            if len(temp) > 0:
                                ids.append(temp)
                    # logger.info(ids)
                    if len(ids) > 0:
                        # cursor.executemany('DELETE FROM '+table_name+' WHERE id=?', ids)
                        logger.info('Info:: Number of rows deleted is: '+str(len(ids))+' : '+browser_type)
                    connection.commit()
                except sqlite3.OperationalError:
                    logger.warning("Warning:: Database locked, please close: "+browser_type)

            finally:
                connection.close()
        
    return 0


def ie_clear():
    try:
        check_output("RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 1", shell=True)
        logger.info('Info:: IE cleared')
        return 0
    except:
        logger.warning('Warning:: IE not cleared')
        return 1


def delete_history(*args):
    strings_to_be_deleted = []
    args = list(args)
    # logger.info('Info:: args:', args)
    
    if len(args) == 0:
        argumentList = sys.argv
        argumentList = argumentList[1:]
        # logger.info('Info:: argumentList:', argumentList)
    
        if len(argumentList) > 0:
            strings_to_be_deleted.extend(argumentList)
        else:
            logger.info('Info:: No argument passed')
            return
    else:
        strings_to_be_deleted.extend(args)
        
    # strings_to_be_deleted = ['forward', 'KYwtivxpUx']
    _ = ' '
    for __ in strings_to_be_deleted:
        _ += __

    logger.info('Info:: String(s) to be deleted:'+_)
    logger.info('')

    for _ in ['chrome', 'firefox', 'opera', 'safari']:    
        delete_history_non_ie(_, strings_to_be_deleted)  
    # ie_clear()
    # logger.info('')


if __name__ == "__main__":
    delete_history('abd')
    # delete_history()
