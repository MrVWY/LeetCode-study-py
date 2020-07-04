import os
import subprocess
var = subprocess.call("wp export --dir=/tmp/ --user=Hayley --post_type=post --start_date=2020-06-01 "
                      "--end_date=2020-06-05")
