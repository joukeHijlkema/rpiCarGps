#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - sam. févr. 15:45 2017
#   - Initial Version 1.0
#  =================================================
import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

data={}

while True:
    try:
        report = session.next()
        # print(report)
        if report['class'] == 'TPV':
            data.clear()
            for i in ['time','speed','lon','lat']:
                if hasattr(report, i):
                    eval("data['{1}']=report.{1}".format(i))
            print(data)

    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
    
