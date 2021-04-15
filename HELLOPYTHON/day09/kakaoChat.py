#!/usr/bin/env python

#-*-coding: utf-8-*-



import os

from flask import Flask, request, jsonify



app = Flask(__name__)



@app.route('/keyboard')

def Keyboard():



    contents = {

        "type"     : "buttons",

        "buttons" : [ "살아있어" ]

    }



    return jsonify( contents )





if __name__ == "__main__":

    app.run( host = '0.0.0.0', port = 7000 )



