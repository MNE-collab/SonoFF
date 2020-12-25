import sonoff
#import config

s = sonoff.Sonoff("mne@yaposarl.ma", "WAPwap124816", "eu")
devices = s.get_devices()
if devices:
    # We found a device, lets turn something on
    device_id = devices[0]['deviceid']
    print("deviceid:",device_id)
    s.switch('on', device_id, None)

# update config
api_region = s.get_api_region
user_apikey = s.get_user_apikey
bearer_token = s.get_bearer_token

print("api region: ",api_region)
print("user_apikey : ",user_apikey )