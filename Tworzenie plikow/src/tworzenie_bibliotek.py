
import sys
class PlikNaglowkowy:
    pass
def main():
    for ar in sys.argv[0:]:
        utworz_biblioteke(ar)
def utworz_biblioteke(nazwa):
        utworz_h(nazwa)
        utworz_cpp(nazwa)
def utworz_h(nazwa):
    zawartosc_h="""
#ifndef {0}_makr
#define {0}_makr
    
class {0}
{{
    public:
        
    protected:
        
    private:
}};
    
    #endif
    """.format(nazwa)
    with open("{0}.h".format(nazwa),'w') as fh:
        fh.write(zawartosc_h)
    print("biblioteka {0}.h utworzona".format(nazwa))
def utworz_cpp(nazwa):
    zawartosc_cpp="""
#include "{0}.h"
    

""".format(nazwa)
    with open("{0}.cpp".format(nazwa),'w') as fh:
        fh.write(zawartosc_cpp)
    print("plik wykonywalny {0}.cpp utworzona".format(nazwa))
    
main()
    
        
        
