#!/usr/bin/evn python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

DATA_PATH_ROOT = os.path.join(os.getcwd(),'data')
Product_File_Name = 'JData_Product.csv'
User_File_Name = 'JData_Product.csv'
Comment_File_Name = 'JData_Comment.csv'
Action_201602_File_Name = 'JData_Action_201602.csv'
Action_201603_File_Name = 'JData_Action_201603.csv'
Action_201603_extra_File_Name = 'JData_Action_201603_extra.csv'
Action_201604_File_Name = 'JData_Action_201604.csv'

def stitch_action():
    mon_2 = pd.read_csv(os.path.join(DATA_PATH_ROOT,Action_201602_File_Name))
    print mon_2.head()
    mon_3 = pd.read_csv(os.path.join(DATA_PATH_ROOT,Action_201603_File_Name))
    print mon_3.head()
    mon_3_add = pd.read_csv(os.path.join(DATA_PATH_ROOT,Action_201603_extra_File_Name))
    print mon_3_add.head()
    mon_4 = pd.read_csv(os.path.join(DATA_PATH_ROOT,Action_201604_File_Name))
    print mon_4.head()
    pieces = [mon_2,mon_3,mon_3_add,mon_4]

    all_action = pd.concat(pieces)

    all_action = pd.DataFrame(all_action)
    print all_action.shape

    all_action.to_csv(os.path.join(DATA_PATH_ROOT,'All_Action.csv'))

stitch_action()