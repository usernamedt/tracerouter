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

            second_token = parts.pop(0)
            if second_token == 'ms':
                # process additional rtt
                hop.rtt = float(first_token)
                if len(parts) > 0 and parts[0].startswith('!'):
                    parts.pop(0)
            else:
                hop.name = first_token
                hop.ip_info = IpInfo(second_token[1:][:-1])
                hop.rtt = float(parts.pop(0))
                parts.pop(0)
                if len(parts) > 0 and parts[0].startswith('!'):
                    parts.pop(0)

            return hop

        except (IndexError, ValueError):
            return None
