# .NET Entity Framework (EF) Core

Essentially a bridge between the database and the application. It allows you to interact with the database using C# objects instead of SQL queries. This is Object-Relational Mapping (ORM).

The `DbContext` is the gateway to interacting with the database.

In an entity class, `Id` or ` <entity name>Id` are inferred to be the primary key.

## Checking Installed .NET SDK Versions

To check what versions of .NET SDK you have installed:

```bash
dotnet --list-sdks
```

## Installations

To install the required packages for EF Core, run the following commands in the terminal:

```bash
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet add package Microsoft.EntityFrameworkCore.Design

dotnet tool install --global dotnet-ef
```

## Examples

Take the `PizzaContext.cs` file as context. Will need to add SQLite to the `Program.cs` file.

```csharp
using ContosoPizza.Data;

builder.Services.AddSqlite<PizzaContext>("Data Source=ContosoPizza.db");
```

## Migrations

Migrations are a way to update the database schema without losing data. This is useful when you need to make changes to the database schema, such as adding or removing columns, changing data types, etc.

To create a migration, run the following command in the terminal:

```bash
dotnet ef migrations add InitialCreate --context PizzaContext
```

To apply the migration to the database, run the following command in the terminal:

```bash
dotnet ef database update --context PizzaContext
```

## Creating models

To create a model, create a class that inherits from `DbContext`. This class will contain the properties that map to the database tables.

Ensure to add the following namespaces and dependencies to the class:

```csharp
using System.ComponentModel.DataAnnotations;

namespace ContosoPizza.Models;
```

The `DataAnnotations` namespace contains attributes that can be used to specify the data type, length, and other properties of the model. For example, the `Key` attribute is used to specify the primary key of the model, and the `Required` attribute is used to specify that a property is required.

```csharp
using System.ComponentModel.DataAnnotations;

[Required]
public int Id { get; set; }

[Required]
[MaxLength(100)]
public string? Name { get; set; }
```

## CRUD operations

CRUD operations are the basic operations that can be performed on a database. They are:

- Create - Insert a new record into the database.
- Read - Retrieve a record from the database.
- Update - Update an existing record in the database.
- Delete - Delete a record from the database.

### Scafolding

> Scaffolds `DbContext` and model classes by using the provided connection string.
>
> Specifies to use the `Microsoft.EntityFrameworkCore.Sqlite` database provider.
> Adapted from [Microsoft Docs](https://learn.microsoft.com/en-nz/training/modules/persist-data-ef-core/6-reverse-engineering)

```bash
dotnet ef dbcontext scaffold "Data Source=Promotions/Promotions.db" Microsoft.EntityFrameworkCore.Sqlite --context-dir Data --output-dir Models
```

Would generate

```csharp
using System;
using System.Collections.Generic;

namespace ContosoPizza.Models
{
    public partial class Coupon
    {
        public int Id { get; set; }
        public string Description { get; set; } = null!;
        public DateOnly? Expiration { get; set; }
    }
}
```
