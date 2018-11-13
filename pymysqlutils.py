import pymysql
import pymysql.cursors


conn = pymysql.connect(
    host="172.16.56.100",
    port=3918,
    user="siov",
    password="9dX@g6UV65r!8",
    db="bidongv2",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def query(conn, sql):
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rvs = cursor.fetchall()
        return rvs
    except Exception as err:
        print(err)
    finally:
        cursor.close()


def execute(conn, sql):
    try:
        with conn.cursor() as cursor:
            rv = cursor.execute(sql)
            return rv
    except Exception as err:
        print(err)
    finally:
        cursor.close()


def dump_user_agent():
    sql = "SELECT platform FROM bd_mac_history;"
    rvs = query(conn, sql)
    with open("user-agent.txt", "w") as writer:
        for r in rvs:
            ua = r["platform"].split("&&")[0] + "\n"
            writer.write(ua)


dump_user_agent()
