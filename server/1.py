from rgo import *
from rgo_layout_component import *
from rgo_utils import *

basic=rgo_debug("layout")
btn1=rgo_component_debug(1,"btn1","button")
btn2=rgo_component_debug(2,"btn2","button")
basic.add(btn1)
basic.add(btn2)
rgo_send(basic.value)
