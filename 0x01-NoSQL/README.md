# 0x01. NoSQL

## Description
This project focuses on NoSQL databases, specifically MongoDB. It covers basic operations like creating databases, inserting documents, querying data, updating records, and deleting entries. The project also includes Python scripts that interact with MongoDB using the PyMongo driver.

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS
- MongoDB version 4.2
- Python 3.7
- PyMongo 3.10

## Files

### MongoDB Scripts
- `0-list_databases`: Lists all databases in MongoDB
- `1-use_or_create_database`: Creates or uses the database `my_db`
- `2-insert`: Inserts a document in the collection `school`
- `3-all`: Lists all documents in the collection `school`
- `4-match`: Lists all documents with name="Holberton school" in the collection `school`
- `5-count`: Displays the number of documents in the collection `school`
- `6-update`: Adds a new attribute to documents in the collection `school`
- `7-delete`: Deletes all documents with name="Holberton school" in the collection `school`

### Python Scripts
- `8-all.py`: Lists all documents in a collection
- `9-insert_school.py`: Inserts a new document in a collection based on kwargs
- `10-update_topics.py`: Changes all topics of a school document based on the name
- `11-schools_by_topic.py`: Returns the list of schools having a specific topic
- `12-log_stats.py`: Provides stats about Nginx logs stored in MongoDB

## Setup
1. Install MongoDB 4.2
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
Copy
2. Install PyMongo
$ pip3 install pymongo
Copy
## Usage
- To run MongoDB scripts:
$ cat script_name | mongo
Copy- To run Python scripts:
$ ./script_name.py
Copy
## Author
GIDEON HABWE

## Acknowledgments
- ALX Africa
- Holberton School
