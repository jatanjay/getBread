def encode(strs) -> str:
    return "".join(str(len(s)) + "/" + s for s in strs)


def decode(strs):
    i = 0
    f = []
    while i < len(strs):
        slash = strs.find("/", i)  # slash position
        length = strs[i:slash]  # length to jump by
        i = length + slash + 1
        f.append(strs[slash + 1 : i])
    return f


encode(["neet", "code", "love", "you"])


"""
pretty good question, was on right path with adding a delimiter, had to encode aditional type of info: lenght of the word

what we do is add legnth + delim + word

then try to create index "i" that can jump through those things

1. find postion of slash
find takes "delim", starting postion, end_postion by default -- returns index

2. find length of the word in question
that will be from ith index --> slsh
done by slicicing strs[i:slash]

3. update index by adding length + slash + 1 (since zero indexed!)

4. splice string by strs[from slash's + 1: updated index]

"""
