# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

a = open("token/me.txt")
for token in a:
    print token,
cl = LINETCR.LINE()
cl.login(token=token)
cl.loginResult()

a.close()

f = open("token/ki.txt")
for token in f:
    print token,
ki = LINETCR.LINE()
ki.login(token=token)
ki.loginResult()
f.close()

f = open("token/kk.txt")
for token in f:
    print token,
kk = LINETCR.LINE()
kk.login(token=token)
kk.loginResult()
f.close()

f = open("token/kc.txt")
for token in f:
    print token,
kc = LINETCR.LINE()
kc.login(token=token)
kc.loginResult()
f.close()

f = open("token/kd.txt")
for token in f:
    print token,
kd = LINETCR.LINE()
kd.login(token=token)
kd.loginResult()
f.close()

f = open("token/ke.txt")
for token in f:
    print token,
ke = LINETCR.LINE()
ke.login(token=token)
ke.loginResult()
f.close()

f = open("token/kf.txt")
for token in f:
    print token,
kf = LINETCR.LINE()
kf.login(token=token)
kf.loginResult()
f.close()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" Keyword BOT

|=*=Key Member=*=|
➡️Ginfo (Check Group Info)
➡️Banlist (Check Account Banned)
➡️Gift (Send Your Suprise)
➡️Gn [Free Change Name Group]
➡️Me By TAG / Me [Send CONTACT BY TAG / Send Your Contact]
➡️Mid By tag / Mid [SHOW MID BY TAG / SHOW YOUR MID]
➡️Creator [LOOK CREATOR BOT SAGIRI]
➡️Staff [LOOK STAFF BOT SAGIRI]
➡️$set and $read [Check Siders]

|=*=Key ADMIN & SPECIAL USER=*=|
➡️All join (Invite all bot)
➡️Bye all (Leave all bot)
➡️/List Group [Show List Group]
➡️@Bye [All BOT LEAVE IN GROUP]
➡️Ban @ (with Tag)
➡️Ban (With send Contact)
➡️Unban @ (With tag)
➡️Unban (With send Contact)
➡️Nk @(with Tag ) [Kick]
➡️Kill ban [Kick User Banned/Banlist]
➡️Respon ( Bot Respon )
➡️Test (Bot Respon)
➡️Kontak bot [SEND CONTACT BOT IN GROUP]
➡️absen(Bot The Count) [ Bot Absen]
➡️Invite [Mid] (Bot Invite Members With mid]
➡️Cancel [Cancel Invited Group Fast]
➡️Ourl [Open Url Group]
➡️Curl [Close Url Group]
➡️Gurl [Gift You Url Group]

|=*=Key Only ADMIN=*=|
➡️Cleanse [Kick all member a Group]
➡️Bye @ [KICK MEMBER]
➡️Kick (Mid) [Kick Members]
➡️Add Staff With Tag / Send Contact
*********************************
****Created AlifP.Sikumbang****
**Instagram: @alifp.sikumbang*
**Protect / Damage Your Group*
*********************************
"""
helpMessage2 =""" PENJELASAN BOT

=*=FITUR BOT STAFF/ADMIN=*=
[JIKA ADMIN/STAFF KELUAR DARI GROUP MAKA - BOT AKAN MENGINVITE]
[JIKA ADMIN/STAFF DIKICK MAKA BOT AKAN MENGINVITE]
[FITUR* BAN / UNBAN - UNTUK BAN CONTAC / UNBAN CONTACT]
[FITUR* NK BY TAG UNTUK MENGKICK ORANG - EXAMPLE NK @namaDiTag]
[FITUR* OURL/GURL/CURL - UNTUK MEMBUKA QR ATAU MENUTUP QR]
[FITUR* CLEANSE - UNTUK MERATAKAN GRUP]
[FITUR* /LIST GROUP - UNTUK MELIHAT LIST GROUP YG BOT JOIN KAN]
[FITUR* DADAH - SEMUA BOT AKAN KELUAR DARI GROUP]
[FITUR* ALL JOIN - SEMUA BOT AKAN MASUK KE GROUP]
[FITUR* INVITE - FITUR INI UNTUK MENGINVITE BY MID , KETIK DAHALU MID @tagNamanya]
[FITUR* P on/off - UNTUK PROTECT JIKA ADA YG NGEKICK MEMBER SELAIN ADMIN/STAFF MAKA AKAN DIKICK]
[FITUR* Inv on/off - UNTUK INVITE JIKA ADA MEMBER YG MENGUNDANG SEMBARANG ORANG AKAN DIKICK DAN MENGCANCEL UNDANGAN]
[FITUR* Qr on/off - UNTUK QR GRUP JIKA ADA YG MEMBUKANYA SELAIN ADMIN/STAFF MAKA BOT AKAN OTOMATIS MENUTUPNYA]
[FITUR* ADD STAFF - MENAMBAHKAN STAFF *ADMIN ONLY NO STAFF NO MEMBERS]
[FITUR* CHECK SIDERS DI GROUP]
*********************************
****Created AlifP.Sikumbang****
**Instagram: @alifp.sikumbang*
**Protect / Damage Your Group*
*********************************
"""
KAC=[cl,ki,kk,kc,kd,ke,kf]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,"uaa75cafbc718153f1b0e69998c51f4e7"]
staff=["uaa75cafbc718153f1b0e69998c51f4e7","u60ddc5ebe9073a3f0b5f794cf2fc7761","u907b8700898c865ed0738ce924496408","u3661447738b7d0766102618c427115d8","ua5231264e098148b585af774928543be","u862ccc55d06161c611dd9fb2fb3fa818","uabaae1607b1eef506d69c2757b830b82","udee72f392d265ad9eea613acc6160397","u2b2f227384e5b0bf04071f849fe160fc"]
admin=["uaa75cafbc718153f1b0e69998c51f4e7"]
wait = {
    'protect':True,
    'protectinv':True,
    'protectqr':True,
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add me , Dont Forget For add Owner Me\nIDLine: alifp.sikumbang",
    "lang":"JP",
    "comment":"Thanks for add me , Dont Forget For add Owner Me\nIDLine: alifp.sikumbang",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"SAGIRI-Chan ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "staff":{},
    "wstaff":False,
    "dstaff":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
  if op.type == 55:
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            cl.sendText
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)

                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)

                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)

                if op.param3 in Fmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 55:
                try:
                    if op.param1 in wait2['readPoint']:
                        Name = cl.getContact(op.param2).displayName
                        if Name in wait2['readMember'][op.param1]:
                            pass
                        else:
                            wait2['readMember'][op.param1] += "\n・" + Name
                            wait2['ROM'][op.param1][op.param2] = "・" + Name
                    else:
                        pass
                except:
                    pass

        if op.type == 24:
	    if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
            elif wait ["protect"] == True:
                ke.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
	    else:
                pass

        if op.type == 15:
	    if op.param3 in admin:
		pass
        	cl.inviteIntoGroup(op.param1, admin)
	    else:
		pass

        if op.type == 32:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
		cl.kickoutFromGroup(op.param1,[op.param2])
		cl.inviteIntoGroup(op.param1,[op.param3])
	    else:
		pass

        if op.type == 11:
	    if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
	    elif wait ["protectqr"] == True:
		X = ki.getGroup(op.param1)
		X.preventJoinByTicket = True
		ki.updateGroup(X)
	    else:
		pass

	if op.type == 19:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
            elif wait ["protect"] == True:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 13:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
            if op.param2 in staff:
                return
	    if wait ["protectinv"] == True:
                try:
                    X = cl.getGroup(op.param1)
                    gInviMids = [contact.mid for contact in X.invitee]
                    cl.cancelGroupInvitation(msg.to, gInviMids)
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    print gInviMids + "INVITE CANCEL"
                except:
                    try:
                        print "RETRY CANCEL INVITATION"
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        print gInviMids + "INVITE CANCELED"
                    except:
                        print "BOT CAN'T CANCEL THE INVITATION"
                        pass

        if op.type == 19:
            if op.param3 in admin:
                ke.kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1, admin)
            else:
                pass
	    if op.param3 in staff:
		kd.kickoutFromGroup(op.param1,[op.param2])
		cl.inviteIntoGroup(op.param1, staff)
	    else:
		pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kd.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            ke.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            kf.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kd.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kd.updateGroup(G)
                    Ticket = kd.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kf.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kf.updateGroup(G)
                    Ticket = kf.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        return
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            ke.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            wait["blacklist"][op.param2] = True
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        wait["blacklist"][op.param2] = True
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.inviteIntoGroup(op.param1, admin)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.inviteIntoGroup(op.param1, admin)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Dihapus")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Ditambahkan")
                        print "SUKSES -- BLACKLIST DITAMBAHKAN"

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        print "SUKSES -- BLACKLIST DIHAPUS"
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wstaff"] == True:
                   if msg.contentMetadata["mid"] in wait["staff"]:
                        cl.sendText(msg.to,"already")
                        wait["wstaff"] = False
                   else:
                        wait["staff"][msg.contentMetadata["mid"]] = True
                        wait["wstaff"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dstaff"] == True:
                   if msg.contentMetadata["mid"] in wait["staff"]:
                        del wait["staff"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dstaff"] = False

                   else:
                        wait["dstaff"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help","key"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    print "SUKSES -- KEYWORD"
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["fitur bot","Fitur bot","Fitur","fitur"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    pass
                    print "SUKSES -- FITUR BOT"
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                    print "SUKSES -- CHANGE NAME GROUP"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      random.choice(KAC).kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif "Kick " in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
                print "SUKSES -- KICK BY MID"
            elif "Invite " in msg.text:
              if msg.from_ in staff:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                print "SUKSES -- INVITED BY MID"
            elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY CREATOR BOT SAGIRI\nPROTECT GROUP")
                msg.contentMetadata = {'mid': 'uaa75cafbc718153f1b0e69998c51f4e7'}
                cl.sendMessage(msg)
                pass
            elif msg.text in ["Staff","staff"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY STAFF BOT SAGIRI\nPROTECT GROUP")
                msg.contentMetadata = {'mid': 'u3661447738b7d0766102618c427115d8'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'ua5231264e098148b585af774928543be'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'uabaae1607b1eef506d69c2757b830b82'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'udee72f392d265ad9eea613acc6160397'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u907b8700898c865ed0738ce924496408'}
                cl.sendMessage(msg)
                print "SUKSES -- SEND CREATOR AND STAFF"
            elif msg.text in ["Contact bot","contact bot","kontak bot","Kontak bot","kibarin","Kibarin"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY CONTACT BOT SAGIRI\nBOT PROTECT GROUP")
                msg.contentMetadata = {'mid': 'u40fba5051ae9c81cc65310d36c940877'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u43a6c3898a378e92c45965dcf9a21904'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'uf2e1938788bbf6e3edcd8a92d185213c'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'ucad7568b9a8722e3e0d7c763f5704a9e'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'ua086d1f8155d6dc637d41a43c2d61cd6'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u8f60f220e58473c5d5128f6bb0749844'}
                cl.sendMessage(msg)
                pass
                msg.contentMetadata = {'mid': 'u9e6da4aacc47dbbf7b1123c96197e483'}
                cl.sendMessage(msg)
                print "SUKSES -- SEND CONTACT BOT"
            elif msg.text in ["me","Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
                print "SUKSES -- SEND CONTACT"
            elif msg.text in ["gift","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '1066653',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '2'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif msg.text in ["gift1","Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8588',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif msg.text in ["gift2","Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '5594',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '4'}
                msg.text = None
                cl.sendMessage(msg)
                print "SUKSES -- SEND GIFT"
            elif msg.text in ["cancel","Cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "SUKSES -- CANCEL INVITE GROUP"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","ourl","our","Our"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    print "SUKSES -- OPEN URL GROUP"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","curl"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    print "SUKSES -- CLOSE URL GROUP"
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    print "SUKSES -- SEND GINFO"
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif msg.text in ["Mid","mid","MID"]:
                print "SUKSES -- SHOW MID USER"
                cl.sendText(msg.to, msg.from_)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif ("Cn " in msg.text):
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif ("Cn1 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn1 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif ("Cn2 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn2 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif ("Cn3 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn3 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kc.getProfile()
                    profile_B.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"name " + string + " done")
            elif ("Cn4 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn4 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kd.getProfile()
                    profile_B.displayName = string
                    kd.updateProfile(profile_B)
                    kd.sendText(msg.to,"name " + string + " done")
            elif ("Cn5 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn5 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ke.getProfile()
                    profile_B.displayName = string
                    ke.updateProfile(profile_B)
                    ke.sendText(msg.to,"name " + string + " done")
            elif ("Cn6 " in msg.text):
              if msg.from_ in admin:
                string = msg.text.replace("Cn6 ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kf.getProfile()
                    profile_B.displayName = string
                    kf.updateProfile(profile_B)
                    kf.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid": msg.from_}
                cl.sendMessage(msg)
            elif msg.text in ["protect on","protect:on","Protect on","Protect:on","p on","P on"]:
              if msg.from_ in staff:
		if wait["protect"] == True:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT ON"
			cl.sendText(msg.to,"already 🔛")
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protect"] = True
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT ON"
			cl.sendText(msg.to,"already 🔛")
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["protect off","Protect off","Protect:off","protect:off","p off","P off"]:
              if msg.from_ in staff:
		if wait["protect"] == False:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT OFF"
			cl.sendText(msg.to,"already ⛔")
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protect"] = False
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT OFF"
			cl.sendText(msg.to,"already ⛔")
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["protectinv on","protectinv:on","Protectinv:on","Protectinv on","inv on","Inv on"]:
              if msg.from_ in staff:
		if wait["protectinv"] == True:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT INV ON"
			cl.sendText(msg.to,"already 🔛")
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectinv"] = True
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT INV ON"
			cl.sendText(msg.to,"already 🔛")
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["protectinv off","Protectinv off","Protectinv:off","protectinv:off","deff off","inv off","Inv off"]:
              if msg.from_ in staff:
		if wait["protectinv"] == False:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT INV OFF"
			cl.sendText(msg.to,"already ⛔")
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectinv"] = False
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT INV OFF"
			cl.sendText(msg.to,"already ⛔")
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["protectqr on","protectqr:on","Protectqr:on","Protectqr on","Qr on","qr on"]:
              if msg.from_ in staff:
		if wait["protectqr"] == True:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT QR ON"
			cl.sendText(msg.to,"already 🔛")
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectqr"] = True
		    if wait["lang"] == "JP":
                        print "SUKSES -- PROTECT QR ON"
			cl.sendText(msg.to,"already 🔛")
		    else:
			cl.sendText(msg.to,"Done")
	    elif msg.text in ["protectqr off","Protectqr:off","Protectqr off","protectqr:off","qr off","Qr off"]:
              if msg.from_ in staff:
		if wait["protectqr"] == False:
		    if wait["lang"] == "JP":
                        print "EXECUTED -- PROTECT QR OFF"
			cl.sendText(msg.to,"already ⛔")
		    else:
			cl.sendText(msg.to,"Done")
		else:
		    wait["protectqr"] = False
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"already ⛔")
			print "SUKSES -- PROTECT QR OFF"
		    else:
			cl.sendText(msg.to,"Done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ⛔")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already 🔛")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
                md = ""
                if wait["protect"] == True: md+=" 🔛Protect : on\n"
                else: md+=" ⛔Protect : off\n"
                if wait["protectinv"] == True: md+=" 🔛Protectinv : on\n"
                else: md+=" ⛔Protectinv : off\n"
                if wait["protectqr"] == True: md+=" 🔛Protectqr : on\n"
                else: md+=" ⛔Protectqr : off\n"
                if wait["contact"] == True: md+=" 🔛Contact : on\n"
                else: md+=" ⛔Contact : off\n"
                if wait["autoJoin"] == True: md+=" 🔛Auto join : on\n"
                else: md +=" ⛔Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" 🔛Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " ⛔Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" 🔛Auto leave : on\n"
                else: md+=" ⛔Auto leave : off\n"
                if wait["timeline"] == True: md+=" 🔛Share : on\n"
                else:md+=" ⛔Share : off\n"
                if wait["autoAdd"] == True: md+=" 🔛Auto add : on\n"
                else:md+=" ⛔Auto add : off\n"
                if wait["commentOn"] == True: md+=" 🔛Comment : on\n"
                else:md+=" ⛔Comment : off\n"
                cl.sendText(msg.to,md)
            elif msg.text in ["Group id","group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["/listgroup","/Listgroup","/List group","/list group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[=> %s\n" % (cl.getGroup(i).name)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                    print "SUKSES -- SEND CANCELALL"
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                    print "SUKSES -- OPEN AND SHARE LINK GROUP"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "SUKSES -- SEND $SET CHECK SIDERS"
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "⬇️Orang Siders ⬇️%s\n⬆️⬆️⬆️\n⬇️Orang - orang yang telah Mengabaikan membaca⬇️\n%sHal Yang Tidak Normal ♪\n\nDibuat pada Tanggal&Jam:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "SUKSES -- SEND $READ CHECK SIDERS"
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
            elif msg.text in ["All join","all join","sokin","Sokin","woi masuk"]:
                if msg.from_ in staff:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    print "EXECUTED -- SUMMON BOT"
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.0)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    print "SUKSES -- SUMMON BOT"
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)

            elif msg.text in ["sagiri join"]:
                  X = kc.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  kc.updateGroup(X)
                  invsend = 0
                  Ti = kc.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kc.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
                if msg.from_ in staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "JOIN -- SUCCESS"
                        G.preventJoinByTicket = True
                        kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Bye all","bye all","dadah","Dadah"]:
                  if msg.from_ in staff:
                    ginfo = cl.getGroup(msg.to)
                    print "EXECUTED -- BOT OUT GROUP"
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
                        print "SUKSES -- BOT OUT GROUP"
                    except:
                        pass
            elif msg.text in ["Bot1 @bye","sagiri bye","bye","bot1 @bye","@bye","@Bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"BYE")
                        return
                    for jj in matched_list:
                        try:
                            klist=[kc,kd,ke,kf]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                            print "SUKSES -- SEND KILL"
                        except:
                            pass
            elif "Cleanse" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "EXECUTED -- CLEANSE GROUP"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    ki.sendText(msg.to,"**THANKS FOR GRUP**\nDANGEROUS!")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not targets in Bots:
                            try:
                                klist=[ki,kk,kc,kd,ke,kf]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")
                                print "SUKSES -- CLEANSE GROUP"
            elif "Nk " in msg.text:
                if msg.from_ in staff:
                       print "EXECUTED -- NK TARGET"
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kf.kickoutFromGroup(msg.to,[target])
                                    print "SUKSES -- NK TARGET"
                                except:
                                    pass
            elif "tagall" in msg.text:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                key = eval(msg.contentMetadata("MENTION"))
                key1 = key["MENTIONEES"][0]["M"]
                mem = [contact.mid for contact in group.members]
                for mm in mem:
                    xname = cl.getGroup(mm).displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    msg.text = "@"+xname+" "+key1
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            elif ("Ban " in msg.text):
              if msg.from_ in staff:
                print "EXECUTED -- BAN TARGET"
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Ter-Banned")
                      print "SUKSES -- BAN TARGET"
                   except:
                      pass
            elif "Unban @" in msg.text:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "EXECUTED -- UNBAN TARGET"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes Unbaned")
                                print "SUKSES -- UNBAN TARGET"
                            except:
                                ki.sendText(msg.to,"Succes UNBANNED")
            elif "getbio @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "EXECUTED -- Getbio TARGET"
                    _name = msg.text.replace("getbio @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                bio = cl.getContact(target).statusMessage
                                Name = cl.getContact(target).displayName
                                cl.sendText(msg.to,Name + " Bio: " + bio)
                                print "SUKSES -- Getbio TARGET"
                            except:
                                pass
            elif "getpict @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    _name = msg.text.replace("getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                ginfo = cl.getContact(target)
                                cl.sendText(msg.to, "[Profile Status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                                cl.sendImage("http://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                                print "SUKSES -- Getpict TARGET"
                            except:
                                pass
            elif "add staff @" in msg.text:
                if msg.from_ in admin:
                    print "EXCUTED -- ADD STAFF"
                    _name = msg.text.replace("add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["staff"][target] = True
                                cl.sendText(msg.to,"Succes Add Staff")
                            except:
                                ki.sendText(msg.to,"Error")
            elif "del staff @" in msg.text:
                if msg.from_ in admin:
                    print "EXCUTED -- DELETE STAFF"
                    _name = msg.text.replace("del staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["staff"][target]
                                cl.sendText(msg.to,"Succes Deleted Staff")
                            except:
                                ki.sendText(msg.to,"Succes Deleted Staff")
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                        pass
            elif "status @" in msg.text:
                msg.contentType = 0
                _name = msg.text.replace("status @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getContact(mid)
                for g in gs.members:
                    if _nametarget == gs.displayName:
                        cl.sendText(msg.to, "[Status Message]" + gs.statusMessage)
                    else:
                        pass 
#-----------------------------------------------
            elif msg.text in ["Test"]:
               if msg.from_ in staff:
                ki.sendText(msg.to,"Ok Cv 􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            elif "Bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Bc ","")
		    ki.sendText(msg.to,(bctxt))
                    kk.sendText(msg.to,(bctxt))
                    kc.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Respon","respon","absen","Absen"]:
              if msg.from_ in staff:
                cl.sendText(msg.to,"Hadir[V1]")
                ki.sendText(msg.to,"Hadir[V2]")
                kk.sendText(msg.to,"Hadir[V3]")
                kc.sendText(msg.to,"Hadir[V4]")
                kd.sendText(msg.to,"Hadir[V5]")
                ke.sendText(msg.to,"Hadir[V6]")
                kf.sendText(msg.to,"Hadir[V7]")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
		pass
		start = time()
                ki.sendText(msg.to, "Progress...")
                elapsed_time = time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
              if msg.from_ in staff:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in staff:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["add staff"]:
              if msg.from_ in admin:
                wait["wstaff"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["del staff"]:
              if msg.from_ in admin:
                wait["dstaff"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["list staff"]:
                if wait["staff"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Staff user")
                    mc = ""
                    for mi_d in wait["staff"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in staff:
                if msg.toType == 2:
                    print "EXCUTED -- KILL BAN"
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        print "SUKSES -- KILL BAN"
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Good Bye Sampah")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
