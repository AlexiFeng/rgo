# -*- coding: UTF-8 -*-
import json
from rgo_layout_component import *
from rgo_utils import *
'''
Online(https)/OffLine(rpc)
Author:AlexiFeng
'''

'''
Online(Response)
{
    header:{
        type:"" =>DEBUG/TEST/FINAL
        version:"" =>0.0.1
        name:"layout"
    }
    data:{
        [{
            action:""=>add/del/alt/update
            target:""=>Button/Textview
            position:[]=>*********
            value:""
            }]
    }
}
'''
class rgo_debug:
    def __init__(self,type):
        self.header=setHeader("DEBUG","0.0.1",type)
        self.data=[]
    def add(self,obj):
        self.data.append(obj.value)
    @property
    def value(self):
        return{"header":self.header,"data":self.data}



