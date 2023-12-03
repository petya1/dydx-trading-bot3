from func_utils import get_ISO_times
from constants import RESOLUTION
import pandas as pd
import numpy as np
import time
from pprint import pprint

# Get relevant time periods
ISO_TIMES = get_ISO_times()

pprint(ISO_TIMES)

# Construct martket prices
def construct_market_prices(client):
    pass