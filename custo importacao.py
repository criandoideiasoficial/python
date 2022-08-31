import requests
import pandas as pd
from datetime import datetime
import time

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao_dic = requisicao.json()

cotacao_colar = requisicao_dic["USDBRL"]["bid"]

print(f"cotação.{cotacao_colar}")
