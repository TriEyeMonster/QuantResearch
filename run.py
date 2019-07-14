import datetime
from client.ig_client import Client


EPIC = 'CS.D.EURUSD.MINI.IP'
RESULO = 'H'
LAST_X_DAYS = 365
GET_DATA = True
ANALYSE = False

def main():
    if GET_DATA:
        client = Client()
        end = datetime.datetime\
            .utcnow()\
            .replace(hour=0, minute=0, second=0, microsecond=0)
        start = end - datetime.timedelta(days=LAST_X_DAYS)
        df = client.get_last_x_days_price(EPIC, RESULO, start, end)
        pass
    else:
        an


if __name__ == '__main__':
    main()