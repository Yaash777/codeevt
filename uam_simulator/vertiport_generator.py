#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:57:22 2021

@author: mrinmoy sarkar
"""

import numpy as np
import pandas as pd

class vertiport:
    def __init__(self, num_vertiport, leg_distance=34725, max_capacity=20):
        self.num_vertiport = num_vertiport
        self.leg_distance = leg_distance
        self.max_capacity = max_capacity
        self.vertiport_db = None

    def create_vertiports(self, desired_locations):
        vertiport_db = np.zeros((self.num_vertiport, 7))  # vertiport_id, x, y, z, takeoff_capacity, land_capacity, total_capacity
        takeoff_capacity = np.random.randint(1, self.max_capacity + 1, size=self.num_vertiport)
        land_capacity = np.random.randint(1, self.max_capacity + 1, size=self.num_vertiport)
        total_capacity = takeoff_capacity + land_capacity

        for i in range(self.num_vertiport):
            vertiport_id = i + 1
            xy = desired_locations[i]  # Use your desired coordinates here
            vertiport_db[i, :] = [vertiport_id, xy[0], xy[1], 0, takeoff_capacity[i], land_capacity[i], total_capacity[i]]

        self.vertiport_db = vertiport_db

    def save_vertiports(self):
        df = pd.DataFrame(data=self.vertiport_db, columns=['vertiport_id', 'x', 'y', 'z', 'takeoff_capacity', 'land_capacity', 'total_capacity'])
        df.to_csv("../config/vertiport_db.csv", index=False)


if __name__ == '__main__':
    # Example usage: Provide a list of desired coordinates
    desired_locations = [[1000, 2000], [3000, 4000], ...]
    vp = vertiport(len(desired_locations))
    vp.create_vertiports(desired_locations)
    vp.save_vertiports()