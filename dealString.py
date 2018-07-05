file=('26','28','29','30','32')
servers = ('61003','61004','61005','61006','61007')
for server in servers:
    print("############################" + server + "###############################" )
    for filename in file:
        f = open( server+'/'+filename + ".txt")
        #print("---------------" +server+'/'+filename + "----------------------")
        line = f.readline()
        bossMap={}
        while line:
            lower = line.index( "CellApp" )
            uper = line.index( "boss" )
            dateIndex = line.index( "2015-10-07" )
            headline = line[dateIndex+10:dateIndex+19]+" : " + line[uper+6:uper+14]
            idx = line.index("str:")+5
            strline = line[idx:]
            if headline in bossMap:
                bossMap[headline] += strline
            else:
                bossMap[headline] =strline
            line = f.readline()
        PH ={}
        for key in bossMap:
            BH = {}
            GH = {}
            str = bossMap[key]
            newstr = ''.join(str.split(']'))
            newstr = ''.join(newstr.split('\n'))
            playerHurt = newstr.split('playerId')
            for hurtEle in playerHurt:
                elestr = ''.join( hurtEle.split(':'))
                elestr = ''.join(elestr.split(','))
                elestr = ''.join(elestr.split('hurt'))
                elestr = ''.join(elestr.split('group'))
                hurtIdx = elestr.split()
                if 0 == len(hurtIdx):
                    #print( key )
                    continue
                hurt = 0;
                playerId = hurtIdx[0]
                playerhurt = hurtIdx[1]
                playergroup = hurtIdx[2]
                hurt = int(playerhurt)
                if playerId in BH:
                    BH[playerId]+= hurt
                else:
                    BH[playerId] = hurt
                if playergroup in GH:
                    GH[playergroup] += "," + playerId
                else:
                    GH[playergroup] = playerId
            gh = 0
            groupHurt={}
            for groupele in GH:
                gh = 0
                if groupele == '0':
                    continue
                member = GH[groupele].split(',')
                for m in member:
                    gh += BH[m]
                groupHurt[groupele] = gh
                #print( groupele, gh, member)
            sorted( groupHurt.items(), key=lambda d:d[1], reverse = True)
            maxHurt = max(groupHurt.items(), key=lambda d:d[1])
            outkey = maxHurt[0]
            #print(maxHurt[1],GH[outkey])
            print(GH[outkey])
        f.close()
    print('\n\n\n')
