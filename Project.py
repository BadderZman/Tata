import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from project1 import main

    main()

elif bit == '32bit':

    from project2 import main

    main()
