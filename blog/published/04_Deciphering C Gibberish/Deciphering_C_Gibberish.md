If you have ever programmed in C or C++, you might have encountered some complex variable declarations like:

`char *(*(**foo[][8])())[];`  
or  
`int (*(*foo)(void ))[3]`

Wouldn't it be great if we could just enter such complex declarations into some program and it could output its meaning in *'plain English'* ?  
For example:

Input:  
`char ** const * const x`  
Output:  
`"declare x as const pointer to const pointer to pointer to char"`

Seems like there is a program made just for this - [cdecl](http://cdecl.org/).

It can even do the opposite; that is, **[convert a declaration written in plain English to its equivalent code](http://cdecl.org/?q=declare+x+as+const+pointer+to+const+pointer+to+pointer+to+char) !**

**Tip:** If you want to learn how to understand such declarations without any help, you may refer to [this article](http://unixwiz.net/techtips/reading-cdecl.html).
