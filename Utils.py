def ReplaceChar(x):
    replaces = (
        ('Ã','í'),
        ('i©','é'),
        ('i¡','á'),
        ('iº','ú'),
        ('',''),
        ('i³','ó'),
        ('Â¿','¿'),
        ('â',"'"),
        ('í©','é'),
        ('í¡','á'),
        ('í±','ñ'),
        ('oÌ','ó'),
        ('í³','ó'),
        ('íº','ú'),
        ('aÌ','á'))
    
    for item in replaces:
        x = x.replace(item[0], item[1])
    return x