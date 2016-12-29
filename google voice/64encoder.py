#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	THIS RETURNS BASE64 OF THE AUDIO FILE"""

import base64
import json

def encode_audio(audio):
  audio_content = audio.read()
  return base64.b64encode(audio_content)

f = open('20160425_64.mp3', 'r+')
f2 = open("20160425_encode.json", 'w')

json.dumps(f)