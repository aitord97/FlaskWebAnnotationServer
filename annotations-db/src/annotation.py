from uuid import uuid1

class Annotation :
    def __init__(self, options):
        self.attributes = options
        if 'id' not in self.attributes or self.attributes['id'] == "" :
            self.attributes['id'] = uuid1()
    def serialize(self):
        return self.attributes
    
annotations = {
    "annotations":[
        Annotation({"context": "hola", 'type': "Annotation", 'target':{'uri':"localhost//"}}).serialize(),
        Annotation({"context": "que", 'type': "Annotation", 'target':{'uri':"localhost//"}}).serialize(),
        Annotation({"context": "tal", 'type': "Annotation", 'target':{'uri':"localhost//"}}).serialize()
        ]

    }
