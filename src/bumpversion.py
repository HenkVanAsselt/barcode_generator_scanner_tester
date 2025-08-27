# file: bumpversion.py

"""bumpversion.py

Read the file buildinfo.txt

The contents should look like

[DEFAULT]
name = Auto_Code128_Barcode Generator
version = 0.51.0001
date = 20190302 09:37:40

Bump the build version number with 1, 0-padded and write a new build date.

For example

[DEFAULT]
name = Auto_Code128_Barcode Generator
version = 0.51.0002
date = 201900302 09:40:32

"""

# Global imports
import os
import configparser
import datetime

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------
if __name__ == "__main__":

    filename = "buildinfo.txt"

    config = configparser.ConfigParser()
    config.read(filename)

    # Bump the minor version number with 1, 0-padded, so for example .01 becomes .02
    version = config["DEFAULT"]["version"]
    print(f"Current version = {version}")
    major_str, minor_str, build_str = version.split(".")
    build = int(build_str)
    new_version = f"{major_str}.{minor_str}.{build+1:04}"
    print(f"New version = {new_version}")
    config["DEFAULT"]["version"] = new_version
    # print(config['DEFAULT']['version'])

    # Write the new date string
    datestr = datetime.datetime.today().strftime("%Y%m%d")
    print(f"New date: {datestr}")
    config["DEFAULT"]["date"] = datestr

    with open(filename, "w") as configfile:
        config.write(configfile)
        print(f"{filename} has been updated")

    filename = "version_to_env.cmd"
    with open(filename, "w") as cmdfile:
        cmdfile.write(f"set EXE_version={new_version}\n")
        cmdfile.write(f"set EXE_date={datestr}\n")
        print(f"{filename} has been updated")


