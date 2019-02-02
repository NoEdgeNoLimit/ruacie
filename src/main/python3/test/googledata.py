#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Imports the Google Cloud client library
from google.cloud import datastore

# Instantiates a client
client = datastore.Client()

# The kind for the new entity
kind = 'Task'
# The name/ID for the new entity
id = 'sampletask1id'
# The Cloud Datastore key for the new entity
task_key = client.key(kind, id)

# Prepares the new entity
task = datastore.Entity(client.key('Task'))
task.update({
    'category': 'Personal',
    'done': False,
    'priority': 4,
    'descriptionii': 'Learn Cloud Datastore'
})
client.put(task)
print('Saved {}: {}'.format(task.key.id, task['descriptionii']))