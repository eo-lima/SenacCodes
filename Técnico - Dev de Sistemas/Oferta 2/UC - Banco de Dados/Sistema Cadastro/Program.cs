using Cadastro_de_usuario.Data;
using Cadastro_de_usuario.Models;
using MySql.Data.MySqlClient;

var repositorio = new UsuarioRepositorio(new Conexao());

try
{
    if(!Login(repositorio)) return;

    MenuPrincipal(repositorio);
}
catch(MySqlException ex)
{
    Console.WriteLine($"Erro de banco de dados: {ex.Message}");
    Console.WriteLine("Verifique a Conexão");
}

static bool Login(UsuarioRepositorio repo)
{
    for(int tentativa = 1; tentativa <= 3; tentativa++)
    {
        Console.Clear();
        Console.WriteLine("=== LOGIN ===");
        string email = Ler("Email: ");
        string senha = Ler("Senha: ");

        var usuario = repo.Autenticar(email, senha);
        if(usuario != null)
        {
            Console.WriteLine($"Bem-vindo, {usuario.Nome}!");
            Pausar();
            return true;
        }
        Console.WriteLine("Email ou senha inválidos. Tente novamente.");
        Console.WriteLine($"Tentativa {tentativa} de 3.");
        Pausar();
    }
    Console.WriteLine("Número máximo de tentativas atingido.");
    return false;
}

static void MenuPrincipal(UsuarioRepositorio repo)
{
    while(true)
    {
        Console.Clear();
        Console.WriteLine("=== MENU PRINCIPAL ===");
        Console.WriteLine("1. Cadastrar Usuário");
        Console.WriteLine("2. Listar Usuários");
        Console.WriteLine("3. Editar Usuário");
        Console.WriteLine("4. Excluir Usuário");
        Console.WriteLine("5. Sair");
        Console.Write("Escolha uma opção: ");

        switch(Console.ReadLine())
        {
            case "1":
                Cadastrar(repo);
                break;
            case "2":
                Listar(repo);
                break;
            case "3":
                Editar(repo);
                break;
            case "4":
                Excluir(repo);
                break;
            case "5":
                return;
            default:
                Console.WriteLine("Opção inválida.");
                Pausar();
                break;
        }
    }
}

static void Cadastrar(UsuarioRepositorio repo)
{
    Console.WriteLine("=== CADASTRAR USUÁRIO ===");
    var u = new Usuarios
    {
        Nome = Ler("Nome: "),
        Email = Ler("Email: "),
        Senha = Ler("Senha: ")
    };
    try
    {
        repo.Cadastrar(u);
        Console.WriteLine("Usuário cadastrado com sucesso!");
    }
    catch (MySqlException ex) when (ex.Number == 1062)
    {
        Console.WriteLine("Já existe um usuário com este email.");
    }
    Pausar();

}

static void Listar(UsuarioRepositorio repo)
{
    Console.WriteLine("=== LISTA DE USUÁRIOS ===");
    var lista = repo.Listar();
    if (lista.Count == 0)
    {
        Console.WriteLine("Nenhum usuário encontrado.");
        Pausar();
        return;
    }
    else
    {
        System.Console.WriteLine($"{"ID",-4} {"Nome",-25} Email");
        lista.ForEach(Console.WriteLine);
    }

}

static void Editar(UsuarioRepositorio repo)
{
    ListarNaTela(repo);
    if(!int.TryParse(Ler("Digite o ID do usuário que deseja editar: "), out int id))
    {
        Console.WriteLine("ID inválido.");
        Pausar();
        return;
    }
    var u = new Usuarios
{
        ID = id,
        Nome = Ler("Novo Nome: "),
        Email = Ler("Novo Email: ")
};
    try
    {
        Console.WriteLine(repo.Editar(u) ? "Usuário editado com sucesso!" : "Usuário não encontrado.");
    }
    catch (MySqlException ex) when (ex.Number == 1062)
    {
        Console.WriteLine("Já existe um usuário com este email.");
    }
}

static void ListarNaTela(UsuarioRepositorio repo)
{
    Console.WriteLine("=== USUÁRIOS CADASTRADOS ===");
    var lista = repo.Listar();
    Console.WriteLine($"{"ID",-4} {"Nome",-25} Email");
    lista.ForEach(Console.WriteLine);
}

static void Excluir(UsuarioRepositorio repo)
{
    ListarNaTela(repo);
    if(!int.TryParse(Ler("Digite o ID do usuário que deseja excluir: "), out int id))
    {
        Console.WriteLine("ID inválido.");
        Pausar();
        return;
    }
    if (Ler("Tem certeza? (s/n): ").ToLower() != "s")
    {
        Console.WriteLine("Exclusão cancelada.");
        Pausar();
    }
    else
    {
        Console.WriteLine(repo.Excluir(id) ? "Usuário excluído com sucesso!" : "Usuário não encontrado.");
        Pausar();
    }
}

static void Pausar()
{
    Console.WriteLine("Pressione ENTER para continuar...");
    Console.ReadLine();
}

static string Ler(string texto)
{
    Console.Write(texto);
    return Console.ReadLine()?.Trim()?? "";
}
