class TracerouteResult:
    def __init__(self):
        self.hops = []

    def get_table(self):
        table_rows = []
        table_header = ["#", "IP", "AS", "Country", "City", "ISP"]
        for hop in self.hops:
            if hop.is_failed_hop():
                continue
            table_rows.append(hop.get_hop_info())
        return table_rows, table_header
