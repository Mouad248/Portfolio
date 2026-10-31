* ============================================================
* VERSION CORRIGEE MINIMALE
* Meme style, memes noms de variables, meme methode que ton code.
* Correction uniquement des plages Excel :
*   alpha : Alpha_Beta!A1:Q24
*   beta  : Alpha_Beta!A26:Q49
* ============================================================

set I Produits detailles S1-S23
/
S1
S2
S3
S4
S5
S6
S7
S8
S9
S10
S11
S12
S13
S14
S15
S16
S17
S18
S19
S20
S21
S22
S23
/
;

ALIAS(I,J)
;

parameter
alphaRural(I)
alphaUrbain(I)
alphaFeminin(I)
alphaMasculin(I)
alphaR1(I)
alphaR2(I)
alphaR3(I)
alphaR4(I)
alphaR5(I)
alphaR6(I)
alphaR7(I)
alphaR8(I)
alphaR9(I)
alphaR10(I)
alphaR11(I)
alphaR12(I)
betaRural(I)
betaUrbain(I)
betaFeminin(I)
betaMasculin(I)
betaR1(I)
betaR2(I)
betaR3(I)
betaR4(I)
betaR5(I)
betaR6(I)
betaR7(I)
betaR8(I)
betaR9(I)
betaR10(I)
betaR11(I)
betaR12(I)
;

PARAMETER
alphadata(*,*);

$CALL GDXXRW.EXE "GAMS_2014_DETAIL.xlsx" par=alphadata rng=Alpha_Beta!A1:Q24 Rdim=1 Cdim=1
$GDXIN GAMS_2014_DETAIL.gdx
$LOAD alphadata
$GDXIN

alphaRural(I) = alphadata(I, "Rural") ;
alphaUrbain(I) = alphadata(I, "Urbain") ;
alphaFeminin(I) = alphadata(I, "Feminin") ;
alphaMasculin(I) = alphadata(I, "Masculin") ;
alphaR1(I) = alphadata(I, "R1") ;
alphaR2(I) = alphadata(I, "R2") ;
alphaR3(I) = alphadata(I, "R3") ;
alphaR4(I) = alphadata(I, "R4") ;
alphaR5(I) = alphadata(I, "R5") ;
alphaR6(I) = alphadata(I, "R6") ;
alphaR7(I) = alphadata(I, "R7") ;
alphaR8(I) = alphadata(I, "R8") ;
alphaR9(I) = alphadata(I, "R9") ;
alphaR10(I) = alphadata(I, "R10") ;
alphaR11(I) = alphadata(I, "R11") ;
alphaR12(I) = alphadata(I, "R12") ;

PARAMETER
betadata(*,*);

$CALL GDXXRW.EXE "GAMS_2014_DETAIL.xlsx" par=betadata rng=Alpha_Beta!A26:Q49 Rdim=1 Cdim=1
$GDXIN GAMS_2014_DETAIL.gdx
$LOAD betadata
$GDXIN

betaRural(I) = betadata(I, "Rural") ;
betaUrbain(I) = betadata(I, "Urbain") ;
betaFeminin(I) = betadata(I, "Feminin") ;
betaMasculin(I) = betadata(I, "Masculin") ;
betaR1(I) = betadata(I, "R1") ;
betaR2(I) = betadata(I, "R2") ;
betaR3(I) = betadata(I, "R3") ;
betaR4(I) = betadata(I, "R4") ;
betaR5(I) = betadata(I, "R5") ;
betaR6(I) = betadata(I, "R6") ;
betaR7(I) = betadata(I, "R7") ;
betaR8(I) = betadata(I, "R8") ;
betaR9(I) = betadata(I, "R9") ;
betaR10(I) = betadata(I, "R10") ;
betaR11(I) = betadata(I, "R11") ;
betaR12(I) = betadata(I, "R12") ;

display
alphaRural
alphaUrbain
alphaFeminin
alphaMasculin
alphaR1
alphaR2
alphaR3
alphaR4
alphaR5
alphaR6
alphaR7
alphaR8
alphaR9
alphaR10
alphaR11
alphaR12
betaRural
betaUrbain
betaFeminin
betaMasculin
betaR1
betaR2
betaR3
betaR4
betaR5
betaR6
betaR7
betaR8
betaR9
betaR10
betaR11
betaR12;

variables
VCminRural(I)
VCminUrbain(I)
VCminFeminin(I)
VCminMasculin(I)
VCminR1(I)
VCminR2(I)
VCminR3(I)
VCminR4(I)
VCminR5(I)
VCminR6(I)
VCminR7(I)
VCminR8(I)
VCminR9(I)
VCminR10(I)
VCminR11(I)
VCminR12(I)
;

equations
eqCMINRural
eqCMINUrbain
eqCMINFeminin
eqCMINMasculin
eqCMINR1
eqCMINR2
eqCMINR3
eqCMINR4
eqCMINR5
eqCMINR6
eqCMINR7
eqCMINR8
eqCMINR9
eqCMINR10
eqCMINR11
eqCMINR12
;
eqCMINRural(I).. VCminRural(I) - sum[J, -alphaRural(J)*VCminRural(J)] =e= betaRural(I);
eqCMINUrbain(I).. VCminUrbain(I) - sum[J, -alphaUrbain(J)*VCminUrbain(J)] =e= betaUrbain(I);
eqCMINFeminin(I).. VCminFeminin(I) - sum[J, -alphaFeminin(J)*VCminFeminin(J)] =e= betaFeminin(I);
eqCMINMasculin(I).. VCminMasculin(I) - sum[J, -alphaMasculin(J)*VCminMasculin(J)] =e= betaMasculin(I);
eqCMINR1(I).. VCminR1(I) - sum[J, -alphaR1(J)*VCminR1(J)] =e= betaR1(I);
eqCMINR2(I).. VCminR2(I) - sum[J, -alphaR2(J)*VCminR2(J)] =e= betaR2(I);
eqCMINR3(I).. VCminR3(I) - sum[J, -alphaR3(J)*VCminR3(J)] =e= betaR3(I);
eqCMINR4(I).. VCminR4(I) - sum[J, -alphaR4(J)*VCminR4(J)] =e= betaR4(I);
eqCMINR5(I).. VCminR5(I) - sum[J, -alphaR5(J)*VCminR5(J)] =e= betaR5(I);
eqCMINR6(I).. VCminR6(I) - sum[J, -alphaR6(J)*VCminR6(J)] =e= betaR6(I);
eqCMINR7(I).. VCminR7(I) - sum[J, -alphaR7(J)*VCminR7(J)] =e= betaR7(I);
eqCMINR8(I).. VCminR8(I) - sum[J, -alphaR8(J)*VCminR8(J)] =e= betaR8(I);
eqCMINR9(I).. VCminR9(I) - sum[J, -alphaR9(J)*VCminR9(J)] =e= betaR9(I);
eqCMINR10(I).. VCminR10(I) - sum[J, -alphaR10(J)*VCminR10(J)] =e= betaR10(I);
eqCMINR11(I).. VCminR11(I) - sum[J, -alphaR11(J)*VCminR11(J)] =e= betaR11(I);
eqCMINR12(I).. VCminR12(I) - sum[J, -alphaR12(J)*VCminR12(J)] =e= betaR12(I);

option limrow = 10000 ;
OPTION NLP = conopt4 ;

MODEL LESmodelRural "Modele estimation equation LES" /eqCMINRural/;
MODEL LESmodelUrbain "Modele estimation equation LES" /eqCMINUrbain/;
MODEL LESmodelFeminin "Modele estimation equation LES" /eqCMINFeminin/;
MODEL LESmodelMasculin "Modele estimation equation LES" /eqCMINMasculin/;
MODEL LESmodelR1 "Modele estimation equation LES" /eqCMINR1/;
MODEL LESmodelR2 "Modele estimation equation LES" /eqCMINR2/;
MODEL LESmodelR3 "Modele estimation equation LES" /eqCMINR3/;
MODEL LESmodelR4 "Modele estimation equation LES" /eqCMINR4/;
MODEL LESmodelR5 "Modele estimation equation LES" /eqCMINR5/;
MODEL LESmodelR6 "Modele estimation equation LES" /eqCMINR6/;
MODEL LESmodelR7 "Modele estimation equation LES" /eqCMINR7/;
MODEL LESmodelR8 "Modele estimation equation LES" /eqCMINR8/;
MODEL LESmodelR9 "Modele estimation equation LES" /eqCMINR9/;
MODEL LESmodelR10 "Modele estimation equation LES" /eqCMINR10/;
MODEL LESmodelR11 "Modele estimation equation LES" /eqCMINR11/;
MODEL LESmodelR12 "Modele estimation equation LES" /eqCMINR12/;

LESmodelRural.HOLDFIXED = 1;
LESmodelUrbain.HOLDFIXED = 1;
LESmodelFeminin.HOLDFIXED = 1;
LESmodelMasculin.HOLDFIXED = 1;
LESmodelR1.HOLDFIXED = 1;
LESmodelR2.HOLDFIXED = 1;
LESmodelR3.HOLDFIXED = 1;
LESmodelR4.HOLDFIXED = 1;
LESmodelR5.HOLDFIXED = 1;
LESmodelR6.HOLDFIXED = 1;
LESmodelR7.HOLDFIXED = 1;
LESmodelR8.HOLDFIXED = 1;
LESmodelR9.HOLDFIXED = 1;
LESmodelR10.HOLDFIXED = 1;
LESmodelR11.HOLDFIXED = 1;
LESmodelR12.HOLDFIXED = 1;

SOLVE LESmodelRural USING CNS;
SOLVE LESmodelUrbain USING CNS;
SOLVE LESmodelFeminin USING CNS;
SOLVE LESmodelMasculin USING CNS;
SOLVE LESmodelR1 USING CNS;
SOLVE LESmodelR2 USING CNS;
SOLVE LESmodelR3 USING CNS;
SOLVE LESmodelR4 USING CNS;
SOLVE LESmodelR5 USING CNS;
SOLVE LESmodelR6 USING CNS;
SOLVE LESmodelR7 USING CNS;
SOLVE LESmodelR8 USING CNS;
SOLVE LESmodelR9 USING CNS;
SOLVE LESmodelR10 USING CNS;
SOLVE LESmodelR11 USING CNS;
SOLVE LESmodelR12 USING CNS;

display
VCminRural.L
VCminUrbain.L
VCminFeminin.L
VCminMasculin.L
VCminR1.L
VCminR2.L
VCminR3.L
VCminR4.L
VCminR5.L
VCminR6.L
VCminR7.L
VCminR8.L
VCminR9.L
VCminR10.L
VCminR11.L
VCminR12.L;

execute_unload ".\LES-DETAIL-2014.gdx"
alphaRural
alphaUrbain
alphaFeminin
alphaMasculin
alphaR1
alphaR2
alphaR3
alphaR4
alphaR5
alphaR6
alphaR7
alphaR8
alphaR9
alphaR10
alphaR11
alphaR12
betaRural
betaUrbain
betaFeminin
betaMasculin
betaR1
betaR2
betaR3
betaR4
betaR5
betaR6
betaR7
betaR8
betaR9
betaR10
betaR11
betaR12
VCminRural.L
VCminUrbain.L
VCminFeminin.L
VCminMasculin.L
VCminR1.L
VCminR2.L
VCminR3.L
VCminR4.L
VCminR5.L
VCminR6.L
VCminR7.L
VCminR8.L
VCminR9.L
VCminR10.L
VCminR11.L
VCminR12.L;

$setglobal outdir %USERPROFILE%\Downloads

$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminRural.L rng=Rural!A1

$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminUrbain.L rng=Urbain!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminFeminin.L rng=Feminin!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminMasculin.L rng=Masculin!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR1.L rng=R1!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR2.L rng=R2!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR3.L rng=R3!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR4.L rng=R4!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR5.L rng=R5!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR6.L rng=R6!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR7.L rng=R7!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR8.L rng=R8!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR9.L rng=R9!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR10.L rng=R10!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR11.L rng=R11!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2014.gdx output="%outdir%\Results_DETAIL_2014.xlsx" var=VCminR12.L rng=R12!A1 append=1