import os
import datetime
# filename = os.path.dirname(__file__)
# tet = os.path.join(filename,"photo")
# if not os.path.exists(tet):
#     os.makedirs(tet)
# innter = os.path.join(tet + "/1.text")
# with open(innter,"w") as f:
#     f.write("1234567")
date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(type(date))

