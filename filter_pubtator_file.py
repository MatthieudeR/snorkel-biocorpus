
with open("data/bioconcepts2pubtator_offsets" ,"r") as f_in:
    with open("data/bioconcepts2pubtator_offsets_filtered", "w") as f_out:
        with open("pubtator_api/input/pmids.txt","r") as f_in2:
            pmids_list = set([line.strip() for line in f_in2 if len(line.strip())>0])
        line = f_in.readline()
        print("PMID list generated")
        while len(pmids_list)>0:
            while "|" not in line:
                line = f_in.readline()
            pmid_local = line.split("|")[0].strip()
            if pmid_local in pmids_list:
                print "{} remaining".format(len(pmids_list))
                pmids_list.remove(pmid_local)
                f_out.write(line)
                while(line!='\n'):
                    line = f_in.readline()
                    f_out.write(line)
            else:
                while(line!='\n'):
                    line = f_in.readline()


