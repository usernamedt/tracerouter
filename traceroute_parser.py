from ip_info import IpInfo
from traceroute_hop import Hop
from traceroute_result import TracerouteResult


class TracerouteParser:
    def parse_data(self, data):
        result = TracerouteResult()
        for line in data.splitlines():
            line = line.strip()
            if line == '':
                continue
            hop = self._parse_hop(line)
            result.hops.append(hop)
        return result

    @staticmethod
    def _parse_hop(line):
        try:
            parts = line.split()
            hop = Hop(parts.pop(0))
            first_token = parts.pop(0)
            if first_token == '*':
                return hop

            hop.name = first_token
            hop.ip_info = IpInfo(first_token)

            return hop

        except (IndexError, ValueError):
            return None
