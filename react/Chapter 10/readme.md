# Chapter 10

* Understand difference between server and client side components.

* Network boundary seperates the server and client.

## Client

* Refers to the browser on a client's device that sends requests to a server.

  * Turns the response into something a user can interact with.

## Server

* A device in a data center that receives your requests, does some computation and returns back to client.

* Client normally has constraints so if a server renders more, can reduce amount of data sent to a client.

* Certain operations are better on certain sides.

## Network boundary

* Conceptual line between.

* In react, a developer chooses this line.

  * E.g. fetch data and render posts(using Server), then render a like button(using client).

  * E.g2. nav component by server and the links by the client.

After server components are rendered, a special React Server Component Payload (RSC) is sent to the client.
Contains:

1. Rendered result of the server components
2. Placeholders(holes) where the client components will be rendered.

## Next learning

* Fast refresh
