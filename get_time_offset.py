
import ntplib
c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org', version=3)
offset = response.offset

print("Time Offset: {}".format(offset))
