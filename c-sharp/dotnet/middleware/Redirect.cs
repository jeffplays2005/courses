// Redirection code snippet
using Microsoft.AspNetCore.Rewrite;

app.MapGet("/", () => "Welcome to Contoso!");

app.MapGet("/about", () => "About.");

// Redirects when the URL is /history -> /about
app.UseRewriter(new RewriteOptions().AddRedirect("history", "about"));
