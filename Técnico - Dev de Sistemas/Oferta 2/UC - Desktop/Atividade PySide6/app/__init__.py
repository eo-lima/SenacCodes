from pathlib import Path #Manipulação dos caminhos do sistema

base_dir = Path(__file__).resolve().parent.parent #Pasta do projeto (app/ para raiz)
imagem_login = base_dir / "login.jpg"
imagem_perfil = base_dir / "image.jpg"

__all__ = ["base_dir", "imagem_login", "imagem_perfil"]