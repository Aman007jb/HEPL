def name_to_number(filename):
    if filename.find("1k")!=-1:
        return 1000
    elif filename.find("10k")!=-1:
        return 10000
    elif filename.find("100k")!=-1:
        return 100000
    elif filename.find("1M")!=-1:
        return 1000000
    elif filename.find("10M")!=-1:
        return 10000000
    else:
        print "event file mismatch"