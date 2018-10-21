from ds.dll import DLL

if __name__ == "__main__":
    l = DLL()
    #l.insert_start(3)
    #l.insert_start(2)
    #l.insert_start(1)
    l.insert_end(3)
    l.insert_end(2)
    l.insert_end(1)
    l.print_list()
    l.print_rev()

