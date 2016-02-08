import os
from smooch import Smooch, Device

app_token = os.environ['SMOOCH_APP_TOKEN']

device = Device(id='7e6eedd677eb3ede0c636fc4c5b51a14')
app_user = Smooch(app_token=app_token).init(device)
print(app_user)

conv = app_user.get_conversation()
print(conv)
