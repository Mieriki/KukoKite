import mapper.UserMapper as userMapper

#用户登录
def login(userNmae, password):
    return userMapper.getUserByUserNameAndPassword(userNmae, password)

#用户注册
def register(userName, password, phone):
    return userMapper.addUser(userName, password, phone)

#更改密码
def changePassword(uid, password):
    return userMapper.updataUserByUid(uid ,None, password, None)

#更换手机号
def changephone(uid, phone):
    return userMapper.updataUserByUid(uid ,None, None, phone)