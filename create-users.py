#!/usr/bin/python2
import os
import re
import sys

def main():
    for line in sys.stdin:
        # Create a regex to match lines that start with #
        match = re.match(r'^\s*#', line)
        if match:
            continue

        # Split the line into an array using ':' as the separator
        fields = line.strip().split(':')

        # Check that there are 5 fields in the array
        if len(fields) != 5:
            continue

        # Extract the username, password, gecos, and groups from the fields
        username = fields[0]
        password = fields[1]
        gecos = " %s %s," % (fields[3], fields[2])
        groups = fields[4].split(',')

        # Create the user account
        print("===> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)

        # Set the user's password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)

        # Assign the user to the specified groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()
