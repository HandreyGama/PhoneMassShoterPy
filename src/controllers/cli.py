from src.services.services import ApiService

def run(args):
    print("* Iniciando Script!")
    if args.rate_limit == None:
        args.rate_limit = 0
    api = ApiService()
    api.enviar_mensagem(int(args.rate_limit))