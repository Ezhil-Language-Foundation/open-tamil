## -*- coding: utf-8 -*-
## (C) 2016 Muthiah Annamalai,

from flask import Flask

app = Flask(__name__)
from webspell import views
