from mirai import Mirai, WebSocketAdapter
def bot_config():
    bot = Mirai(
    qq=941229119, 
    adapter=WebSocketAdapter(
        verify_key='12345678', host='localhost', port=8008
        )
    )
    return bot