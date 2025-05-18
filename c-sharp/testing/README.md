# Test Driven Development (TDD)

Writing tests that fail before writing the code that makes them pass.

# Behavior driven development (BDD)

Writing tests that describe the behavior of the application. This is done by writing tests in a way that describes the behavior of the application in a human-readable format.

## Don't repeat yourself (DRY)

Don't repeat yourself. This is a principle that states that you should not repeat yourself in your code. This can be done by using functions, classes, and other abstractions to avoid repeating code.

"For example, let's say you're writing unit tests for different constructors, but you're reusing many of the parameters for multiple tests. You can write a test helper method that keeps all the parameter inputs in one place, so they can more easily be called and modified for all of your tests. This is an example of reducing duplication, so you don't repeat yourself." - [Microsoft Docs](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices#dont-repeat-yourself-dry)

## Testing pyramid

UI -> Acceptance -> Load -> Performance -> Integration -> Unit

- Unit - the most basic type of test, testing a single function or component.
- Integration - testing how multiple components work together.
- Performance - testing how the application performs under load, catches code that slows down your app.
- Load - testing how the application performs under load.
- Acceptance - tests criteria against the functionality of an app based on a business requirement.
- UI - testing the user interface of the application. E.g. using Playwright.
