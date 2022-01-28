import pandas
import os
import logging
import schedule
import datetime
import time
from scrapping.scrapping_kabinet import get_kabinet
from scrapping.scrapping_dpr_mpr import get_dpr_mpr
from scrapping.scrapping_wagub import get_gub_wagub
from scrapping.scrapping_dprd_tk1 import get_dpr_tk1

import warnings
warnings.filterwarnings("ignore")


def job():
    print("Time... : ")
    print(datetime.datetime.now().time())
    print('Load Config... ')
    json_path = "./scrapping/config.json"
    scrp_kabinet = get_kabinet.load_config_json(json_path)
    scrp_dpr_mpr = get_dpr_mpr.load_config_json(json_path)
    scrp_gub = get_gub_wagub.load_config_json(json_path)
    scrp_dprd1 = get_dpr_tk1.load_config_json(json_path)

    print('Scrapping Data... ')
    scrp_kabinet.get_kabinet_data()
    scrp_dpr_mpr.get_dpr_data()
    scrp_dprd1.get_dprd1()
    scrp_gub.get_dataframe()


schedule.every(60).minutes.do(job)
# schedule.every(720).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute