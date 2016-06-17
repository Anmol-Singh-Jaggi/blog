For all the C++ developers who have ever felt the need to print different types of objects in your source code in a neat and structured format ( perhaps for debugging ), I have developed a set of [function templates](https://en.wikipedia.org/wiki/Template_%28C%2B%2B%29) to ease your pain.  

[Pretty-print.hpp](https://github.com/anmol-singh-jaggi/Pretty-print/blob/master/prettyprint.hpp "Prettyprint")  

Usage -:  

[example1.cpp](https://github.com/Anmol-Singh-Jaggi/Pretty-print/blob/master/examples/example1.cpp "example1")  
[example2.cpp](https://github.com/anmol-singh-jaggi/Pretty-print/blob/master/examples/example2.cpp "example2")  

Now, after looking at the code, you might be wondering why is the overload of `operator<<` for an array is so much different from that of the rest of the data types.  

This is because there is already an implementation of `operator<<` for arrays in C++.  
`operator<<` has two overloaded versions, one for [`const void*`](http://www.cplusplus.com/reference/ostream/ostream/operator%3C%3C/) and the other for [`const char*`](http://www.cplusplus.com/reference/ostream/ostream/operator-free/).  

A `char` array is converted to `const char*` and passed to that overload, because it fits better than to `const void*`.  
The `int` array, however, is converted to `const void*` and passed to that version.  
The version of `operator<<` taking `const void*` just outputs the address, whereas the version taking the `const char*` actually treats it like a C-string and outputs every character until the terminating null character.  

All this can be seen in action [here](https://github.com/anmol-singh-jaggi/Pretty-print/blob/master/examples/example3.cpp "example3").  

Therefore, by overloading the `operator<<` for an array, we are creating an ambiguity for the compiler.  
You can confirm it yourself by trying to compile [this](https://github.com/anmol-singh-jaggi/Pretty-print/blob/master/examples/example4.cpp "example4"), and reading the error given by the compiler in which the multiple ambiguous declarations are pointed out.  
[ **TIP** : Execute `g++ example4.cpp 2>log.txt` to redirect the compilation error to a file for convenience. ]  

We can overcome this problem using some *'template wizardry'*.  
By using the [`enable_if`](http://en.cppreference.com/w/cpp/types/enable_if) template feature to explicitly specify the types for which a function is overloaded, we can instruct the compiler to not call our custom overloaded function if the `operator<<` is called with a `char` array.
