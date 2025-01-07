#encoding: utf-8
import os, csv, sys
from extract_trait import *
    
if __name__ == "__main__":
    for tr in all_traits:
        print(tr.name)
        for eff in tr.effects:
            print(eff.__repr__(), eff.get_description())
