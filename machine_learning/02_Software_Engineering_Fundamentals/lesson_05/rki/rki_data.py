
import pandas as pd
import requests
from pathlib import Path
from datetime import datetime

class RKI():
    """Main RKI Class, provides DataFrame."""

    def __init__(self, file_url='https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv'):
        """Init RKI Class, default csv given by arcgis."""

        if file_url[:4] == 'http':
            r = requests.get(file_url, allow_redirects=True)
            content = r.content
        else:
            content = file_url

        def dateparser(X):
            """Parse RKI CSV date formats (there a two different ones)."""

            try:
                parsed = [datetime.strptime(x, '%d.%m.%Y, %H:%M Uhr') for x in X]
            except ValueError:
                parsed = [datetime.strptime(x, "%Y/%m/%d %H:%M:%S") for x in X]

            return parsed

        rki = pd.read_csv(content,
                        index_col=0,
                        parse_dates=[8, 10, 13],
                        date_parser=dateparser)
        self.df = rki
