
from django.contrib.gis.db import models

class LAdresseEtat(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LAvancement(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LBaieType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

 
 

class Lbpracco(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LbptypeLog(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LbptypePhy(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LCableType(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LCassetteType(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LClimType(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LDocTab(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LDocType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LEtatType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LFoColor(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LFoType(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LGeolocClasse(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LGeolocMode(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LImmeubleType(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LImplantationType(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LNoeudType(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LNroEtat(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LNroType(models.Model):
    code = models.CharField(max_length=7, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class LOccupationType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LPositionFonction(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LPositionType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LProprieteType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LReferenceEtat(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LReferenceType(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LSiteEmissionType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LSiteTypeLog(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LSiteTypePhy(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class LSroEtat(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LSroEmplacement(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class LStatut(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LSufRacco(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LSufType(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LTiroirType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class LTube(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class LZoneDensite(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LTechnologieType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class TNoeud(models.Model):
    nd_code = models.CharField(max_length=254, primary_key=True)
    nd_codeext = models.CharField(max_length=254, blank=True, null=True)
    nd_nom = models.CharField(max_length=254, blank=True, null=True)
    nd_coderat = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    nd_r1_code = models.CharField(max_length=100, blank=True, null=True)
    nd_r2_code = models.CharField(max_length=100, blank=True, null=True)
    nd_r3_code = models.CharField(max_length=100, blank=True, null=True)
    nd_r4_code = models.CharField(max_length=100, blank=True, null=True)
    nd_voie = models.CharField(max_length=254, blank=True, null=True)
    nd_type = models.ForeignKey(LNoeudType, on_delete=models.SET_NULL, null=True)
    nd_type_ep = models.ForeignKey(LTechnologieType, on_delete=models.SET_NULL, null=True)
    nd_comment = models.CharField(max_length=254, blank=True, null=True)
    nd_dtclass = models.ForeignKey(LGeolocClasse, on_delete=models.SET_NULL, null=True)
    nd_geolqlt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nd_geolmod = models.ForeignKey(LGeolocMode, on_delete=models.SET_NULL, null=True)
    nd_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    nd_creadat = models.DateTimeField(auto_now_add=True)
    nd_majdate = models.DateTimeField(auto_now=True)
    nd_majsrc = models.CharField(max_length=254, blank=True, null=True)
    nd_abddate = models.DateField(blank=True, null=True)
    nd_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(srid=3857)




class LPtechNature(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class LInfraNature(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

class LPassageType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

class LPoseType(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

class LInfraTypeLog(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)




class LConduiteType(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)



class LQualiteInfo(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

class LMasqueFace(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)










class LPtechNature(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

class LPtechTypeLog(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)

class LPtechTypePhy(models.Model):
    code = models.CharField(max_length=1, primary_key=True)
    libelle = models.CharField(max_length=254)
    definition = models.CharField(max_length=254)


class TPtech(models.Model):
    pt_code = models.CharField(max_length=254, primary_key=True)
    pt_codeext = models.CharField(max_length=254, null=True)
    pt_etiquet = models.CharField(max_length=254, null=True)
    pt_nd_code = models.CharField(max_length=254)
    pt_ad_code = models.CharField(max_length=254, null=True)
    pt_gest_do = models.CharField(max_length=20, null=True)
    pt_prop_do = models.CharField(max_length=20, null=True)
    pt_prop = models.CharField(max_length=20, null=True)
    pt_gest = models.CharField(max_length=20, null=True)
    pt_user = models.CharField(max_length=20, null=True)
    pt_proptyp = models.CharField(max_length=3, null=True)
    pt_statut = models.CharField(max_length=3)
    pt_etat = models.CharField(max_length=3, null=True)
    pt_dateins = models.DateField(null=True)
    pt_datemes = models.DateField(null=True)
    pt_avct = models.CharField(max_length=1, null=True)
    pt_typephy = models.ForeignKey(LPtechTypePhy, on_delete=models.SET_NULL)
    pt_typelog = models.ForeignKey(LPtechTypeLog, on_delete=models.SET_NULL)
    pt_rf_code = models.CharField(max_length=254, null=True)
    pt_nature = models.ForeignKey(LPtechNature, on_delete=models.SET_NULL)
    pt_secu = models.BooleanField(null=True)
    pt_occp = models.CharField(max_length=10, null=True)
    pt_a_dan = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    pt_a_dtetu = models.DateField(null=True)
    pt_a_struc = models.CharField(max_length=100, null=True)
    pt_a_haut = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    pt_a_passa = models.BooleanField(null=True)
    pt_a_strat = models.BooleanField(null=True)
    pt_rotatio = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    pt_detec = models.BooleanField(null=True)
    pt_comment = models.CharField(max_length=254, null=True)
    pt_creadat = models.DateTimeField(null=True)
    pt_majdate = models.DateTimeField(null=True)
    pt_majsrc = models.CharField(max_length=254, null=True)
    pt_abddate = models.DateField(null=True)
    pt_abdsrc = models.CharField(max_length=254, null=True)





class TAdresse(models.Model):
    ad_code = models.CharField(max_length=254, primary_key=True)
    ad_ban_id = models.CharField(max_length=24, blank=True, null=True)
    ad_nomvoie = models.CharField(max_length=254, blank=True, null=True)
    ad_fantoir = models.CharField(max_length=10, blank=True, null=True)
    ad_numero = models.IntegerField(blank=True, null=True)
    ad_rep = models.CharField(max_length=20, blank=True, null=True)
    ad_insee = models.CharField(max_length=6, blank=True, null=True)
    ad_postal = models.CharField(max_length=20, blank=True, null=True)
    ad_alias = models.CharField(max_length=254, blank=True, null=True)
    ad_nom_ld = models.CharField(max_length=254, blank=True, null=True)
    ad_x_ban = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    ad_y_ban = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    ad_commune = models.CharField(max_length=254, blank=True, null=True)
    ad_section = models.CharField(max_length=5, blank=True, null=True)
    ad_idpar = models.CharField(max_length=20, blank=True, null=True)
    ad_x_parc = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    ad_y_parc = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    ad_nat = models.BooleanField(blank=True, null=True)
    ad_nblhab = models.IntegerField(blank=True, null=True)
    ad_nblpro = models.IntegerField(blank=True, null=True)
    ad_nbprhab = models.IntegerField(blank=True, null=True)
    ad_nbprpro = models.IntegerField(blank=True, null=True)
    ad_rivoli = models.CharField(max_length=254, blank=True, null=True)
    ad_hexacle = models.CharField(max_length=254, blank=True, null=True)
    ad_hexaclv = models.CharField(max_length=254, blank=True, null=True)
    ad_distinf = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    ad_isole = models.BooleanField(blank=True, null=True)
    ad_prio = models.BooleanField(blank=True, null=True)
    ad_racc = models.ForeignKey(LImplantationType, on_delete=models.SET_NULL, blank=True, null=True)
    ad_batcode = models.CharField(max_length=100, blank=True, null=True)
    ad_nombat = models.CharField(max_length=254, blank=True, null=True)
    ad_ietat = models.ForeignKey(LAdresseEtat, on_delete=models.SET_NULL, blank=True, null=True)
    ad_itypeim = models.ForeignKey(LImmeubleType, on_delete=models.SET_NULL, blank=True, null=True)
    ad_imneuf = models.BooleanField(blank=True, null=True)
    ad_idatimn = models.DateField(blank=True, null=True)
    ad_prop = models.CharField(max_length=254, blank=True, null=True)
    ad_gest = models.CharField(max_length=20, blank=True, null=True)
    ad_idatsgn = models.DateField(blank=True, null=True)
    ad_iaccgst = models.BooleanField(blank=True, null=True)
    ad_idatcab = models.DateField(blank=True, null=True)
    ad_idatcom = models.DateField(blank=True, null=True)
    ad_typzone = models.ForeignKey(LZoneDensite, on_delete=models.SET_NULL, blank=True, null=True)
    ad_comment = models.CharField(max_length=254, blank=True, null=True)
    ad_geolqlt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ad_geolmod = models.ForeignKey(LGeolocMode, on_delete=models.SET_NULL, blank=True, null=True)
    ad_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    ad_creadat = models.DateTimeField(blank=True, null=True)
    ad_majdate = models.DateTimeField(blank=True, null=True)
    ad_majsrc = models.CharField(max_length=254, blank=True, null=True)
    ad_abddate = models.DateField(blank=True, null=True)
    ad_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    geom = models.PointField(srid=3857)




class TOrganisme(models.Model):
    or_code = models.CharField(max_length=20, primary_key=True)
    or_siren = models.CharField(max_length=9, blank=True, null=True)
    or_nom = models.CharField(max_length=254)
    or_type = models.CharField(max_length=254, blank=True, null=True)
    or_activ = models.CharField(max_length=254, blank=True, null=True)
    or_l331 = models.CharField(max_length=254, blank=True, null=True)
    or_siret = models.CharField(max_length=14, blank=True, null=True)
    or_nometab = models.CharField(max_length=254, blank=True, null=True)
    or_ad_code = models.ForeignKey(TAdresse, on_delete=models.SET_NULL, blank=True, null=True)
    or_nomvoie = models.CharField(max_length=254, blank=True, null=True)
    or_numero = models.IntegerField(blank=True, null=True)
    or_rep = models.CharField(max_length=20, blank=True, null=True)
    or_local = models.CharField(max_length=254, blank=True, null=True)
    or_postal = models.CharField(max_length=20, blank=True, null=True)
    or_commune = models.CharField(max_length=254, blank=True, null=True)
    or_telfixe = models.CharField(max_length=20, blank=True, null=True)
    or_mail = models.CharField(max_length=254, blank=True, null=True)
    or_comment = models.CharField(max_length=254, blank=True, null=True)
    or_creadat = models.DateTimeField(auto_now_add=True)
    or_majdate = models.DateTimeField(auto_now=True)
    or_majsrc = models.CharField(max_length=254, blank=True, null=True)
    or_abddate = models.DateField(blank=True, null=True)
    or_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TReference(models.Model):
    rf_code = models.CharField(max_length=254, primary_key=True)
    rf_type = models.ForeignKey(LReferenceType, on_delete=models.SET_NULL, null=True)
    rf_fabric = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    rf_design = models.CharField(max_length=254, blank=True, null=True)
    rf_etat = models.ForeignKey(LReferenceEtat, on_delete=models.SET_NULL, null=True)
    rf_comment = models.CharField(max_length=254, blank=True, null=True)
    rf_creadat = models.DateTimeField(auto_now_add=True)
    rf_majdate = models.DateTimeField(auto_now=True)
    rf_majsrc = models.CharField(max_length=254, blank=True, null=True)
    rf_abddate = models.DateField(blank=True, null=True)
    rf_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TZnro(models.Model):
    zn_code = models.CharField(max_length=254, primary_key=True)
    zn_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL)
    zn_r1_code = models.CharField(max_length=100, blank=True, null=True)
    zn_r2_code = models.CharField(max_length=100, blank=True, null=True)
    zn_r3_code = models.CharField(max_length=100, blank=True, null=True)
    zn_r4_code = models.CharField(max_length=100, blank=True, null=True)
    zn_nroref = models.CharField(max_length=15, blank=True, null=True)
    zn_nrotype = models.ForeignKey(LNroType, on_delete=models.SET_NULL)
    zn_etat = models.ForeignKey(LNroEtat, on_delete=models.SET_NULL)
    zn_etatlpm = models.ForeignKey(LNroEtat, on_delete=models.SET_NULL)
    zn_datelpm = models.DateField(blank=True, null=True)
    zn_comment = models.CharField(max_length=254, blank=True, null=True)
    zn_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    zn_creadat = models.DateTimeField(auto_now_add=True)
    zn_majdate = models.DateTimeField(auto_now=True)
    zn_majsrc = models.CharField(max_length=254, blank=True, null=True)
    zn_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    zn_abddate = models.DateField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857)


class TZsro(models.Model):
    zs_code = models.CharField(max_length=254, primary_key=True)
    zs_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL)
    zs_zn_code = models.ForeignKey(TZnro, on_delete=models.SET_NULL, null=True, blank=True)
    zs_r1_code = models.CharField(max_length=100, blank=True, null=True)
    zs_r2_code = models.CharField(max_length=100, blank=True, null=True)
    zs_r3_code = models.CharField(max_length=100, blank=True, null=True)
    zs_r4_code = models.CharField(max_length=100, blank=True, null=True)
    zs_refpm = models.CharField(max_length=20, blank=True, null=True)
    zs_etatpm = models.ForeignKey(LSroEtat, on_delete=models.SET_NULL, null=True, blank=True)
    zs_dateins = models.DateField(blank=True, null=True)
    zs_typeemp = models.ForeignKey(LSroEmplacement, on_delete=models.SET_NULL, null=True, blank=True)
    zs_capamax = models.IntegerField(blank=True, null=True)
    zs_ad_code = models.ForeignKey(TAdresse, on_delete=models.SET_NULL, null=True, blank=True)
    zs_typeing = models.CharField(max_length=254, blank=True, null=True)
    zs_nblogmt = models.IntegerField(blank=True, null=True)
    zs_nbcolmt = models.IntegerField(blank=True, null=True)
    zs_datcomr = models.DateField(blank=True, null=True)
    zs_actif = models.BooleanField(blank=True, null=True)
    zs_datemad = models.DateField(blank=True, null=True)
    zs_accgest = models.BooleanField(blank=True, null=True)
    zs_brassoi = models.BooleanField(blank=True, null=True)
    zs_comment = models.CharField(max_length=254, blank=True, null=True)
    zs_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    zs_creadat = models.DateTimeField(auto_now_add=True)
    zs_majdate = models.DateTimeField(auto_now=True)
    zs_majsrc = models.CharField(max_length=254, blank=True, null=True)
    zs_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    zs_abddate = models.DateField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857)


class TZpbo(models.Model):
    zp_code = models.CharField(max_length=254, primary_key=True)
    zp_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL)
    zp_zs_code = models.ForeignKey(TZsro, on_delete=models.SET_NULL, null=True, blank=True)
    zp_r1_code = models.CharField(max_length=100, blank=True, null=True)
    zp_r2_code = models.CharField(max_length=100, blank=True, null=True)
    zp_r3_code = models.CharField(max_length=100, blank=True, null=True)
    zp_r4_code = models.CharField(max_length=100, blank=True, null=True)
    zp_capamax = models.IntegerField(blank=True, null=True)
    zp_comment = models.CharField(max_length=254, blank=True, null=True)
    zp_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    zp_creadat = models.DateTimeField(auto_now_add=True)
    zp_majdate = models.DateTimeField(auto_now=True)
    zp_majsrc = models.CharField(max_length=254, blank=True, null=True)
    zp_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    zp_abddate = models.DateField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857)


class TZdep(models.Model):
    zd_code = models.CharField(max_length=254, primary_key=True)
    zd_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, null=True)
    zd_zs_code = models.ForeignKey(TZsro, on_delete=models.SET_NULL, null=True)
    zd_r1_code = models.CharField(max_length=100, blank=True, null=True)
    zd_r2_code = models.CharField(max_length=100, blank=True, null=True)
    zd_r3_code = models.CharField(max_length=100, blank=True, null=True)
    zd_r4_code = models.CharField(max_length=100, blank=True, null=True)
    zd_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, related_name='zd_prop', null=True)
    zd_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, related_name='zd_gest', null=True)
    zd_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL)
    zd_comment = models.CharField(max_length=254, blank=True, null=True)
    zd_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    zd_creadat = models.DateTimeField(auto_now_add=True)
    zd_majdate = models.DateTimeField(auto_now=True)
    zd_majsrc = models.CharField(max_length=254, blank=True, null=True)
    zd_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    zd_abddate = models.DateField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857)


class TZcoax(models.Model):
    zc_code = models.CharField(max_length=254, primary_key=True)
    zc_codeext = models.CharField(max_length=254, blank=True, null=True)
    zc_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, null=True)
    zc_r1_code = models.CharField(max_length=100, blank=True, null=True)
    zc_r2_code = models.CharField(max_length=100, blank=True, null=True)
    zc_r3_code = models.CharField(max_length=100, blank=True, null=True)
    zc_r4_code = models.CharField(max_length=100, blank=True, null=True)
    zc_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    zc_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    zc_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL, null=True)
    zc_comment = models.CharField(max_length=254, blank=True, null=True)
    zc_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    zc_creadat = models.DateTimeField(blank=True, null=True)
    zc_majdate = models.DateTimeField(blank=True, null=True)
    zc_majsrc = models.CharField(max_length=254, blank=True, null=True)
    zc_abddate = models.DateField(blank=True, null=True)
    zc_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857)




    

class TSitetech(models.Model):
    st_code = models.CharField(max_length=254, primary_key=True)
    st_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, null=True)
    st_codeext = models.CharField(max_length=254, blank=True, null=True)
    st_nom = models.CharField(max_length=254, blank=True, null=True)
    st_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    st_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    st_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    st_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL, null=True)
    st_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL, null=True)
    st_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    st_dateins = models.DateField(blank=True, null=True)
    st_datemes = models.DateField(blank=True, null=True)
    st_avct = models.ForeignKey(LAvancement, on_delete=models.SET_NULL, null=True)
    st_typephy = models.ForeignKey(LSiteTypePhy, on_delete=models.SET_NULL, null=True)
    st_typelog = models.ForeignKey(LSiteTypeLog, on_delete=models.SET_NULL, null=True)
    st_nblines = models.IntegerField(blank=True, null=True)
    st_ad_code = models.ForeignKey(TAdresse, on_delete=models.SET_NULL, null=True)
    st_comment = models.CharField(max_length=254, blank=True, null=True)
    st_creadat = models.DateTimeField(blank=True, null=True)
    st_majdate = models.DateTimeField(blank=True, null=True)
    st_majsrc = models.CharField(max_length=254, blank=True, null=True)
    st_abddate = models.DateField(blank=True, null=True)
    st_abdsrc = models.CharField(max_length=254, blank=True, null=True)



class TLtech(models.Model):
    lt_code = models.CharField(max_length=254, primary_key=True)
    lt_codeext = models.CharField(max_length=254, blank=True, null=True)
    lt_etiquet = models.CharField(max_length=20, blank=True, null=True)
    lt_st_code = models.ForeignKey(TSitetech, on_delete=models.SET_NULL, null=True)
    lt_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    lt_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    lt_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    lt_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL, null=True)
    lt_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL, null=True)
    lt_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    lt_dateins = models.DateField(blank=True, null=True)
    lt_datemes = models.DateField(blank=True, null=True)
    lt_local = models.CharField(max_length=254, blank=True, null=True)
    lt_elec = models.BooleanField(default=False)
    lt_clim = models.ForeignKey(LClimType, on_delete=models.SET_NULL, null=True)
    lt_occp = models.ForeignKey(LOccupationType, on_delete=models.SET_NULL, null=True)
    lt_idmajic = models.CharField(max_length=254, blank=True, null=True)
    lt_comment = models.CharField(max_length=254, blank=True, null=True)
    lt_creadat = models.DateTimeField(auto_now_add=True)
    lt_majdate = models.DateTimeField(auto_now=True)
    lt_majsrc = models.CharField(max_length=254, blank=True, null=True)
    lt_abddate = models.DateField(blank=True, null=True)
    lt_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TBaie(models.Model):
    ba_code = models.CharField(max_length=254, primary_key=True)
    ba_codeext = models.CharField(max_length=254, blank=True, null=True)
    ba_etiquet = models.CharField(max_length=254, blank=True, null=True)
    ba_lt_code = models.ForeignKey(TLtech, on_delete=models.SET_NULL, null=True)
    ba_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    ba_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    ba_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    ba_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL, null=True)
    ba_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL, null=True)
    ba_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    ba_rf_code = models.ForeignKey(TReference, on_delete=models.SET_NULL, null=True)
    ba_type = models.ForeignKey(LBaieType, on_delete=models.SET_NULL, null=True)
    ba_nb_u = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ba_haut = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ba_larg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ba_prof = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ba_comment = models.CharField(max_length=254, blank=True, null=True)
    ba_creadat = models.DateTimeField(auto_now_add=True)
    ba_majdate = models.DateTimeField(auto_now=True)
    ba_majsrc = models.CharField(max_length=254, blank=True, null=True)
    ba_abddate = models.DateField(blank=True, null=True)
    ba_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TTiroir(models.Model):
    ti_code = models.CharField(max_length=254, primary_key=True)
    ti_codeext = models.CharField(max_length=254, blank=True, null=True)
    ti_etiquet = models.CharField(max_length=254, blank=True, null=True)
    ti_ba_code = models.ForeignKey(TBaie, on_delete=models.SET_NULL, null=True)
    ti_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    ti_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    ti_type = models.ForeignKey(LTiroirType, on_delete=models.SET_NULL, null=True)
    ti_rf_code = models.ForeignKey(TReference, on_delete=models.SET_NULL, null=True)
    ti_taille = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ti_placemt = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    ti_localis = models.CharField(max_length=254, blank=True, null=True)
    ti_comment = models.CharField(max_length=254, blank=True, null=True)
    ti_creadat = models.DateTimeField(auto_now_add=True)
    ti_majdate = models.DateTimeField(auto_now=True)
    ti_majsrc = models.CharField(max_length=254, blank=True, null=True)
    ti_abddate = models.DateField(blank=True, null=True)
    ti_abdsrc = models.CharField(max_length=254, blank=True, null=True)

class TEquipement(models.Model):
    eq_code = models.CharField(max_length=254, primary_key=True)
    eq_codeext = models.CharField(max_length=254, blank=True, null=True)
    eq_etiquet = models.CharField(max_length=254, blank=True, null=True)
    eq_ba_code = models.ForeignKey(TBaie, on_delete=models.SET_NULL, null=True)
    eq_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    eq_rf_code = models.ForeignKey(TReference, on_delete=models.SET_NULL, null=True)
    eq_dateins = models.DateField(blank=True, null=True)
    eq_datemes = models.DateField(blank=True, null=True)
    eq_comment = models.CharField(max_length=254, blank=True, null=True)
    eq_creadat = models.DateTimeField(auto_now_add=True)
    eq_majdate = models.DateTimeField(auto_now=True)
    eq_majsrc = models.CharField(max_length=254, blank=True, null=True)
    eq_abddate = models.DateField(blank=True, null=True)
    eq_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TSuf(models.Model):
    sf_code = models.CharField(max_length=254, primary_key=True)
    sf_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, null=True)
    sf_ad_code = models.ForeignKey(TAdresse, on_delete=models.SET_NULL, null=True)
    sf_zp_code = models.ForeignKey(TZpbo, on_delete=models.SET_NULL, null=True)
    sf_escal = models.CharField(max_length=20, blank=True, null=True)
    sf_etage = models.CharField(max_length=20, blank=True, null=True)
    sf_oper = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    sf_type = models.ForeignKey(LSufType, on_delete=models.SET_NULL, null=True)
    sf_prop = models.CharField(max_length=254, blank=True, null=True)
    sf_resid = models.CharField(max_length=254, blank=True, null=True)
    sf_local = models.CharField(max_length=254, blank=True, null=True)
    sf_racco = models.ForeignKey(LSufRacco, on_delete=models.SET_NULL, null=True)
    sf_comment = models.CharField(max_length=254, blank=True, null=True)
    sf_creadat = models.DateTimeField(auto_now_add=True)
    sf_majdate = models.DateTimeField(auto_now=True)
    sf_majsrc = models.CharField(max_length=254, blank=True, null=True)
    sf_abddate = models.DateField(blank=True, null=True)
    sf_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TEbp(models.Model):
    bp_code = models.CharField(max_length=254, primary_key=True)
    bp_etiquet = models.CharField(max_length=254, blank=True, null=True)
    bp_codeext = models.CharField(max_length=254, blank=True, null=True)
    bp_pt_code = models.ForeignKey(TPtech, on_delete=models.SET_NULL, null=True)
    bp_lt_code = models.ForeignKey(TLtech, on_delete=models.SET_NULL, null=True)
    bp_sf_code = models.ForeignKey(TSuf, on_delete=models.SET_NULL, null=True)
    bp_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    bp_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    bp_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    bp_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL, null=True)
    bp_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL)
    bp_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    bp_occp = models.ForeignKey(LOccupationType, on_delete=models.SET_NULL, null=True)
    bp_datemes = models.DateField(blank=True, null=True)
    bp_avct = models.ForeignKey(LAvancement, on_delete=models.SET_NULL, null=True)
    bp_typephy = models.ForeignKey(LbptypePhy, on_delete=models.SET_NULL, null=True)
    bp_typelog = models.ForeignKey(LbptypeLog, on_delete=models.SET_NULL)
    bp_rf_code = models.ForeignKey(TReference, on_delete=models.SET_NULL, null=True)
    bp_entrees = models.IntegerField(blank=True, null=True)
    bp_ref_kit = models.CharField(max_length=30, blank=True, null=True)
    bp_ca_nb = models.IntegerField(blank=True, null=True)
    bp_nb_pas = models.IntegerField(blank=True, null=True)
    bp_linecod = models.CharField(max_length=12, blank=True, null=True)
    bp_oc_code = models.CharField(max_length=50, blank=True, null=True)
    bp_racco = models.ForeignKey(Lbpracco, on_delete=models.SET_NULL, null=True)
    bp_comment = models.CharField(max_length=254, blank=True, null=True)
    bp_creadat = models.DateTimeField(auto_now_add=True)
    bp_majdate = models.DateTimeField(auto_now=True)
    bp_majsrc = models.CharField(max_length=254, blank=True, null=True)
    bp_abddate = models.DateField(blank=True, null=True)
    bp_abdsrc = models.CharField(max_length=254, blank=True, null=True)



class TCassette(models.Model):
    cs_code = models.CharField(max_length=254, primary_key=True)
    cs_nb_pas = models.IntegerField()
    cs_bp_code = models.ForeignKey(TEbp, on_delete=models.SET_NULL, null=True)
    cs_num = models.IntegerField()
    cs_type = models.ForeignKey(LCassetteType, on_delete=models.SET_NULL)
    cs_face = models.CharField(max_length=20)
    cs_rf_code = models.ForeignKey(TReference, on_delete=models.SET_NULL, null=True)
    cs_comment = models.CharField(max_length=254, blank=True, null=True)
    cs_creadat = models.DateTimeField(auto_now_add=True)
    cs_majdate = models.DateTimeField(auto_now=True)
    cs_majsrc = models.CharField(max_length=254, blank=True, null=True)
    cs_abddate = models.DateField(blank=True, null=True)
    cs_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TCheminement(models.Model):
    cm_code = models.CharField(max_length=254, primary_key=True)
    cm_codeext = models.CharField(max_length=254, blank=True, null=True)
    cm_ndcode1 = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, related_name='cheminements_1', null=True)
    cm_ndcode2 = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, related_name='cheminements_2', null=True)
    cm_cm1 = models.CharField(max_length=254, blank=True, null=True)
    cm_cm2 = models.CharField(max_length=254, blank=True, null=True)
    cm_r1_code = models.CharField(max_length=100, blank=True, null=True)
    cm_r2_code = models.CharField(max_length=100, blank=True, null=True)
    cm_r3_code = models.CharField(max_length=100, blank=True, null=True)
    cm_r4_code = models.CharField(max_length=100, blank=True, null=True)
    cm_voie = models.CharField(max_length=254, blank=True, null=True)
    cm_gest_do = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    cm_prop_do = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    cm_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL, null=True)
    cm_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    cm_datcons = models.DateField(blank=True, null=True)
    cm_datemes = models.DateField(blank=True, null=True)
    cm_avct = models.ForeignKey(LAvancement, on_delete=models.SET_NULL, null=True)
    cm_typelog = models.ForeignKey(LInfraTypeLog, on_delete=models.SET_NULL, null=True)
    cm_typ_imp = models.ForeignKey(LImplantationType, on_delete=models.SET_NULL, null=True)
    cm_nature = models.ForeignKey(LInfraNature, on_delete=models.SET_NULL, null=True)
    cm_compo = models.CharField(max_length=254, blank=True, null=True)
    cm_cddispo = models.IntegerField(blank=True, null=True)
    cm_fo_util = models.IntegerField(blank=True, null=True)
    cm_mod_pos = models.ForeignKey(LPoseType, on_delete=models.SET_NULL, null=True)
    cm_passage = models.ForeignKey(LPassageType, on_delete=models.SET_NULL, null=True)
    cm_revet = models.CharField(max_length=254, blank=True, null=True)
    cm_remblai = models.CharField(max_length=254, blank=True, null=True)
    cm_charge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cm_larg = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cm_fildtec = models.BooleanField(default=False)
    cm_mut_org = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    cm_long = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cm_lgreel = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cm_comment = models.CharField(max_length=254, blank=True, null=True)
    cm_dtclass = models.ForeignKey(LGeolocClasse, on_delete=models.SET_NULL, null=True)
    cm_geolqlt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cm_geolmod = models.ForeignKey(LGeolocMode, on_delete=models.SET_NULL, null=True)
    cm_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    cm_creadat = models.DateTimeField(auto_now_add=True)
    cm_majdate = models.DateTimeField(auto_now=True)
    cm_majsrc = models.CharField(max_length=254, blank=True, null=True)
    cm_abddate = models.DateField(blank=True, null=True)
    cm_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(srid=3857)



class TConduite(models.Model):
    cd_code = models.CharField(max_length=254, primary_key=True)
    cd_codeext = models.CharField(max_length=254, blank=True, null=True)
    cd_etiquet = models.CharField(max_length=254, blank=True, null=True)
    cd_cd_code = models.CharField(max_length=254, blank=True, null=True)
    cd_r1_code = models.CharField(max_length=100, blank=True, null=True)
    cd_r2_code = models.CharField(max_length=100, blank=True, null=True)
    cd_r3_code = models.CharField(max_length=100, blank=True, null=True)
    cd_r4_code = models.CharField(max_length=100, blank=True, null=True)
    cd_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True, related_name='conduites_prop')
    cd_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True, related_name='conduites_gest')
    cd_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True, related_name='conduites_user')
    cd_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL, null=True)
    cd_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL, null=True)
    cd_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL, null=True)
    cd_dateaig = models.DateField(blank=True, null=True)
    cd_dateman = models.DateField(blank=True, null=True)
    cd_datemes = models.DateField(blank=True, null=True)
    cd_avct = models.ForeignKey(LAvancement, on_delete=models.SET_NULL, null=True)
    cd_type = models.ForeignKey(LConduiteType, on_delete=models.SET_NULL,null=True)  # Adjust on_delete if needed
    cd_dia_int = models.IntegerField(blank=True, null=True)
    cd_dia_ext = models.IntegerField(blank=True, null=True)
    cd_color = models.CharField(max_length=254, blank=True, null=True)
    cd_long = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cd_nbcable = models.IntegerField(blank=True, null=True)
    cd_occup = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    cd_comment = models.CharField(max_length=254, blank=True, null=True)
    cd_creadat = models.DateTimeField(auto_now_add=True)
    cd_majdate = models.DateTimeField(auto_now=True)
    cd_majsrc = models.CharField(max_length=254, blank=True, null=True)
    cd_abddate = models.DateField(blank=True, null=True)
    cd_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TCondChem(models.Model):
    dm_cd_code = models.ForeignKey(TConduite, on_delete=models.CASCADE, related_name='condchem_conduites')
    dm_cm_code = models.ForeignKey(TCheminement, on_delete=models.CASCADE, related_name='condchem_cheminements')
    dm_creadat = models.DateTimeField(null=True)
    dm_majdate = models.DateTimeField(null=True)
    dm_majsrc = models.CharField(max_length=254, null=True)
    dm_abddate = models.DateField(null=True)
    dm_abdsrc = models.CharField(max_length=254, null=True)

    class Meta:
        # Define a composite primary key
        constraints = [
            models.UniqueConstraint(fields=['dm_cd_code', 'dm_cm_code'], name='composite_primary_key')
        ]




class TMasque(models.Model):
    mq_id = models.BigAutoField(primary_key=True)
    mq_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL)
    mq_face = models.ForeignKey(LMasqueFace, on_delete=models.SET_NULL)
    mq_col = models.IntegerField()
    mq_ligne = models.IntegerField()
    mq_cd_code = models.ForeignKey(TConduite, on_delete=models.SET_NULL, null=True, blank=True)
    mq_qualinf = models.ForeignKey(LQualiteInfo, on_delete=models.SET_NULL)
    mq_comment = models.CharField(max_length=254, blank=True, null=True)
    mq_creadat = models.DateTimeField(auto_now_add=True)
    mq_majdate = models.DateTimeField(auto_now=True)
    mq_majsrc = models.CharField(max_length=254, blank=True, null=True)
    mq_abddate = models.DateField(blank=True, null=True)
    mq_abdsrc = models.CharField(max_length=254, blank=True, null=True)



class TCable(models.Model):
    cb_code = models.CharField(max_length=254, primary_key=True)
    cb_codeext = models.CharField(max_length=254, blank=True, null=True)
    cb_etiquet = models.CharField(max_length=254, blank=True, null=True)
    cb_nd1 = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, related_name='cable_start')
    cb_nd2 = models.ForeignKey(TNoeud, on_delete=models.SET_NULL, related_name='cable_end')
    cb_r1_code = models.CharField(max_length=100, blank=True, null=True)
    cb_r2_code = models.CharField(max_length=100, blank=True, null=True)
    cb_r3_code = models.CharField(max_length=100, blank=True, null=True)
    cb_r4_code = models.CharField(max_length=100, blank=True, null=True)
    cb_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True, blank=True)
    cb_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True, blank=True)
    cb_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True, blank=True)
    cb_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL)
    cb_statut = models.ForeignKey(LStatut, on_delete=models.SET_NULL)
    cb_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL)
    cb_dateins = models.DateField(blank=True, null=True)
    cb_datemes = models.DateField(blank=True, null=True)
    cb_avct = models.ForeignKey(LAvancement, on_delete=models.SET_NULL)
    cb_tech = models.ForeignKey(LTechnologieType, on_delete=models.SET_NULL)
    cb_typephy = models.ForeignKey(LCableType, on_delete=models.SET_NULL)
    cb_typelog = models.ForeignKey(LInfraTypeLog, on_delete=models.SET_NULL)
    cb_rf_code = models.ForeignKey(TReference, on_delete=models.SET_NULL, null=True, blank=True)
    cb_capafo = models.IntegerField(blank=True, null=True)
    cb_fo_disp = models.IntegerField(blank=True, null=True)
    cb_fo_util = models.IntegerField(blank=True, null=True)
    cb_modulo = models.IntegerField(blank=True, null=True)
    cb_diam = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cb_color = models.CharField(max_length=254, blank=True, null=True)
    cb_lgreel = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cb_localis = models.CharField(max_length=254, blank=True, null=True)
    cb_comment = models.CharField(max_length=254, blank=True, null=True)
    cb_creadat = models.DateTimeField(auto_now_add=True)
    cb_majdate = models.DateTimeField(auto_now=True)
    cb_majsrc = models.CharField(max_length=254, blank=True, null=True)
    cb_abddate = models.DateField(blank=True, null=True)
    cb_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TCabCond(models.Model):
    cc_cb_code = models.ForeignKey(TCable, on_delete=models.SET_NULL)
    cc_cd_code = models.ForeignKey(TConduite, on_delete=models.SET_NULL)
    cc_creadat = models.DateTimeField(auto_now_add=True)
    cc_majdate = models.DateTimeField(auto_now=True)
    cc_majsrc = models.CharField(max_length=254, blank=True, null=True)
    cc_abddate = models.DateField(blank=True, null=True)
    cc_abdsrc = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cc_cb_code', 'cc_cd_code'], name='t_cab_cond_pk'),
        ]



class TLove(models.Model):
    lv_id = models.BigAutoField(primary_key=True)
    lv_cb_code = models.ForeignKey(TCable, on_delete=models.SET_NULL)
    lv_nd_code = models.ForeignKey(TNoeud, on_delete=models.SET_NULL)
    lv_long = models.IntegerField(blank=True, null=True)
    lv_creadat = models.DateTimeField(auto_now_add=True)
    lv_majdate = models.DateTimeField(auto_now=True)
    lv_majsrc = models.CharField(max_length=254, blank=True, null=True)
    lv_abddate = models.DateField(blank=True, null=True)
    lv_abdsrc = models.CharField(max_length=254, blank=True, null=True)




class TFibre(models.Model):
    fo_code = models.CharField(max_length=254, primary_key=True)
    fo_code_ext = models.CharField(max_length=254, blank=True, null=True)
    fo_cb_code = models.ForeignKey(TCable, on_delete=models.SET_NULL)
    fo_nincab = models.IntegerField(blank=True, null=True)
    fo_numtub = models.IntegerField(blank=True, null=True)
    fo_nintub = models.IntegerField(blank=True, null=True)
    fo_type = models.ForeignKey(LFoType, on_delete=models.SET_NULL)
    fo_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL)
    fo_color = models.ForeignKey(LFoColor, on_delete=models.SET_NULL)
    fo_reper = models.ForeignKey(LTube, on_delete=models.SET_NULL)
    fo_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL)
    fo_comment = models.CharField(max_length=254, blank=True, null=True)
    fo_creadat = models.DateTimeField(auto_now_add=True)
    fo_majdate = models.DateTimeField(auto_now=True)
    fo_majsrc = models.CharField(max_length=254, blank=True, null=True)
    fo_abddate = models.DateField(blank=True, null=True)
    fo_abdsrc = models.CharField(max_length=254, blank=True, null=True)


class TPosition(models.Model):
    ps_code = models.CharField(max_length=254, primary_key=True)
    ps_numero = models.IntegerField(blank=True, null=True)
    ps_1 = models.ForeignKey(TFibre, on_delete=models.SET_NULL, related_name='ps_1_positions', null=True)
    ps_2 = models.ForeignKey(TFibre, on_delete=models.SET_NULL, related_name='ps_2_positions', null=True)
    ps_cs_code = models.ForeignKey(TCassette, on_delete=models.SET_NULL, null=True)
    ps_ti_code = models.ForeignKey(TTiroir, on_delete=models.SET_NULL, null=True)
    ps_type = models.ForeignKey(LPositionType, on_delete=models.SET_NULL)
    ps_fonct = models.ForeignKey(LPositionFonction, on_delete=models.SET_NULL)
    ps_etat = models.ForeignKey(LEtatType, on_delete=models.SET_NULL)
    ps_preaff = models.CharField(max_length=50, blank=True, null=True)
    ps_comment = models.CharField(max_length=254, blank=True, null=True)
    ps_creadat = models.DateTimeField(auto_now_add=True)
    ps_majdate = models.DateTimeField(auto_now=True)
    ps_majsrc = models.CharField(max_length=254, blank=True, null=True)
    ps_abddate = models.DateField(blank=True, null=True)
    ps_abdsrc = models.CharField(max_length=254, blank=True, null=True)



class TRopt(models.Model):
    rt_id = models.BigAutoField(primary_key=True)
    rt_code = models.CharField(max_length=254)
    rt_code_ext = models.CharField(max_length=254, blank=True, null=True)
    rt_fo_code = models.ForeignKey(TFibre, on_delete=models.SET_NULL, null=True)
    rt_fo_ordr = models.IntegerField(blank=True, null=True)
    rt_comment = models.CharField(max_length=254, blank=True, null=True)
    rt_creadat = models.DateTimeField(auto_now_add=True)
    rt_majdate = models.DateTimeField(auto_now=True)
    rt_majsrc = models.CharField(max_length=254, blank=True, null=True)
    rt_abddate = models.DateField(blank=True, null=True)
    rt_abdsrc = models.CharField(max_length=254, blank=True, null=True)



class TSiteEmission(models.Model):
    se_code = models.CharField(max_length=254, primary_key=True)
    se_nd_code = models.CharField(max_length=254, unique=True)
    se_anfr = models.CharField(max_length=50, blank=True, null=True)
    se_prop = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, null=True)
    se_gest = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, related_name='se_gest', null=True)
    se_user = models.ForeignKey(TOrganisme, on_delete=models.SET_NULL, related_name='se_user', null=True)
    se_proptyp = models.ForeignKey(LProprieteType, on_delete=models.SET_NULL, null=True)
    se_statut = models.ForeignKey(LStatut, on_delete=models.PROTECT)
    se_etat = models.ForeignKey(LEtatType, on_delete=models.PROTECT)
    se_occp = models.ForeignKey(LOccupationType, on_delete=models.SET_NULL, null=True)
    se_dateins = models.DateField(blank=True, null=True)
    se_datemes = models.DateField(blank=True, null=True)
    se_type = models.ForeignKey(LSiteEmissionType, on_delete=models.PROTECT)
    se_haut = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    se_ad_code = models.ForeignKey(TAdresse, on_delete=models.SET_NULL, null=True)
    se_comment = models.CharField(max_length=254, blank=True, null=True)
    se_creadat = models.DateTimeField(auto_now_add=True)
    se_majdate = models.DateTimeField(auto_now=True)
    se_majsrc = models.CharField(max_length=254, blank=True, null=True)
    se_abddate = models.DateField(blank=True, null=True)
    se_abdsrc = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = 't_siteemission'
        constraints = [
            models.UniqueConstraint(fields=['se_nd_code'], name='t_siteemission_nd_code_unique'),
    
        ]




class TDocument(models.Model):
    do_code = models.CharField(max_length=254, primary_key=True)
    do_ref = models.CharField(max_length=254, unique=True)
    do_reftier = models.CharField(max_length=254, blank=True, null=True)
    do_r1_code = models.CharField(max_length=100, blank=True, null=True)
    do_r2_code = models.CharField(max_length=100, blank=True, null=True)
    do_r3_code = models.CharField(max_length=100, blank=True, null=True)
    do_r4_code = models.CharField(max_length=100, blank=True, null=True)
    do_type = models.CharField(max_length=3)
    do_indice = models.CharField(max_length=3, blank=True, null=True)
    do_date = models.DateField(blank=True, null=True)
    do_classe = models.CharField(max_length=2, blank=True, null=True)
    do_url1 = models.CharField(max_length=254, blank=True, null=True)
    do_url2 = models.CharField(max_length=254, blank=True, null=True)
    do_comment = models.CharField(max_length=254, blank=True, null=True)
    do_creadat = models.DateTimeField(auto_now_add=True)
    do_majdate = models.DateTimeField(auto_now=True)
    do_majsrc = models.CharField(max_length=254, blank=True, null=True)
    do_abddate = models.DateField(blank=True, null=True)
    do_abdsrc = models.CharField(max_length=254, blank=True, null=True)



class TDocObj(models.Model):
    od_id = models.BigAutoField(primary_key=True)
    od_do_code = models.CharField(max_length=254)
    od_tbltype = models.CharField(max_length=2)
    od_codeobj = models.CharField(max_length=254)
    od_creadat = models.DateTimeField(auto_now_add=True)
    od_majdate = models.DateTimeField(auto_now=True)
    od_majsrc = models.CharField(max_length=254, blank=True, null=True)
    od_abddate = models.DateField(blank=True, null=True)
    od_abdsrc = models.CharField(max_length=254, blank=True, null=True)

  

class TEmpreinte(models.Model):
    em_code = models.CharField(max_length=254, primary_key=True)
    em_do_code = models.CharField(max_length=254)
    em_geolsrc = models.CharField(max_length=254, blank=True, null=True)
    em_creadat = models.DateTimeField(auto_now_add=True)
    em_majdate = models.DateTimeField(auto_now=True)
    em_majsrc = models.CharField(max_length=254, blank=True, null=True)
    em_abddate = models.DateField(blank=True, null=True)
    em_abdsrc = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPolygonField(srid=3857)