from .import set_nember_name,muteAll,jytime,fudu,setjytime,suijiimg,tuijianeat,tianqi,bilibililive,chehuigoudi,goudikouqiu,qiandao,yuanshen,zaowan,tiren
class Start(object):
    def import_plugins(bot):
        suijiimg.main(bot)
        setjytime.main(bot)
        jytime.main(bot)
        fudu.main(bot,389391931)
        #bilibililive.main(bot) 
        muteAll.main(bot)
        tianqi.main(bot) 
        qiandao.main(bot)
        chehuigoudi.main(bot) 
        goudikouqiu.main(bot)
        tuijianeat.main(bot)
        yuanshen.main(bot)
        zaowan.main(bot)
        tiren.main(bot)