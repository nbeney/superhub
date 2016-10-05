from collections import namedtuple

from superhub.utils.crypto import decode
from superhub.utils.password_vault import PasswordVault

Device = namedtuple("Device", ["name", "mac_address"])

enc_device_list = [
    Device(name='desktop-loft', mac_address=b'hmWhatNqlsxrbodvl5asYMU='),
    Device(name='laptop-blue', mac_address=b'uGWhbqZqmaJrbohvnWyslZo='),
    Device(name='laptop-toshiba', mac_address=b'uGWhmNNqnJ9rbLdvmJmsksQ='),
    Device(name='phone-keiko', mac_address=b'i2mhZqJqk89rmrlvl5asYJg='),
    Device(name='phone-maya', mac_address=b'iWWhl9dqxaBrbopvmJmsZ5k='),
    Device(name='phone-nana', mac_address=b'iW2hmKZql89rcblvl5msY5Q='),
    Device(name='phone-nicolas', mac_address=b'i5ihaNNqyJ5rbrZvmZesYMU='),
    Device(name='phone-sacha', mac_address=b'h2Whbapqk6BrmrZvmmesYcY='),
    Device(name='pi1', mac_address=b'tW2hZ6lqyM1rnrVvoGuslZc='),
    Device(name='pi2', mac_address=b'tW2hZ6lqyM1rcbRvmJesack='),
    Device(name='pi3', mac_address=b'tW2hZ6lqyM1rabhvy5askZg='),
    Device(name='kano', mac_address=b'g2WhmKNql5xraohvl2askZc='),
    Device(name='tablet-nexus', mac_address=b't22haqJqyKFrb4xvymysYMk='),
    Device(name='tablet-samsung', mac_address=b'hWWhmaVqnJtrnYxvzGWsZpc='),
    Device(name='tv', mac_address=b'tpihZ9Zqm85rmYlvmWqsZpg='),
]

key = PasswordVault().get()
device_list = [Device(_.name, decode(key, _.mac_address)) for _ in enc_device_list]

device_dict = {_.mac_address.upper(): _ for _ in device_list}

# Check there are no duplicates.
assert len(device_list) == len(device_dict)
