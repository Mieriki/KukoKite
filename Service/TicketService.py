import mapper.TicketMapper as ticketMapper

#获取用户订单
def getTicket(uid, fid, cid, isPayment, fromCity, toCity):
    return ticketMapper.getTicketByUid(uid, fid, cid, isPayment, fromCity, toCity)

#添加用户订单
def addTicket(uid, fid, cid):
    return ticketMapper.getTicketByUid(uid, fid, cid, 1)

#用户删除订单
def deleteTicket(tid):
    return ticketMapper.deleteTicKetByTid(tid)

#付款
def payment(tid):
    return ticketMapper.updataTicKetByTid(tid)
