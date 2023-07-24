import sqlalchemy
# web_test
# 0 id
# 1 title
# 2 location
# 3 salary
# 4 currency
# 5 responsibities
# 6 requirements
#

engine = sqlalchemy.create_engine('mysql+pymysql://tldm95f00mafz538n090:pscale_pw_SG10kO1SExFPxxk2HPoxSwVEczdGvIzIMnc9Ujo0Fmu@aws.connect.psdb.cloud/web_test?charset=utf8mb4',connect_args = {
  "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
  }
})

#with engine.connect() as conn:
# result = conn.execute(sqlalchemy.text('SELECT * FROM jobs'))
# result_list = result.all()[0]._asdict()
# print(result.all())

def get_content(id):
  x = id
  page = ''
  with engine.connect() as conn:
    get_pags = conn.execute(sqlalchemy.text("SELECT * FROM jobs WHERE id = :page "), {"page":id})
  hax_list = []
  for _ in get_pags.all():
    hax_list.append(_._asdict())
  return hax_list
    