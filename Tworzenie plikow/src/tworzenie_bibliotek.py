#! /usr/bin/env/pyt
import sys
class PlikNaglowkowy:
    def __init__(self,nazwa):
        self.nazwa=nazwa
        self.wzor="""
#pragma once
    //
class {0}
{{
    public:
        {0}();
        ~{0}();
    protected:
        
    private:
}};
    
    
    """.format(self.nazwa)
    
    def wykonaj(self):
        with open("{0}.h".format(self.nazwa),'w') as fh:
            fh.write(self.wzor)  
        print("biblioteka {0}.h utworzona".format(self.nazwa))  
class PlikWykonywalny:
    def __init__(self,nazwa):
        self.nazwa=nazwa
        self.wzor="""
#include "{0}.h"
   {0}::{0}()
   {{
   }}
   {0}::~{0}()
   {{
   }} 

"""
    def wykonaj(self):
        with open("{0}.cpp".format(self.nazwa),'w') as fh:
            fh.write(self.wzor.format(self.nazwa))  
        print("plik {0}.cpp utworzony".format(self.nazwa))  
class KlasaPochodna():
    def __init__(self,pochodna,podstawowa):
        self.podstawowa=podstawowa
        self.pochodna=pochodna
        self.wzor="""
#pragma once
#include "{1}.h"  
class {0}:public {1}
{{
    public:
        {0}();
        ~{0}();
    protected:
        
    private:
}};
    
    
    """.format(self.pochodna,self.podstawowa)
    def wykonaj(self):
        with open("{0}.h".format(self.pochodna),'w') as fh:
            fh.write(self.wzor)  
        print("biblioteka {0}.h utworzona".format(self.pochodna)) 
        PlikNaglowkowy(self.podstawowa).wykonaj()
        PlikWykonywalny(self.podstawowa).wykonaj()
         
def main():
    
    
    
    for ar in sys.argv[1:]:
        
        if "@" in ar:
            nazwa,pochodna=ar.split('@')
            print(nazwa,pochodna)
            generator=KlasaPochodna(nazwa,pochodna)
            print(nazwa,pochodna)
        else:
            generator=PlikNaglowkowy(ar)
            nazwa=ar
            print(ar)
        generator.wykonaj() 
        PlikWykonywalny(nazwa).wykonaj()
    
main()
    
        
        