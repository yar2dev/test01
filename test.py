import pandas as pd
import numpy as np
import datetime

from pycbrf.toolbox import ExchangeRates
import yfinance as yf
import requests
import time
import urllib.request
import io
import smtplib
import sys
pd.options.mode.chained_assignment = None

text_set1 = set()
text_set2 = set()
