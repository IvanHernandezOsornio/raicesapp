import web

db_host = 'z1ntn1zv0f1qbh8u.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'ch2grp8la2imunk5'
db_user = 't07nr2nt5lmby05q'
db_pw = 'gqlbcxkuzeqnl2tb'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )