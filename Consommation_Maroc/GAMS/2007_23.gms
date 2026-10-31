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
alphaSud(I)
alphaR4(I)
alphaR5(I)
alphaR6(I)
alphaR7(I)
alphaR8(I)
alphaR9(I)
alphaR10(I)
alphaR11(I)
alphaR12(I)
alphaR13(I)
alphaR14(I)
alphaR15(I)
alphaR16(I)
betaRural(I)
betaUrbain(I)
betaFeminin(I)
betaMasculin(I)
betaSud(I)
betaR4(I)
betaR5(I)
betaR6(I)
betaR7(I)
betaR8(I)
betaR9(I)
betaR10(I)
betaR11(I)
betaR12(I)
betaR13(I)
betaR14(I)
betaR15(I)
betaR16(I)
;

PARAMETER
alphadata(*,*);

$CALL GDXXRW.EXE "GAMS_2007_DETAIL.xlsx" par=alphadata rng=alpha!A1:S24 Rdim=1 Cdim=1
$GDXIN GAMS_2007_DETAIL.gdx
$LOAD alphadata
$GDXIN

alphaRural(I) = alphadata(I, "Rural") ;
alphaUrbain(I) = alphadata(I, "Urbain") ;
alphaFeminin(I) = alphadata(I, "Feminin") ;
alphaMasculin(I) = alphadata(I, "Masculin") ;
alphaSud(I) = alphadata(I, "Sud") ;
alphaR4(I) = alphadata(I, "R4") ;
alphaR5(I) = alphadata(I, "R5") ;
alphaR6(I) = alphadata(I, "R6") ;
alphaR7(I) = alphadata(I, "R7") ;
alphaR8(I) = alphadata(I, "R8") ;
alphaR9(I) = alphadata(I, "R9") ;
alphaR10(I) = alphadata(I, "R10") ;
alphaR11(I) = alphadata(I, "R11") ;
alphaR12(I) = alphadata(I, "R12") ;
alphaR13(I) = alphadata(I, "R13") ;
alphaR14(I) = alphadata(I, "R14") ;
alphaR15(I) = alphadata(I, "R15") ;
alphaR16(I) = alphadata(I, "R16") ;

PARAMETER
betadata(*,*);

$CALL GDXXRW.EXE "GAMS_2007_DETAIL.xlsx" par=betadata rng=beta!A1:S24 Rdim=1 Cdim=1
$GDXIN GAMS_2007_DETAIL.gdx
$LOAD betadata
$GDXIN

betaRural(I) = betadata(I, "Rural") ;
betaUrbain(I) = betadata(I, "Urbain") ;
betaFeminin(I) = betadata(I, "Feminin") ;
betaMasculin(I) = betadata(I, "Masculin") ;
betaSud(I) = betadata(I, "Sud") ;
betaR4(I) = betadata(I, "R4") ;
betaR5(I) = betadata(I, "R5") ;
betaR6(I) = betadata(I, "R6") ;
betaR7(I) = betadata(I, "R7") ;
betaR8(I) = betadata(I, "R8") ;
betaR9(I) = betadata(I, "R9") ;
betaR10(I) = betadata(I, "R10") ;
betaR11(I) = betadata(I, "R11") ;
betaR12(I) = betadata(I, "R12") ;
betaR13(I) = betadata(I, "R13") ;
betaR14(I) = betadata(I, "R14") ;
betaR15(I) = betadata(I, "R15") ;
betaR16(I) = betadata(I, "R16") ;

display
alphaRural
alphaUrbain
alphaFeminin
alphaMasculin
alphaSud
alphaR4
alphaR5
alphaR6
alphaR7
alphaR8
alphaR9
alphaR10
alphaR11
alphaR12
alphaR13
alphaR14
alphaR15
alphaR16
betaRural
betaUrbain
betaFeminin
betaMasculin
betaSud
betaR4
betaR5
betaR6
betaR7
betaR8
betaR9
betaR10
betaR11
betaR12
betaR13
betaR14
betaR15
betaR16;

variables
VCminRural(I)
VCminUrbain(I)
VCminFeminin(I)
VCminMasculin(I)
VCminSud(I)
VCminR4(I)
VCminR5(I)
VCminR6(I)
VCminR7(I)
VCminR8(I)
VCminR9(I)
VCminR10(I)
VCminR11(I)
VCminR12(I)
VCminR13(I)
VCminR14(I)
VCminR15(I)
VCminR16(I)
;

equations
eqCMINRural
eqCMINUrbain
eqCMINFeminin
eqCMINMasculin
eqCMINSud
eqCMINR4
eqCMINR5
eqCMINR6
eqCMINR7
eqCMINR8
eqCMINR9
eqCMINR10
eqCMINR11
eqCMINR12
eqCMINR13
eqCMINR14
eqCMINR15
eqCMINR16
;
eqCMINRural(I).. VCminRural(I) - sum[J, -alphaRural(J)*VCminRural(J)] =e= betaRural(I);
eqCMINUrbain(I).. VCminUrbain(I) - sum[J, -alphaUrbain(J)*VCminUrbain(J)] =e= betaUrbain(I);
eqCMINFeminin(I).. VCminFeminin(I) - sum[J, -alphaFeminin(J)*VCminFeminin(J)] =e= betaFeminin(I);
eqCMINMasculin(I).. VCminMasculin(I) - sum[J, -alphaMasculin(J)*VCminMasculin(J)] =e= betaMasculin(I);
eqCMINSud(I).. VCminSud(I) - sum[J, -alphaSud(J)*VCminSud(J)] =e= betaSud(I);
eqCMINR4(I).. VCminR4(I) - sum[J, -alphaR4(J)*VCminR4(J)] =e= betaR4(I);
eqCMINR5(I).. VCminR5(I) - sum[J, -alphaR5(J)*VCminR5(J)] =e= betaR5(I);
eqCMINR6(I).. VCminR6(I) - sum[J, -alphaR6(J)*VCminR6(J)] =e= betaR6(I);
eqCMINR7(I).. VCminR7(I) - sum[J, -alphaR7(J)*VCminR7(J)] =e= betaR7(I);
eqCMINR8(I).. VCminR8(I) - sum[J, -alphaR8(J)*VCminR8(J)] =e= betaR8(I);
eqCMINR9(I).. VCminR9(I) - sum[J, -alphaR9(J)*VCminR9(J)] =e= betaR9(I);
eqCMINR10(I).. VCminR10(I) - sum[J, -alphaR10(J)*VCminR10(J)] =e= betaR10(I);
eqCMINR11(I).. VCminR11(I) - sum[J, -alphaR11(J)*VCminR11(J)] =e= betaR11(I);
eqCMINR12(I).. VCminR12(I) - sum[J, -alphaR12(J)*VCminR12(J)] =e= betaR12(I);
eqCMINR13(I).. VCminR13(I) - sum[J, -alphaR13(J)*VCminR13(J)] =e= betaR13(I);
eqCMINR14(I).. VCminR14(I) - sum[J, -alphaR14(J)*VCminR14(J)] =e= betaR14(I);
eqCMINR15(I).. VCminR15(I) - sum[J, -alphaR15(J)*VCminR15(J)] =e= betaR15(I);
eqCMINR16(I).. VCminR16(I) - sum[J, -alphaR16(J)*VCminR16(J)] =e= betaR16(I);

option limrow = 10000 ;
OPTION NLP = conopt4 ;

MODEL LESmodelRural "Modele estimation equation LES" /eqCMINRural/;
MODEL LESmodelUrbain "Modele estimation equation LES" /eqCMINUrbain/;
MODEL LESmodelFeminin "Modele estimation equation LES" /eqCMINFeminin/;
MODEL LESmodelMasculin "Modele estimation equation LES" /eqCMINMasculin/;
MODEL LESmodelSud "Modele estimation equation LES" /eqCMINSud/;
MODEL LESmodelR4 "Modele estimation equation LES" /eqCMINR4/;
MODEL LESmodelR5 "Modele estimation equation LES" /eqCMINR5/;
MODEL LESmodelR6 "Modele estimation equation LES" /eqCMINR6/;
MODEL LESmodelR7 "Modele estimation equation LES" /eqCMINR7/;
MODEL LESmodelR8 "Modele estimation equation LES" /eqCMINR8/;
MODEL LESmodelR9 "Modele estimation equation LES" /eqCMINR9/;
MODEL LESmodelR10 "Modele estimation equation LES" /eqCMINR10/;
MODEL LESmodelR11 "Modele estimation equation LES" /eqCMINR11/;
MODEL LESmodelR12 "Modele estimation equation LES" /eqCMINR12/;
MODEL LESmodelR13 "Modele estimation equation LES" /eqCMINR13/;
MODEL LESmodelR14 "Modele estimation equation LES" /eqCMINR14/;
MODEL LESmodelR15 "Modele estimation equation LES" /eqCMINR15/;
MODEL LESmodelR16 "Modele estimation equation LES" /eqCMINR16/;

LESmodelRural.HOLDFIXED = 1;
LESmodelUrbain.HOLDFIXED = 1;
LESmodelFeminin.HOLDFIXED = 1;
LESmodelMasculin.HOLDFIXED = 1;
LESmodelSud.HOLDFIXED = 1;
LESmodelR4.HOLDFIXED = 1;
LESmodelR5.HOLDFIXED = 1;
LESmodelR6.HOLDFIXED = 1;
LESmodelR7.HOLDFIXED = 1;
LESmodelR8.HOLDFIXED = 1;
LESmodelR9.HOLDFIXED = 1;
LESmodelR10.HOLDFIXED = 1;
LESmodelR11.HOLDFIXED = 1;
LESmodelR12.HOLDFIXED = 1;
LESmodelR13.HOLDFIXED = 1;
LESmodelR14.HOLDFIXED = 1;
LESmodelR15.HOLDFIXED = 1;
LESmodelR16.HOLDFIXED = 1;

SOLVE LESmodelRural USING CNS;
SOLVE LESmodelUrbain USING CNS;
SOLVE LESmodelFeminin USING CNS;
SOLVE LESmodelMasculin USING CNS;
SOLVE LESmodelSud USING CNS;
SOLVE LESmodelR4 USING CNS;
SOLVE LESmodelR5 USING CNS;
SOLVE LESmodelR6 USING CNS;
SOLVE LESmodelR7 USING CNS;
SOLVE LESmodelR8 USING CNS;
SOLVE LESmodelR9 USING CNS;
SOLVE LESmodelR10 USING CNS;
SOLVE LESmodelR11 USING CNS;
SOLVE LESmodelR12 USING CNS;
SOLVE LESmodelR13 USING CNS;
SOLVE LESmodelR14 USING CNS;
SOLVE LESmodelR15 USING CNS;
SOLVE LESmodelR16 USING CNS;

display
VCminRural.L
VCminUrbain.L
VCminFeminin.L
VCminMasculin.L
VCminSud.L
VCminR4.L
VCminR5.L
VCminR6.L
VCminR7.L
VCminR8.L
VCminR9.L
VCminR10.L
VCminR11.L
VCminR12.L
VCminR13.L
VCminR14.L
VCminR15.L
VCminR16.L;

execute_unload ".\LES-DETAIL-2007.gdx"
alphaRural
alphaUrbain
alphaFeminin
alphaMasculin
alphaSud
alphaR4
alphaR5
alphaR6
alphaR7
alphaR8
alphaR9
alphaR10
alphaR11
alphaR12
alphaR13
alphaR14
alphaR15
alphaR16
betaRural
betaUrbain
betaFeminin
betaMasculin
betaSud
betaR4
betaR5
betaR6
betaR7
betaR8
betaR9
betaR10
betaR11
betaR12
betaR13
betaR14
betaR15
betaR16
VCminRural.L
VCminUrbain.L
VCminFeminin.L
VCminMasculin.L
VCminSud.L
VCminR4.L
VCminR5.L
VCminR6.L
VCminR7.L
VCminR8.L
VCminR9.L
VCminR10.L
VCminR11.L
VCminR12.L
VCminR13.L
VCminR14.L
VCminR15.L
VCminR16.L;

$setglobal outdir %USERPROFILE%\Downloads

$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminRural.L rng=Rural!A1

$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminUrbain.L rng=Urbain!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminFeminin.L rng=Feminin!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminMasculin.L rng=Masculin!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminSud.L rng=Sud!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR4.L rng=R4!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR5.L rng=R5!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR6.L rng=R6!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR7.L rng=R7!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR8.L rng=R8!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR9.L rng=R9!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR10.L rng=R10!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR11.L rng=R11!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR12.L rng=R12!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR13.L rng=R13!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR14.L rng=R14!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR15.L rng=R15!A1 append=1
$CALL GDXXRW.EXE .\LES-DETAIL-2007.gdx output="%outdir%\Results_DETAIL_2007.xlsx" var=VCminR16.L rng=R16!A1 append=1