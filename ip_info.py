import ipaddress
import json

import requests


class IpInfo:
    IP_INFO_API = "http://ip-api.com/json"

    def __init__(self, address):
        self.address = ipaddress.IPv4Address(address)
        self.is_global = self.address.is_global
        self._data_fetched = False
        self.info = dict(
            **{'as': "-"},
            country="-",
            city="-",
            isp="-"
        )

    def __str__(self):
        return str(self.address)

    def _fetch_ip_data(self):
        self._data_fetched = True
        if not self.address.is_global:
            return
        api_response = requests.get(f"{self.IP_INFO_API}/{self.address}")
        response = json.loads(api_response.content)
        for key in response.keys():
            if key in self.info.keys():
                self.info[key] = response[key]

    def get_info(self):
        if not self._data_fetched:
            self._fetch_ip_data()
        return [str(self.address)] + list(self.info.values())
