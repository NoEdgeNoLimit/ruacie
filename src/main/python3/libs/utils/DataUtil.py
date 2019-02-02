#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from google.cloud import datastore
import datetime
import time

# ===============基础数据区================start
base_table_name = 'Task'  # Task CollectUrlId
# key 等于url_id
base_table_row = {
    'use_status': 0,  # 0未使用 1已使用 2已完成
    'collect_num': 0,
    'collect_time': datetime.datetime.utcnow(),
    'update_time': datetime.datetime.utcnow()
}

# ===============基础数据区================end
# Instantiates a client
client = datastore.Client()


# 保存数据到数据库
def save_url_id_to_data(url_id):
    # 批量查询 查询到的采集+1
    task_list = []
    tasks = batch_lookup(url_id)
    for task in tasks:
        task_list.append(update_task(task))
        url_id.remove(task.key.id_or_name)
    for id in url_id:
        task_list.append(create_task(id))
    # 批量保存
    client.put_multi(task_list)


def batch_lookup(url_id: set):
    keys = []
    for id in url_id:
        keys.append(client.key(base_table_name, id))
    tasks = client.get_multi(keys)
    return tasks


def create_task(id):
    time.sleep(0.001)
    complete_key = client.key(base_table_name, id)
    task = datastore.Entity(key=complete_key)
    task.update(base_table_row)
    return task


def update_task(task):
    time.sleep(0.001)
    task['update_time'] = datetime.datetime.utcnow()
    task['collect_num'] = (task.get('collect_num') + 1 if (task.get('collect_num') != None) else 0)
    return task


def update_task_use(task):
    time.sleep(0.001)
    task['update_time'] = datetime.datetime.utcnow()
    task['use_status'] = 1
    return task


def get_url_id_by_data():
    query = client.query(kind=base_table_name)
    query.add_filter('use_status', '=', 0)
    query.order = ['-update_time']
    results = list(query.fetch(limit=10))
    # 立即设置状态 已使用
    task_list = []
    url_ids = set()
    for task in results:
        task_list.append(update_task_use(task))
    # 批量保存 已使用
    client.put_multi(task_list)
    for task in task_list:
        url_ids.add(task.key.id_or_name)
    return url_ids


if __name__ == "__main__":
    # save_url_id_to_data({5634472569470976, 56444065603911681})
    get_url_id_by_data()
