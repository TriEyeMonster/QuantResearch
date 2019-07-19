import datetime
from client.ig_client import Client


EPIC = 'CS.D.EURUSD.MINI.IP'
RESULO = 'H'
LAST_X_DAYS = 360
GET_DATA = True
ANALYSE = False

def main():
    client = Client()
    end = datetime.datetime\
        .utcnow()\
        .replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - datetime.timedelta(days=LAST_X_DAYS)
    name_str = EPIC.split('.')[2:4] + [RESULO, start.strftime('%y%m%d'), end.strftime('%y%m%d')]
    file_name = f'./data/{"_".join(name_str)}.csv'
    df = client.get_last_x_days_price(EPIC, RESULO, start, end)
    df.to_csv(file_name)


if __name__ == '__main__':
    main()