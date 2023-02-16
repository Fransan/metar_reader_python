import requests
from xml.etree import ElementTree

from metar_reader_python.endpoints import Endpoint
from metar_reader_python.models.metar import Metar

endpoint = Endpoint(prefix=f"/v1/metar")

@endpoint.router.get("/{icao_code}")
def read_item(icao_code: str)->Metar:
    url:str = f"https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=metars&requesttype=retrieve&format=xml&hoursBeforeNow=1.25&stationString={icao_code}"

    r = requests.get(url)
    tree = ElementTree.fromstring(r.content)
    metar_station = tree[6][0][1].text
    metar_time = tree[6][0][2].text
    metar_raw = tree[6][0][0].text

    metar = Metar(
        station=metar_station,
        time=metar_time,
        raw_string=metar_raw
    )

    return metar
