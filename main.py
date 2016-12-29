#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hmc5883
from time import sleep

if __name__ == "__main__":
    c = hmc5883.hmc5883()
    c.calibration()

    while 1:
        d  = c.get_bearing()
        print "Bearing: ", d
        sleep(1)
