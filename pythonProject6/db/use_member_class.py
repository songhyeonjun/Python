from db.member_dao_class import *

if __name__ == '__main__':
    vo = input('id,name,url,img>> ').split(',')
    dao = DAO()
    dao.create(vo)
