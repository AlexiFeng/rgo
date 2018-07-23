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

basic=rgo_debug("layout")
btn1=rgo_component_debug(1,"btn1","button")
btn2=rgo_component_debug(2,"btn2","button")
basic.add(btn1)
basic.add(btn2)
print(basic.value)

