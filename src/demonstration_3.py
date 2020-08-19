"""
A colleague of yours keeps including incorrect JavaScript code in pull
requests. You are getting tired of parsing through their code to make sure
they've included correct brackets, braces, and parentheses.

In order to save yourself time, you decide to write a function that can parse
the code to make sure it includes the correct amount of opening and closing
characters.

We will call `(`, `{`, and `[` "openers".

We will call `)`, `}`, and `]` "closers".

Your input will be a string and your function needs to make sure that there is
a correct number of openers and closers and that they are properly nested.

Examples:

`"{ [ ] ( ) }"` should return `True`
`"{ [ ( ] ) }"` should return `False`
`"{ [ }"` should return `False`

You should be able to do this in one pass with O(n) time and O(n) space
complexity.

*Note: Remember that just making sure that each opener has a corresponding
closer is not enough. You also have to confirm that they are ordered and nested
correctly. For example, "{ [ ( ] ) }" should return False, even though each
opener can be matched to a closer.*
"""
def is_valid(code):
    # Your code here

