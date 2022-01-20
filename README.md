# redis-om-python-users-tasks

This is a basic demo showing one way you could model users that can be assigned tasks, and tasks that can have multiple users assigned to them.

## Getting Started

```bash
$ git clone https://github.com/simonprickett/redis-om-python-users-tasks.git
$ docker-compose up -d
$ python3 -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
$ python user_task_demo.py
```

Example output:

```bash
$ python user_task_demo.py
Saved user user1 as 01FSW9S4NBCRVJ9WRR6D1AB3TN.
Saved user user2 as 01FSW9S4NK9VMZQAGDQJSF7Q8C.
Saved user user3 as 01FSW9S4NMAFN8M5Y8K20ZP9Z4.
Saved task 12 as 01FSW9S4NQ01CSXQCRTAHAQMT7.
Saved task 19 as 01FSW9S4NR6G2WZDT56HYR9MAX.
Saved task 22 as 01FSW9S4NSFXDWVCE6C315JFC4.
Saved task 29 as 01FSW9S4NVGEFRGC6V37JV98TB.
Saved task 33 as 01FSW9S4NW59T8PR8M8HQ2XQDZ.
Saved task 41 as 01FSW9S4NX06RGNT9CDBMG6BTX.
Saved task 46 as 01FSW9S4NY85TZSEQ0T3FYNH1E.
Users with user_id "user2":
pk='01FSW9S4NK9VMZQAGDQJSF7Q8C' name='User 2' user_id='user2' job_title='Senior Janitor'

Tasks with a "TODO" status
pk='01FSW9S4NVGEFRGC6V37JV98TB' name='Clean room 361' task_id='29' status='TODO' description='Room 361 is in a terrible state.' assigned_to=[TaskAssignee(pk='01FSW9S4NT664SP90ET8H6R04N', user_id='user1'), TaskAssignee(pk='01FSW9S4NTR2SBMQHSG0HZ5QC9', user_id='user2'), TaskAssignee(pk='01FSW9S4NTFR2MNYVHNNCPGM6T', user_id='user3')]

pk='01FSW9S4NQ01CSXQCRTAHAQMT7' name='Clean room 101' task_id='12' status='TODO' description='Room 101 needs a good clean.' assigned_to=[TaskAssignee(pk='01FSW9S4NQHC69W4B7G7BMWCNB', user_id='user1'), TaskAssignee(pk='01FSW9S4NQMFC7899MVX6SJ3E6', user_id='user2')]

Tasks assigned to user with user_id "user2":
pk='01FSW9S4NVGEFRGC6V37JV98TB' name='Clean room 361' task_id='29' status='TODO' description='Room 361 is in a terrible state.' assigned_to=[TaskAssignee(pk='01FSW9S4NT664SP90ET8H6R04N', user_id='user1'), TaskAssignee(pk='01FSW9S4NTR2SBMQHSG0HZ5QC9', user_id='user2'), TaskAssignee(pk='01FSW9S4NTFR2MNYVHNNCPGM6T', user_id='user3')]

pk='01FSW9S4NX06RGNT9CDBMG6BTX' name='Clean room 369' task_id='41' status='DONE' description='Room 369 has mud on the carpet.' assigned_to=[TaskAssignee(pk='01FSW9S4NX2WDKK0FBK4T3Y3FB', user_id='user1'), TaskAssignee(pk='01FSW9S4NX30GHVXP53F9NR90K', user_id='user2'), TaskAssignee(pk='01FSW9S4NXD48KWE11YPZRJZY3', user_id='user3')]

pk='01FSW9S4NQ01CSXQCRTAHAQMT7' name='Clean room 101' task_id='12' status='TODO' description='Room 101 needs a good clean.' assigned_to=[TaskAssignee(pk='01FSW9S4NQHC69W4B7G7BMWCNB', user_id='user1'), TaskAssignee(pk='01FSW9S4NQMFC7899MVX6SJ3E6', user_id='user2')]

pk='01FSW9S4NY85TZSEQ0T3FYNH1E' name='Clean room 148' task_id='46' status='IN PROGRESS' description='Room 148 needs the bathroom cleaning.' assigned_to=[TaskAssignee(pk='01FSW9S4NY6S9JQ6HYN0H46ABV', user_id='user2'), TaskAssignee(pk='01FSW9S4NY2FD9G7JF4APBQRZH', user_id='user3')]

Tasks assigned to user with user_id "user2" with status "TODO":
pk='01FSW9S4NVGEFRGC6V37JV98TB' name='Clean room 361' task_id='29' status='TODO' description='Room 361 is in a terrible state.' assigned_to=[TaskAssignee(pk='01FSW9S4NT664SP90ET8H6R04N', user_id='user1'), TaskAssignee(pk='01FSW9S4NTR2SBMQHSG0HZ5QC9', user_id='user2'), TaskAssignee(pk='01FSW9S4NTFR2MNYVHNNCPGM6T', user_id='user3')]

pk='01FSW9S4NQ01CSXQCRTAHAQMT7' name='Clean room 101' task_id='12' status='TODO' description='Room 101 needs a good clean.' assigned_to=[TaskAssignee(pk='01FSW9S4NQHC69W4B7G7BMWCNB', user_id='user1'), TaskAssignee(pk='01FSW9S4NQMFC7899MVX6SJ3E6', user_id='user2')]

```
