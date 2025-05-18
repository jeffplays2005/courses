# Middleware and delegates

Take an example in `BasicExample.cs`, the output is below:

```
Hello from middleware 1. Passing to the next middleware!
Hello from middleware 2!
Hello from middleware 1 again!
```

The first middelware print statement is executed from the `app.Use` middleware, and executes the first statement, this then is passed to the `next.Invoke()` method and awaits for it to finish executing (hence 2nd statement), and then writes the 3rd statement in the same middleware.

## Custom Middleware

A custom middleware is a class that implements the `IMiddleware` interface.

Middleware can be terminal and non-terminal. A terminal middleware is one that does not call the next middleware in the pipeline, while a non-terminal middleware does.

> [!NOTE]
> Remember that the middleware is executed in the order it is added to the pipeline.

```csharp
app.Use(async (context, next) =>
{
    Console.WriteLine($"{context.Request.Method} {context.Request.Path} {context.Response.StatusCode}");
    await next();
});
```

## Built in middleware

A few example middleware functions used in `Program.cs` file:

- `app.UseExceptionHandler()` - Catches exceptions and returns to an error page.
- `app.UseAntiforgery()` - Prevents CSRF attacks by adding a token
- `app.UseHttpsRedirection()` - Redirects HTTP requests to HTTPS.
- `app.UseHsts()` - Adds HTTP Strict Transport Security (HSTS) headers to responses, which enforce secure connections.
- `app.MapStaticAssets()` - Serves static files from the wwwroot folder.
- `app.MapRazorComponents<App>()` - Maps Razor components to the app.

Additional middleware functions:

- `app.UseRouting()` enables routing to map requests to endpoints.

### Map endpoints and add a URL rewriter

```csharp
using Microsoft.AspNetCore.Rewrite;

app.MapGet("/", () => "Welcome to Contoso!");

app.MapGet("/about", () => "About.");

// Redirects when the URL is /history -> /about
app.UseRewriter(new RewriteOptions().AddRedirect("history", "about"));
```
