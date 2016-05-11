def foo():
    print "foo"

def loo():
    try:
        print "a"
    except Exception:
        print "b"
    else: # there was no exception whatsoever
        print "c"
        return foo()
    finally:
        print "d"
        return True


print loo()
