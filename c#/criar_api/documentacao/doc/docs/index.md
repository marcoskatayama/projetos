# Bem vindo ao projeto de API em C#

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## 1 Configurar projeto

- Escolha novo projeto do tipo ASP.NET Core Web API
- Exclua o arquivo WeatherForecast.cs e WeatherForecastController.cs

## 2 Models

- Crie a pasta Models
- Dentro da pasta Models crie o arquivo UsuarioModels.cs

```csharp
namespace SistemaDeTarefas.Models
{
    public class UsuarioModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }

    }
}
```

- Dentro da pasta Models crie o arquivo TarefaModels.cs

```csharp
namespace SistemaDeTarefas.Models
{
    public class TarefaModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; } 
        public string Status { get; set; }
    }
}
```
## 3 Controller

- Clique com botão direito na pasta controller > add > Controller... > API > API Controller - Empty
- Crie com o nome de UsuarioController.cs

```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace SistemaDeTarefas.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UsuarioController : ControllerBase
    {
    }
}
```

* Do jeito que esta o codigo, significa que temos a rota http://localhost:porta/api/Usuario

```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SistemaDeTarefas.Models;

namespace SistemaDeTarefas.Controllers
{
    [Route("api/[controller]")] // Rota
    [ApiController]
    public class UsuarioController : ControllerBase
    {
        [HttpGet] //Metodo
        public ActionResult<List<UsuarioModel>> BuscarTodosUsuarios() // Retorna uma lista de usuarios
        {
            return Ok(); //Ok =  HttpStatusCode.OK (200)
        }
    }
}
```

## 4 Entity Framework Core

- Botão direito em `Sistema de Tarefas` > Manage NuGet Packages
- Instalar Microsoft.EntityFrameworkCore, Microsoft.EntityFrameworkCore.Design, Npgsql.EntityFrameworkCore.PostgreSQL e Microsoft.EntityFrameworkCore.Tools

Vamos criar o contexto do nosso banco de dados

- Crie uma pasta chamada Data
- Clique com o botão direito na pasta > Add > New Item e nomeia para `SistemaTarefasDBContext.cs`

```csharp
using Microsoft.EntityFrameworkCore; // contém classes e funcionalidades para trabalhar com o Entity Framework Core, um framework de mapeamento objeto-relacional (ORM) para .NET.
using SistemaDeTarefas.Models; // contém a definição do modelo de dados usado neste contexto do banco de dados. 

namespace SistemaDeTarefas.Data
{
    public class SistemaTarefasDBContext : DbContext // classe que representa o contexto do banco de dados para o sistema de tarefas. Ela herda da classe DbContext, que é fornecida pelo Entity Framework Core e fornece funcionalidades para acessar e interagir com o banco de dados.
    {
        public SistemaTarefasDBContext(DbContextOptions<SistemaTarefasDBContext> options) : base(options) { } // Este é o construtor da classe SistemaTarefasDBContext, que recebe um parâmetro options do tipo DbContextOptions<SistemaTarefasDBContext>. Isso permite que as opções de configuração do contexto do banco de dados sejam passadas para este contexto. O construtor então chama o construtor da classe base (DbContext) passando essas opções.
        
        // Ao rodar o migration será criado as tabelas abaixo no banco de dados
        public DbSet<UsuarioModel> Usuarios { get; set; } // Um DbSet representa uma coleção de entidades no banco de dados. Neste caso, UsuarioModel é uma classe de modelo que representa a entidade de usuário. Essa propriedade permite que você consulte, insira, atualize e exclua objetos do tipo UsuarioModel no banco de dados.
        public DbSet<TarefaModel> Tarefas { get; set; }

        // Este método é chamado pelo Entity Framework Core durante a inicialização do contexto do banco de dados e é usado para configurar o modelo de entidades (entidades são representações das tabelas no banco de dados).
        protected override void OnModelCreating(ModelBuilder modelBuilder) // Esta linha declara que estamos substituindo o método OnModelCreating da classe base DbContext. O método OnModelCreating recebe um parâmetro modelBuilder do tipo ModelBuilder, que é usado para configurar o modelo de entidades.
        {
            base.OnModelCreating(modelBuilder); // Esta linha chama a implementação do método OnModelCreating na classe base DbContext. Isso é importante para garantir que qualquer configuração padrão fornecida pelo Entity Framework Core seja aplicada antes de adicionar nossas próprias configurações.
        }
    }
}
```

## 5 Repositorio

- Criar a pasta Repositorio e dentro dela criar a pasta Interface
- Clicar com botão direito em Interface > Add > New Item
- Escolher a opção Interface e nomear o arquivo para IUsuarioRepositorio.cs

```csharp
using SistemaDeTarefas.Models;

namespace SistemaDeTarefas.Repositorio.Interface
{
    public interface IUsuarioRepositorio
    {
        Task<List<UsuarioModel>> BuscarTodosUsuarios();
        Task<UsuarioModel>BuscarPorId(int id);
        Task<UsuarioModel>Adicionar(UsuarioModel usuario);
        Task<UsuarioModel> Atualizar(UsuarioModel usuario, int id);
        Task<bool> Apagar(int id);
    }
}
```

## 6 Implementar UsuarioRepositorio

- Clicar com botão direito na pasta Repositorio > Add > New Item e nomear para UsuarioRepositorio.cs

```csharp
using Microsoft.EntityFrameworkCore;
using SistemaDeTarefas.Data;
using SistemaDeTarefas.Models;
using SistemaDeTarefas.Repositorio.Interface;

namespace SistemaDeTarefas.Repositorio
{
    public class UsuarioRepositorio : IUsuarioRepositorio
    {
        private readonly SistemaTarefasDBContext _dbContext;
        public UsuarioRepositorio(SistemaTarefasDBContext sistemaTarefasDBContext)
        {
            _dbContext = sistemaTarefasDBContext;
        }
        public async Task<UsuarioModel> BuscarPorId(int id)
        {
            return await _dbContext.Usuarios.FirstOrDefaultAsync(x => x.Id == id);
        }

        public async Task<List<UsuarioModel>> BuscarTodosUsuarios()
        {
            return await _dbContext.Usuarios.ToListAsync();
        }
        public async Task<UsuarioModel> Adicionar(UsuarioModel usuario)
        {
            _dbContext.Usuarios.AddAsync(usuario);
            _dbContext.SaveChangesAsync();

            return usuario;
        }
        public async Task<UsuarioModel> Atualizar(UsuarioModel usuario, int id)
        {
            UsuarioModel usuarioPorId = await BuscarPorId(id);

            if (usuarioPorId == null)
            {
                throw new Exception($"Usuário não foi encontrado no banco de dados!");
            }

            usuarioPorId.Name = usuario.Name;
            usuarioPorId.Email = usuario.Email;

            _dbContext.Usuarios.Update(usuarioPorId);
            _dbContext.SaveChangesAsync();

            return usuarioPorId;
        }

        public async Task<bool> Apagar(int id)
        {
            UsuarioModel usuarioPorId = await BuscarPorId(id);

            if (usuarioPorId == null)
            {
                throw new Exception($"Usuário não foi encontrado no banco de dados!");
            }

            _dbContext.Usuarios.Remove(usuarioPorId);
            _dbContext.SaveChangesAsync();

            return true;
        }

    }
}
```

## 7 appsettings.json

Vamos adicionar as propriedades para ConnectionStrings

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "ConnectionStrings": {
    "DataBase": "Server=localhost;DataBase=name;User Id=postgres;Password=123"
  },
  "AllowedHosts": "*"
}
```
## 8 Program.cs

Adicionar a configuração do nosso EntityFramework, informando qual dbContext e connectionstring será utilizado

```csharp
builder.Services.AddEntityFrameworkNpgsql()
    .AddDbContext<SistemaTarefasDBContext>(
    options => options.UseNpgsql(builder.Configuration.GetConnectionString("DataBase"))
    );

builder.Services.AddScoped<IUsuarioRepositorio, UsuarioRepositorio>();
```

```csharp
using Microsoft.EntityFrameworkCore;
using SistemaDeTarefas.Data;
using SistemaDeTarefas.Repositorio;
using SistemaDeTarefas.Repositorio.Interface;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddEntityFrameworkNpgsql()
    .AddDbContext<SistemaTarefasDBContext>(
    options => options.UseNpgsql(builder.Configuration.GetConnectionString("DataBase"))
    );

builder.Services.AddScoped<IUsuarioRepositorio, UsuarioRepositorio>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
```

## 9 Enums

- Crie uma pasta chamada  "Enums" e adicione a seguinte class `StatusTarefa.cs`

```csharp
using System.ComponentModel;

namespace SistemaDeTarefas.Enums
{
    public enum StatusTarefa
    {
        [Description("A fazer")]
        AFazer =1,
        [Description("Em andamento")]
        EmAndamento = 2,
        [Description("Concluido")]
        Concluido = 3
    }
}
```

- No TarefaModel altere o Status de string para StatusTarefa

```csharp
using SistemaDeTarefas.Enums;

namespace SistemaDeTarefas.Models
{
    public class TarefaModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; } 
        public StatusTarefa Status { get; set; }
    }
}
```

## 10 Mapeamento das entidades

- Dentro da pasta Data crie a pasta Map
- Na pasta Map adicione uma class chamada `UsuarioMap.cs`

```csharp
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SistemaDeTarefas.Models;

namespace SistemaDeTarefas.Data.Map
{
    public class UsuarioMap : IEntityTypeConfiguration<UsuarioModel>
    {
        public void Configure(EntityTypeBuilder<UsuarioModel> builder)
        {
            builder.HasKey(x => x.Id);
            builder.Property(x => x.Name).IsRequired().HasMaxLength(255);
            builder.Property(x => x.Email).IsRequired().HasMaxLength(255);
        }
    }
}
``` 
- Faça a mesma coisa para TarefaMap

```csharp
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using SistemaDeTarefas.Models;

namespace SistemaDeTarefas.Data.Map
{
    public class TarefaMap : IEntityTypeConfiguration<TarefaModel>
    {
        public void Configure(EntityTypeBuilder<TarefaModel> builder)
        {
            builder.HasKey(x => x.Id);
            builder.Property(x => x.Name).IsRequired().HasMaxLength(255);
            builder.Property(x => x.Description).HasMaxLength(255);
            builder.Property(x => x.Status).IsRequired();
        }
    }
}
```

## 11 Adicionar o mapeamento para dentro do context

- Abra o arquivo SistemaTarefasDBContext.cs
- Adicione os maps

```csharp
modelBuilder.ApplyConfiguration(new UsuarioMap());
modelBuilder.ApplyConfiguration(new TarefaMap());
```

```csharp
using Microsoft.EntityFrameworkCore;
using SistemaDeTarefas.Data.Map;
using SistemaDeTarefas.Models; 

namespace SistemaDeTarefas.Data
{
    public class SistemaTarefasDBContext : DbContext 
    {
        public SistemaTarefasDBContext(DbContextOptions<SistemaTarefasDBContext> options) : base(options) { } 
        
        // Ao rodar o migration será criado as tabelas abaixo no banco de dados
        public DbSet<UsuarioModel> Usuarios { get; set; } 
        public DbSet<TarefaModel> Tarefas { get; set; }

        
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new UsuarioMap());
            modelBuilder.ApplyConfiguration(new TarefaMap());
            base.OnModelCreating(modelBuilder);
        }
    }
}
```

## 12 Gerar migration

Em Package Manager Console(View > Other Windows > Package Manager Console) digite

```bash
Add-Migration InitialDB -Context SistemaTarefasDBContext
```

Ele irá exibir ma tela o migration gerado, pode fechar 

Agora iremos rodar a migration, novamente no Package Manager Console

```bash
Update-Database -Context SistemaTarefasDBContext
```
Caso consulte agora, verá as duas tabelas criadas no banco de dados

## 13  Criando um controller para gerenciar esses dados

- Em UsuarioController vamos adicionar  os metodos necessários para realizar CRUD (Create, Read, Update e Delete).

```csharp
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SistemaDeTarefas.Models;
using SistemaDeTarefas.Repositorio;
using SistemaDeTarefas.Repositorio.Interface;

namespace SistemaDeTarefas.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UsuarioController : ControllerBase
    {
        private readonly IUsuarioRepositorio _usuarioRepositorio;

        public UsuarioController(IUsuarioRepositorio usuarioRepositorio)
        {
            _usuarioRepositorio = usuarioRepositorio;
        }

        [HttpGet]
        public async Task<ActionResult<List<UsuarioModel>>> BuscarTodosUsuarios()
        {
            List<UsuarioModel>usuarios = await _usuarioRepositorio.BuscarTodosUsuarios();
            return Ok(usuarios);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<UsuarioModel>> BuscarPorId(int id)
        {
            UsuarioModel usuario = await _usuarioRepositorio.BuscarPorId(id);
            return Ok(usuario);
        }

        [HttpPost]
        public async Task<ActionResult<UsuarioModel>> Cadastrar([FromBody]UsuarioModel usuarioModel)
        {
            UsuarioModel usuario = await _usuarioRepositorio.Adicionar(usuarioModel);
            return Ok(usuario);
        }

        [HttpPut("{id}")]
        public async Task<ActionResult<UsuarioModel>> Atualizar([FromBody] UsuarioModel usuarioModel, int id)
        {
            usuarioModel.Id = id;
            UsuarioModel usuario = await _usuarioRepositorio.Atualizar(usuarioModel,id);
            return Ok(usuario);
        }

        [HttpDelete("{id}")]
        public async Task<ActionResult<UsuarioModel>> Apagar(int id)
        {
            bool apagado = await _usuarioRepositorio.Apagar(id);
            return Ok(apagado);
        }
    }
}
```

