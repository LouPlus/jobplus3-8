# -*- coding: utf-8 -*-

import os
import json
from random import randint
from faker import Faker
from simplejob.models import db, User, Company, Job

fake = Faker()

# 生成企业用户
def iter_users():
    yield Company(
            name = '测试账户',
            email = 'test@test.com',
            website = 'www.test.com',
            password = '123456',
            address = 'test'
            )

def iter_job():
    company = Job.query.filter_by(name = '测试账户').first()
    with open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'jobs.json')) as f:
        jobs = json.load(f)
    for job in jobs:
        yield Job(
                name = job['name'],
                salary = job['salary'],
                address = job['address']
                )

def run():
    for user in iter_users():
        db.session.add(user)

    for job in iter_job():
        db.session.add(job)

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
