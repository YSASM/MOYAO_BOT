from mirai import Mirai, WebSocketAdapter
def bot_config():
    bot = Mirai(
    qq=【qq】, 
    adapter=WebSocketAdapter(
        verify_key='12345678', host='localhost', port=8008
        )
    )
    return bot
