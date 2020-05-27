# Tracerouter

Super fancy tracerouter app.

This is an enriched version of traceroute - it fetches AS, country, city and ISP of each hop.  

Needs a traceroute installed. Should work OOB on Linux/MacOS. Tested on Python 3.7 / MacOS 10.15.

# Usage

Specify a target - IP or domain name

    traceroute.py [-h] [-w W] [-m M] target

optional arguments:
  -h, --help  show this help message and exit
  -w W        Option used to specify the amount of time (in seconds) that
              traceroute will wait for an ICMP response message. The allowed
              range for wait_time is 1 to 300 seconds; the default is 5
              seconds.
  -m M        Option used to specify the maximum TTL value for outgoing ICMP
              datagrams. The allowed range for max_ttl is 1 to 255; the
              default value is 30.

# Launch sample

Install requirements

    python -m pip install -r requirements.txt

Launch and enjoy...

    python traceroute.py -w 10 -m 30 google.com
