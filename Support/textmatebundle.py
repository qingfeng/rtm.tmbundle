#!/usr/bin/env python
# encoding: utf-8
"""
Created by QingFeng on 2008-08-28.
Copyright (c) 2008 QingFeng. All rights reserved.
"""

__author__ = 'Qing Feng <paradise.qingfeng@gmail.com>'
from rtm import createRTM
from string import Template

API_KEY = "4a2ce417fc9ea4ea5e2caeb137625e3e"
SECRET = "188b0622533f7fc8"

def item_html(*args):
    s='''
    <tr>
    <td>%s</td><td>%s</td><td>%s</td>
    </tr>
    '''%args
    return s

def getTasks(rtm):
    for t in rtm.tasks.getList().tasks.list:
        try:
            for tt in t.taskseries:
                if tt.task.completed=="":
                    name=eval("u'%s'"%tt.name)
                    # print name,tt.task.has_due_time,tt.task.priority
                    yield (name.encode("utf8"),tt.task.has_due_time,tt.task.priority)
        except AttributeError:
            pass
def main():
    rtm = createRTM(API_KEY, SECRET ,"e2a5a534409b85f87d8767616f7340bebaf86676")
    # print "\n".join([eval("u'%s'"%mylist.name) for mylist in rtm.lists.getList().lists.list])
    print """
    <table>
    <tr>
    <td>Task</td><td>Has due time</td><td>priority</td>
    </tr>
    """
    for task in getTasks(rtm):
        print item_html(*task)
    print "</table>"
if __name__ == '__main__':
    main()