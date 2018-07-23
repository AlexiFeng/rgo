class rgo_component_debug:
    def __init__(self,id=0,value="",type="Button"):
        #Button/Textview
        self.value={
            "type":type,
            "id":id,
            "value":value,
            "height":-1, #-1 means auto
            "width":-1}
    def setId(self,id):
        self.value[id]=id
    def setValue(self,value):
        self.value[value]=value
    def setHeight(self,height):
        if int(height)>=-1:
          self.value[height]=height
    def setWidth(self,width):
        if int(width)>=-1:
          self.value[width]=width
    def setType(self,type):
        self.value[type]=type


