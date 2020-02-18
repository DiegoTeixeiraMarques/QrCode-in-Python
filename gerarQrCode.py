import pyqrcode
def gerar():
    qr = pyqrcode.create('https://trello.com/b/dy6S3to3/pedidos-compra-usibras')
    qr.png('youtube.png', scale=16)
gerar()