class Hop(object):
    """
    A traceroute hop consists of a number of probes.
    """
    def __init__(self, idx):
        self.ip_info = None
        self.name = None
        self.rtt = None
        self.idx = int(idx)

    def is_failed_hop(self):
        return self.ip_info is None

    def get_hop_info(self):
        if self.is_failed_hop():
            return None
        return [self.idx] + self.ip_info.get_info()
