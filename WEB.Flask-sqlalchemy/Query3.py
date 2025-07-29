from flask import Flask
 
db_name = input()
global_init(db_name)
db_sess = create_session()
colonists = db_sess.query(User).all()
for i in colonists:
    if i.age < 18:
        print(i, i.age, "years")