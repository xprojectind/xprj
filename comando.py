elif msg.text in ["/listgroup","/Listgroup"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[=> %s\n" % (cl.getGroup(i).name)
                cl.sendText(msg.to,h)
                
def autolike():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
    if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try: 
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Sora\n\nhttp://line.me/ti/p/%40dsd5411x")
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Sora\n\nhttp://line.me/ti/p/%40dsd5411x")
            print "Like"
        except:
            pass
    else:
        print "Already Liked"
        time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

# -------- VIEW SEEN ---------- 
elif msg.text.lower() == rname+' setview':
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendMessage(msg.to, "Checkpoint checked!")
                print "@setview"
            elif msg.text.lower() == rname+' viewseen':
                with open('dataSeen/'+group_id+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContact(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n* "
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendMessage(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        cl.sendMessage(msg.to, "Belum ada viewers")
                    print "@viewseen"
    except Exception as e:
        print "ERROR : " + str(e)

# ---------------- CREATOR
elif msg.text in ["Creator","creator"]:
                msg.contentType = 13
                cl.sendText(msg.to, "ADD MY CREATOR BOT SAGIRI\nPROTECT GROUP\nline.me/ti/p/~alifp.sikumbang")
                msg.contentMetadata = {'mid': 'uaa75cafbc718153f1b0e69998c51f4e7'}
                cl.sendMessage(msg)
                pass
                cl.sendText(msg.to, "ADD MY STAFF BOT SAGIRI\nPROTECT GROUP")
                msg.contentMetadata = {'mid': 'u3661447738b7d0766102618c427115d8'}
                cl.sendMessage(msg)
# ----------------- CHECK SIDERS
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
# ----------------- JIKA ADMIN / STAFF KELUAR DARI GROUP MAKA DIINVITE LAGI
        if op.type == 15:
            if op.param3 in admin:
                pass
                cl.inviteIntoGroup(op.param1, admin)
	    else:
		pass
	    if op.param2 in staff:
                pass
                cl.inviteIntoGroup(op.param1,[op.param2])
	    else:
		pass
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
            if op.param2 in Bots:
                return
            kk.sendText(op.param1, "Good Bye\n(*´･ω･*)")
            print "MEMBER HAS LEFT THE GROUP"
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
            if op.param2 in Bots:
                return
            kk.sendText(op.param1, "Welcome\n(*´･ω･*)")
            print "MEMBER HAS JOIN THE GROUP"
            
# ----------------- NOTIFED PROTECT INV MEMBER GROUP
        if op.type == 13:
            if op.param2 in Bots:
                return
            if op.param2 in admin:
                return
	    if wait ["protectinv"] == True:
                try:
                    X = cl.getGroup(op.param1)
                    gInviMids = [contact.mid for contact in X.invitee]
                    cl.cancelGroupInvitation(msg.to, gInviMids)
                    print gInviMids + "INVITE CANCEL"
                except:
                    try:
                        print "RETRY CANCEL INVITATION"
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "INVITE CANCELED"
                    except:
                        print "BOT CAN'T CANCEL THE INVITATION"
                        pass
# ----------------- Me By tag / Me @ and Mid By tag/ Mid @
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
# ----------------- Mid By tag/ Mid @ PART 2
            if "Mid:" in msg.text:
                   midd = eval(msg.contentMetadata["MENTION"])
                   key1 = midd["MENTIONEES"][0]["M"]
                   cl.sendText(msg.to,"mid:"+key1)
# ----------------- KICK MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
# ---------------- ADD STAFF By Tag / Send Contack
    "staff":{},
    "wstaff":False,
    "dstaff":False,

            if op.type == 26:
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

  
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
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
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
# -----------------
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    xname = ""
                    for mi_d in wait["blacklist"]:
                        xname = cl.getContact(mi_d).displayName + "\n"
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+"\n" " "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mi_d)+'}]}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
# -----------------
	if op.type == 19:
            if op.param3 in mid:
                try:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    kk.inviteIntoGroup(op.param1,[mid])
                except:
                    pass
            if op.param3 in Amid:
                try:
                    kc.kickoutFromGroup(op.param1,[op.param2])
                    kd.inviteIntoGroup(op.param1,[Amid])
                except:
                    pass
            if op.param3 in Bmid:
                try:
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    kf.inviteIntoGroup(op.param1,[Bmid])
                except:
                    pass
            if op.param3 in Cmid:
                try:
                    kd.kickoutFromGroup(op.param1,[op.param2])
                    ke.inviteIntoGroup(op.param1,[Cmid])
                except:
                    pass
            if op.param3 in Dmid:
                try:
                    kf.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,[Dmid])
                except:
                    pass
            if op.param3 in Emid:
                try:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    kk.inviteIntoGroup(op.param1,[Emid]
                except:
                    pass
            if op.param3 in Fmid:
                try:
                    ke.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[Fmid]
                except:
                    pass
