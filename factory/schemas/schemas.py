'''
schemas for incoming and outgoing messages
more important for incoming (feed) - outcoming (stream) are not obligatory
'''


feed = {
    'source_app': {
        'required': True,
        'type': 'string'
    },
    'data':{
        'required':True,
        'type': 'string'
    }
}

stream = {
   'addressie_app' :{
       'required':True,
       'type': 'string'
   },
    'result': {
        'required':True,
        'type':'float'
    }
}
