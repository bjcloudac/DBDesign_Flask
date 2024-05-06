"""
This module designs and implement a simple static database to be used by Flask application.
"""

stores = {}  # "Halifax", "Toronto", "London" to be added with auto generated uuid

items = {}

# {"book_name": "Harry Potter", "Lease period in days": 20},
#
# {"book_name": "Python 3.11", "Lease period in days": 15},
#
# {"book_name": "Physics & AI ", "Lease period in days": 45}
