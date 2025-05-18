# Chapter 7

React adding interactivity with state and event handlers

# Props

- Read only info
- Passed to components

## Hooks

Allows adding additional logic such as a state.
States - info that UI changes over time, usually by user
E.g. number of likes, button toggle

React hook function : `useState()`
This useState function takes a value and an update function

> [!NOTE]
> States are different to props, the data of a state can be passed as a prop but the update method shouldn't be used outside of the component that it was created in.
