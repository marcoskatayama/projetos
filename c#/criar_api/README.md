# Bem-vindo ao projeto de API em C#

Este projeto é uma API em C# desenvolvida usando ASP.NET Core. A API permite gerenciar usuários e tarefas, fornecendo endpoints para criar, ler, atualizar e excluir esses recursos.

## 1. Configuração do projeto

Para configurar o projeto, siga estas etapas:

- Inicie um novo projeto do tipo ASP.NET Core Web API.
- Remova os arquivos WeatherForecast.cs e WeatherForecastController.cs, que são gerados por padrão.
- Esses arquivos não são necessários para o nosso projeto e podem ser excluídos com segurança.

## 2. Models

Os modelos são classes que representam as entidades do nosso domínio. No nosso caso, temos os modelos `UsuarioModel` e `TarefaModel` para representar usuários e tarefas, respectivamente.

- `UsuarioModel`: Representa um usuário com as propriedades Id, Name e Email.
- `TarefaModel`: Representa uma tarefa com as propriedades Id, Name, Description e Status.

## 3. Controller

Os controladores são responsáveis por receber requisições HTTP e retornar respostas adequadas. 

- `UsuarioController`: Responsável por lidar com operações relacionadas a usuários, como buscar todos os usuários, buscar usuário por id, cadastrar, atualizar e apagar usuário.

## 4. Entity Framework Core

O Entity Framework Core é utilizado para mapear os modelos para o banco de dados e realizar operações de persistência.

- Configuração do contexto do banco de dados: Criamos a classe `SistemaTarefasDBContext` que herda de `DbContext` e contém `DbSet`s para os modelos `UsuarioModel` e `TarefaModel`.

- Migrations: Utilizamos migrações do Entity Framework Core para criar e atualizar o esquema do banco de dados de acordo com as mudanças no modelo.

## 5. Repositório

Os repositórios são responsáveis por encapsular a lógica de acesso a dados e fornecer uma abstração sobre o DbContext.

- `IUsuarioRepositorio`: Interface que define os métodos para operações relacionadas a usuários, como buscar todos os usuários, buscar usuário por id, cadastrar, atualizar e apagar usuário.

- `UsuarioRepositorio`: Implementação da interface `IUsuarioRepositorio` que utiliza o DbContext para interagir com o banco de dados.

## 6. Configuração do banco de dados

Utilizamos o banco de dados PostgreSQL para armazenar os dados da aplicação. A string de conexão é configurada no arquivo appsettings.json e é utilizada pelo Entity Framework Core para conectar-se ao banco de dados.

## 7. Enums

Enums são utilizados para representar valores fixos que podem ser atribuídos a uma propriedade. No nosso caso, temos o enum `StatusTarefa` para representar o status de uma tarefa.

## 8. Mapeamento das entidades

O mapeamento das entidades é feito usando o Fluent API do Entity Framework Core. As classes de mapeamento (`UsuarioMap` e `TarefaMap`) definem as configurações de mapeamento para cada entidade.

## 9. Gerar migração e atualizar o banco de dados

Usamos o Package Manager Console para adicionar e aplicar migrações. As migrações são usadas para criar e atualizar o esquema do banco de dados de acordo com as mudanças no modelo.

## 10. Criando um controller para gerenciar os dados

Implementamos os métodos CRUD (Create, Read, Update e Delete) no controller correspondente para gerenciar os dados de usuários e tarefas.

Este README fornece uma visão geral detalhada do projeto e orienta o desenvolvedor sobre como configurar, trabalhar e expandir a API em C#. Certifique-se de seguir os passos detalhados em cada seção para configurar e executar o projeto com sucesso.
