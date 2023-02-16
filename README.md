# **inet_4031_adduser_script**

### **Description:**
- "create-users.py" is a python script/code that will check for the precense of a "#" (Hashtag) at the start of the lines and skip it.
- "create-users.input" is a text file for the "create-users.py" python script that contains a list of users and their relevant configuration details.

### **Operation:**
- To run this code we need to have the create-users.py code access the create-users.input text file, in order to do that we can use one of the two following commands:
  1. One way to run or execute this code is to use the linux command: sudo ./create-users.py < create-users.input
  2. The other way to run or execute this code is to use this linux command: cat create-users.input | sudo ./create-users.py
