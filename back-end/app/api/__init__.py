from flask import Blueprint

bp = Blueprint('api', __name__)

# д�������Ϊ�˷�ֹѭ�����룬ping.py�ļ�Ҳ�ᵼ�� bp
from app.api import ping