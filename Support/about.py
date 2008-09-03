from os import environ as env
import os
tm_dialog = env["DIALOG"]

# cmd = "%s ~/Desktop/Textmate_Test1.nib"%tm_dialog
cmd = '%s -p "%s" %s/nibs/SimpleNotificationWindow.nib' \
        %(tm_dialog,"",env['TM_SUPPORT_PATH'])
print cmd
os.system(cmd)

