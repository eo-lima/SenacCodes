namespace Cadastro_de_usuario.Models;

public class Usuarios
{
    public int ID { get; set; }
    public string Nome { get; set; } = "";
    public string Email { get; set; } = "";
    public string Senha { get; set; } = "";

    public override string ToString() => $"{ID,-4} {Nome,-25} {Email}";
}