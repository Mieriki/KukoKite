import mapper.AdmainMapper as adminMapper
import entity.Admin as Admin

#管理员登录
def login(userName, password):
    return adminMapper.getAdminByUserNameAndPassword(userName, password)


#添加新的管理员
def addAdmin(admin , userName, password, permissionLevel):
    if admin.permissionLevel == 0:
        return adminMapper.getAdminByUserNameAndPassword(userName, password, permissionLevel)
    return None

#删除管理员
def deleteAdmin(aid):
    return adminMapper.deleteAdminByAid(aid)
