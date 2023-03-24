for i in lines[1:]:
            i=i.split(",")
            if i[1] in d:
                # incrementing the counr
                d[i[1]] += 1
            else:
                # initializing the count
                d[i[1]] = 1
        print(d)