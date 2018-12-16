#/usr/bin/python
import boto3
ec=boto.recource('ec2')
for list in ec.instance.al():
    print list.id, list.name

