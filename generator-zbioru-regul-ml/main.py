import warunki_logiczne
import reguly
import export
from shutil import copyfile


export.zapisz_do_pliku(reguly.utworz_reguly(warunki_logiczne.utworz_warunki()).sample(1000))

#copyfile("encje_reguly_probka_uczaca.reg","/home/projekty/git-repo/ml_workspace_kotlin/mw-kreator-regul-biznesowych/app-modul-silnik-regul/src/main/modelnlp/reguly/encje_reguly_probka_uczaca.reg")
#copyfile("encje_reguly_probka_uczaca.reg","H:/mw-git/ml_workspace_kotlin/mw-kreator-regul-biznesowych/app-modul-silnik-regul/src/main/modelnlp/reguly/encje_reguly_probka_uczaca.reg")