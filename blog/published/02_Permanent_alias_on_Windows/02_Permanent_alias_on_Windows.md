If you develop C++ programs on Windows, you might have felt the need to invoke the compiler from the command prompt itself. Its pretty easy to do so; just append the path of the compiler to the [`PATH`](https://en.wikipedia.org/wiki/PATH_%28variable%29) environment variable.  
However, if you decide to invoke it with some compiler/linker options, you'll need to do some extra work.

Unlike Linux, it is a bit tricky to create permanent aliases on Windows as it requires editing the [registry](https://en.wikipedia.org/wiki/Windows_Registry).  

Before discussing on how to do it on Windows, let me first illustrate how it is done on Linux (Ubuntu specifically):  
Suppose you want to set `c+` as an alias to `c++ -Wall -Wextra`, simply create a file in your home folder named **`.bash_aliases`** and write the following in it:  
`alias c+ = 'c++ -Wall -Wextra'`  
Instead of writing the compiler options `-Wall -Wextra` directly, I prefer writing them in a separate file and then include them by specifying its path via the `@file` option of the GCC compiler, so that I don't have to write them again in my IDE's settings.  

So, **`.bash_aliases`** now contains the following:  
`alias c+ = 'c++ @/path/to/cpp-options.txt'`  
where **`cpp-options.txt`** contains:  
`-Wall -Wextra`  

Now you can invoke the compiler by typing the following in a *`cmd`* shell:  

    c+ /path/to/source.cpp  

- - -

In Windows, the closest thing to [alias](http://en.wikipedia.org/wiki/Alias_%28command%29) is [doskey](http://en.wikipedia.org/wiki/DOSKEY). 

Just like in the Linux case, we have to somehow instruct *`cmd`* to launch the `doskey` command every time it starts.  
To do this, we need to create 2 files:  

 - **`cmd_aliases.txt`**, which will contain all the aliases:  
[gist]8e1b21f2c8bdbe599dfb679048f37fcb[/gist]  
**Note:** The `$*` option is to allow the use of other command-line options along with `c+` command. Without it, you won't be able to specify the source-code and the output executable path when invoking the compiler with `c+`.  

 - **`cmd_autorun.cmd`**, which loads all those aliases from the above file everytime *`cmd`* is invoked:  
[gist]c1f3dcbd440e0f27ec87b6195282423b[/gist]  

[I am assuming these 2 files are kept in your *`My Documents`* folder, although you can keep them in any other folder you like.]  

Now we need to specify the location of this script in the registry so that it launches automatically along with *`cmd`*.  
To do this, execute the following after pasting it to a text file and saving it with `.reg` extension:  
[gist]1ec1b9e61fe3b3ff3dee93a8bb9b3025[/gist]  

- - -
- - -

 For completeness, here are all the files which I use myself:  

[gist]a59ae8717454e896673e2d55609d7516[/gist]  
[gist]08d8e2ef27d9ab76db5d093a537ea6e5[/gist]  
[gist]9fe5d7b12e4dfc814a94342ada325b71[/gist]  
[gist]7cd684f1d2e8b29ccf985db2a0bb260d[/gist]  
