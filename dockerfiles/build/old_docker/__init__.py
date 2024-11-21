import io
import sys
import os
import json
from contextlib import redirect_stdout
import shutil
#shutil.copy("/app_code", "/home/app_code")
print("here 2")

# Execute on docker container initialize
if __name__ == "__main__":
    print("here 3")
    # (1) Load in user_inputs json
    with open(f"/user_inputs.json", "r") as user_inputs_file:
        user_inputs = json.loads(user_inputs_file.read())
    os.remove(f"/user_inputs.json")  # Remove for privacy

    # (2) Execute user's main() function
    response = {}
    stdout = io.StringIO()

    # (2.1) Redirect stdout
    with redirect_stdout(stdout):
        try:
            # # (2.2) Run main() with user_inputs
            # current_directory = os.getcwd()
            # # Print the current working directory
            # print(f"Current working directory: {current_directory}")
            # for item in os.listdir(current_directory):
            #     item_path = os.path.join(current_directory, item)
            #     if os.path.isdir(item_path):
            #         print(f"Directory: {item}")
            #     else:
            #         print(f"File: {item}")
            shutil.copy("/app_code.py", "/home/app_code.py")
            import app_code  # import app_code.py

            #response["outputs"] = {"current_directory" : current_directory, "listdir" : os.listdir('/')}

            response["outputs"] = app_code.main(user_inputs)

        except Exception as e:
            # (2.3) Print traceback on error
            import traceback

            response["error"] = traceback.format_exc()

    response["stdout"] = stdout.getvalue()

    # (3) Write output as json file
    def set_default(obj):
        import numpy as np
        import pandas as pd

        if isinstance(obj, (set, pd.core.series.Series, np.ndarray)):
            return list(obj)  # convert list
        else:
            try:
                return str(obj)  # As last resort, cast to string
            except Exception as e:
                raise TypeError

    with open(f"/app_outputs.json", "w") as outputs_file:
        outputs_file.write(json.dumps(response, default=set_default))
