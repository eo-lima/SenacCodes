musicas = []
playlists = []

class Musica:
    def __init__(self, titulo, artista, album, duracao):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica: Musica):
        if musica not in self.musicas:
            self.musicas.append(musica)
            print("Música adicionanda com sucesso!")
        else:
            print("Essa música já está na playlist")

    def remover_musica(self, musica: Musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print("Música removida com sucesso!")
        else:
            print("Essa música não está na playlist.")

    def listar_playlist(self):
        if len(self.musicas) == 0:
            print('Não há músicas dentro da playlist.')
        else:
            for musica in self.musicas:
                print(f"{musica.titulo}\n")

    def somar_minutos(self):
        total_minutos = 0
        for musica in self.musicas:
            total_minutos += musica.duracao
        print(f"Total de minutos: {total_minutos}")


while True:
    print("====================")
    print("==      MENU      ==")
    print("====================")
    print("1 - Cadastrar Música\n2 - Listar músicas cadastradas\n3 - Criar playlist\n4 - Adicionar música na playlist\n5 - Remover música na playlist\n6 - Exibir Playlist\n7 - Procurar música pelo autor\n8 - Sair")
    opcao = input("Digite qual operação deseja realizar: ")
    match opcao:
        case "1":
            nome_musica = input("Digite o nome da música: ")
            artista_musica = input("Digite o nome do artista: ")
            album_musica = input("Digite o nome do álbum da música: ")
            duracao_musica = int(input("Digite a duração (em minutos) da música: "))
            musica = Musica(nome_musica, artista_musica, album_musica, duracao_musica)
            musicas.append(musica)
            print("Música cadastrada!")
            continue
        case "2":
            for musica in musicas:
                print(musica.titulo)
        case "3":
            nome_playlist = input("Digite o nome da playlist: ")
            playlist = Playlist(nome_playlist)
            playlists.append(playlist)
            print("Playlist criada com sucesso!")
        case "4":
            nome_playlist = input("Digite o nome da playlist que deseja adicionar música: ")
            playlist_encontrada = None
            for playlist in playlists:
                if playlist.nome == nome_playlist:
                    playlist_encontrada = playlist
                    break
            if playlist_encontrada is None:
                print("Playlist não encontrada no sistema.")
                continue
            nome_musica = input("Digite o nome da música que deseja adicionar na playlist: ")
            musica_encontrada = None
            for musica in musicas:
                if musica.titulo == nome_musica:
                    musica_encontrada = musica
                    break
            if musica_encontrada is None:
                print("Música não encontrada.")
                continue
            playlist_encontrada.adicionar_musica(musica_encontrada)
        case "5":
            nome_playlist = input("Digite o nome da playlist que deseja remover uma música: ")
            playlist_encontrada = None
            for playlist in playlists:
                if playlist.nome == nome_playlist:
                    playlist_encontrada = playlist
                    break
            if playlist_encontrada is None:
                print("Playlist não encontrada no sistema.")
                continue
            nome_musica = input("Digite o nome da música que deseja remover da playlist: ")
            musica_encontrada = None
            for musica in musicas:
                if musica.titulo == nome_musica:
                    musica_encontrada = musica
                    break
            if musica_encontrada is None:
                print("Música não encontrada no sistema.")
                continue
            playlist_encontrada.remover_musica(musica_encontrada)
        case "6":
            nome_playlist = input("Digite o nome da playlist que deseja exibir: ")
            playlist_encontrada = None
            for playlist in playlists:
                if playlist.nome == nome_playlist:
                    playlist_encontrada = playlist
                    break
            if playlist_encontrada is None:
                print("Playlist não encontrada.")
                continue
            print("Músicas: \n")
            playlist_encontrada.listar_playlist()
            playlist_encontrada.somar_minutos()

        case "7":
            autor = input("Digite o nome do autor: ")
            musicas_encontradas = False
            for musica in musicas:
                if musica.autor == autor:
                    musicas_encontradas = True
                    print(musica.nome)
            if musicas_encontradas == False:
                print("Não há músicas com esse autor.")
                break            
        case "8":
            break