def __init__(bot):
    # suijiimg.main(bot)
    # setjytime.main(bot)
    # jytime.main(bot)
    # fudu.main(bot,389391931)
    # bilibililive.main(bot) 
    # muteAll.main(bot)
    from .import weather
    weather.Weather(bot) 
    from .import qiandao
    qiandao.Qiandao(bot)
    # chehuigoudi.main(bot) 
    # goudikouqiu.main(bot)
    from .import tuijianeat
    tuijianeat.Tuijianeat(bot)
    # tuijianeat.main(bot)
    # yuanshen.main(bot)
    from .import zaowan
    zaowan.Zaowan(bot)
    # tiren.main(bot)