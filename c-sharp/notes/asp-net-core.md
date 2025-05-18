## ASP.NET Core

Basic example:

`WebApplicationBuilder` is used to configure the app.

`MapGet` method defines a route and a handler for GET requests.

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();
```

### Using Blazor

Blazor is a component-based web UI framework, built into ASP.NET Core, used for building interactive web UIs using HTML, CSS, and C#. Essentially similar to libraries like React.

```csharp
@page "/counter"
@rendermode InteractiveServer

<PageTitle>Counter</PageTitle>

<h1>Counter</h1>

<p role="status">Current count: @currentCount</p>

<button class="btn btn-primary" @onclick="IncrementCount">Click me</button>

@code {
    private int currentCount = 0;

    private void IncrementCount()
    {
        currentCount++;
    }
}
```

The code above does the following:

- Creates a counter component
- The @code block contains the component's logic using C#, including a method to increment the counter.
- The counter value is displayed and updated each time the button is clicked.
  - Kind of like react `useState`
- A component approach allows for code reuse across different parts of the application and has the flexibility to be run either in the browser or on the server in a Blazor app.

Using the component in a web page:

```csharp
@page "/"

<PageTitle>Home</PageTitle>

<h1>Hello, world!</h1>

<Counter />
```

## Middleware

Adding middleware in the `Program.cs` file:

- `UseHttpsRedirection` enables HTTPS redirection.
- `UseRouting` enables routing to map requests to endpoints.
- `MapStaticAssets` serves static files(such as HTML, CSS, JavaScript, images and other assets) from the `wwwroot` folder.
- `UseAuthentication` enables authentication middleware.
- `UseAuthorization` enables authorization middleware.

- `MapGet` defines a route and a handler for GET requests.

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseHttpsRedirection();
app.UseRouting();
app.MapStaticAssets();
app.UseAuthentication();
app.UseAuthorization();

app.MapGet("/", () => "Hello World!");

app.Run();
```

## Dependency Injection

E.g. using **EntityFramework Core**

```csharp
public class MyDbContext : DbContext
{
    public MyDbContext(DbContextOptions<MyDbContext> options) : base(options) { }

    public DbSet<Product> Products { get; set; } = default!;
}

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<MyDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

app.Run();
```

### Configuration

`appsetting.json`

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;"
  }
}
```

In `Program.cs`, we need to specify the connection string in the `DbContext` options.:

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<MyDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

app.Run();
```
