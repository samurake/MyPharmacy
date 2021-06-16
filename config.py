base_url = r"https://www.anm.ro/nomenclator/medicamente"
page_uri = r"?page={}"

"""
data-dencom="5 - FLUOROURACIL EBEWE 50mg/ml"
data-dci="FLUOROURACILUM"
data-formafarm="CONC. PT. SOL. INJ./PERF."
data-conc="50mg/ml"
data-codatc="L01BC02"
data-actter="ANTIMETABOLITI ANALOGI AI BAZELOR PIRIMIDINICE"
data-prescript="PR"
data-ambalaj="Cutie cu 1 flac. din sticla bruna x 5 ml concentrat pt. sol. inj./perf."
data-volumamb="5 ml"
data-valabamb="2 ani"
data-cim="W43451001"
data-firmtarp="EBEWE PHARMA GES.M.B.H. NFG. KG - AUSTRIA"
data-firmtard="EBEWE PHARMA GES.M.B.H. NFG. KG - AUSTRIA"
data-nrdtamb="7321/2015/01"
data-linkrcp="http://www.anm.ro/_/_RCP/RCP_7321_22.01.15.pdf"
data-linkpro="http://www.anm.ro/_/_PRO/PRO_7321_22.01.15.pdf"
data-linkamb="http://www.anm.ro/_/_AMB/AMB_7321_22.01.15.pdf"
"""
hraw_to_hname_data ={
    "data-dencom" : "Denumire comercială",
    "data-dci" : "DCI",
    "data-formafarm" : "Forma farmaceutică",
    "data-conc" : "Concentrația",
    "data-codatc" : "Cod ATC",
    "data-actter" : "Acțiune terapeutică",
    "data-prescript" : "Prescripție",
    "data-ambalaj" : "Ambalaj",
    "data-volumamb" : "Volum ambalaj",
    "data-valabamb" : "Valabilitate ambalaj",
    "data-cim" : "Cod CIM",
    "data-firmtarp" : "Firma / țara producătoare APP",
    "data-firmtard" : "Firma / țara deținătoare APP",
    "data-nrdtamb" : "Nr. / data ambalaj APP",
    "data-linkrcp" : "Rezumat caracteristici produs",
    "data-linkpro" : "Prospect",
    "data-linkamb" : "Ambalaj",
}
