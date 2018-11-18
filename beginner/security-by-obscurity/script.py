import os
name = "password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p"

while not ".zip" in name:
        os.system("unzip ./"+name)
        #os.system("rm "+name)
        name = name[0:len(name)-2]
    

