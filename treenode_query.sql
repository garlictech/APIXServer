SELECT a."num", a."nev", a."helyszin", a."icon", a."ua_tip", a."es", a."es_vez", a."p1", a."p1_vez", a."p2", a."p2_vez", a."p3", a."p3_vez", a."p4", a."p4_vez", a."sajat", a."keszlet", a."keszlet15", a."kg", a."szazalek", a."csop", a."datumido", a."dt_num", a."suruseg", a."delete", a."zarolt_l", a."zarolt_mm", a."ua_tipn", a."a0", a."hofok", (a."max_liter" - a."keszlet") as max_liter,a.RDB$DB_KEY

from "Tartalyok" a,
    (select "nev" from "TreeNode" where (("parent0"=%(node)s)or
        ("parent1"=%(node)s)or
        ("parent2"=%(node)s)or
        ("parent3"=%(node)s)or
        ("parent4"=%(node)s)or
        ("parent5"=%(node)s)or
        ("parent6"=%(node)s)or
        ("parent7"=%(node)s)or
        ("parent8"=%(node)s)or
        ("dbindx"=%(node)s))and
        ("delete"='#39#39')and
        ("azonosito"<>'#39#39')and
        ("tipus"='#39'2'#39')and
        ("user"='%(user)sForm1.myUser')
        Group by "nev"
    ) al
    where (a."nev"=al."nev")and(a."delete"='#39#39')');
      Form1.IBQuery1.SQL.Add('order by a."nev"');
