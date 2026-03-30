from flask import Blueprint, jsonify
import os
import platform
import psutil

operative_bp = Blueprint('operative', __name__)
sistem_info = {
  'os': os.name,
  'platform': platform.system(),
  'processor': platform.processor(),
  'ram': str(psutil.virtual_memory().total / (1024.0 ** 3)) + ' GB'  # Convert to GB
}

@operative_bp.route('/operative', methods=['GET'])
def get_operative():
    return jsonify({'system_info': sistem_info})
