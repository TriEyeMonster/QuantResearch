#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
IG Markets REST API sample with Python
2015 FemtoTrader
"""

from trading_ig import IGService
from trading_ig.config import config
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Client(IGService):
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        super(Client, self).__init__(
            config.username, config.password, config.api_key, config.acc_type
        )

        # if you want to globally cache queries
        #ig_service = IGService(config.username, config.password, config.api_key, config.acc_type, session)
        self.create_session()

    def get_last_x_days_price(self, EPIC, RESULO, start_date, end_date):
        response = self.fetch_historical_prices_by_epic_and_date_range(EPIC, RESULO, start_date, end_date)
        return response['price']

