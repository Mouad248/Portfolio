set I Produits nomenclature 20 NCN
/
G1
G2
G3
G4
G5
G6
G7
G8
G9
/
;


ALIAS(I,J)
;

parameter
betaRural(I)
betaUrbain(I)
betaMasculin(I)
betaFeminin(I)
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
alphaRural(I)
alphaUrbain(I)
alphaMasculin(I)
alphaFeminin(I)
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
;

PARAMETER
betadata(*,*);

$CALL GDXXRW.EXE "GAMS_2014.xlsx" par=betadata rng=Feuil1!A1:Q10 Rdim=1 Cdim=1
$GDXIN GAMS_2014.gdx
$LOAD betadata
$GDXIN

betaRural(I) = betadata(I, "Rural") ;
betaUrbain(I) = betadata(I, "Urbain") ; 
betaMasculin(I) = betadata(I, "Masculin") ;
betaFeminin(I) = betadata(I, "Feminin") ;
betaR1(I)  = betadata(I, "R1") ; 
betaR2(I)  = betadata(I, "R2") ;
betaR3(I)  = betadata(I, "R3") ;
betaR4(I)  = betadata(I, "R4") ;
betaR5(I)  = betadata(I, "R5") ;
betaR6(I)  = betadata(I, "R6") ;
betaR7(I)  = betadata(I, "R7") ;
betaR8(I)  = betadata(I, "R8") ;
betaR9(I)  = betadata(I, "R9") ;
betaR10(I) = betadata(I, "R10") ;
betaR11(I) = betadata(I, "R11") ;
betaR12(I) = betadata(I, "R12") ;

PARAMETER
alphadata(*,*);

$CALL GDXXRW.EXE "GAMS_2014.xlsx" par=alphadata rng=Feuil1!A13:Q22 Rdim=1 Cdim=1
$GDXIN GAMS_2014.gdx
$LOAD alphadata
$GDXIN

alphaRural(I) = alphadata(I, "Rural");
alphaUrbain(I) = alphadata(I, "Urbain");
alphaMasculin(I) = alphadata(I, "Masculin");
alphaFeminin(I) = alphadata(I, "Feminin");
alphaR1(I)  = alphadata(I, "R1");
alphaR2(I)  = alphadata(I, "R2");
alphaR3(I)  = alphadata(I, "R3");
alphaR4(I)  = alphadata(I, "R4");
alphaR5(I)  = alphadata(I, "R5");
alphaR6(I)  = alphadata(I, "R6");
alphaR7(I)  = alphadata(I, "R7");
alphaR8(I)  = alphadata(I, "R8");
alphaR9(I)  = alphadata(I, "R9");
alphaR10(I) = alphadata(I, "R10");
alphaR11(I) = alphadata(I, "R11");
alphaR12(I) = alphadata(I, "R12");

display
betaRural
betaUrbain
betaMasculin
betaFeminin
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
alphaRural
alphaUrbain
alphaMasculin
alphaFeminin
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
;


variables
VCminRural(I)
VCminUrbain(I)
VCminMasculin(I)
VCminFeminin(I)
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
eqCMINMasculin
eqCMINFeminin
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

eqCMINRural(I)..    VCminRural(I)   - sum[J, -betaRural(J)*VCminRural(J)]   =e= alphaRural(I);
eqCMINUrbain(I)..   VCminUrbain(I)  - sum[J, -betaUrbain(J)*VCminUrbain(J)] =e= alphaUrbain(I);
eqCMINMasculin(I).. VCminMasculin(I)- sum[J, -betaMasculin(J)*VCminMasculin(J)] =e= alphaMasculin(I);
eqCMINFeminin(I)..  VCminFeminin(I) - sum[J, -betaFeminin(J)*VCminFeminin(J)] =e= alphaFeminin(I);

eqCMINR1(I)..  VCminR1(I)  - sum[J, -betaR1(J)*VCminR1(J)]  =e= alphaR1(I);
eqCMINR2(I)..  VCminR2(I)  - sum[J, -betaR2(J)*VCminR2(J)]  =e= alphaR2(I);
eqCMINR3(I)..  VCminR3(I)  - sum[J, -betaR3(J)*VCminR3(J)]  =e= alphaR3(I);
eqCMINR4(I)..  VCminR4(I)  - sum[J, -betaR4(J)*VCminR4(J)]  =e= alphaR4(I);
eqCMINR5(I)..  VCminR5(I)  - sum[J, -betaR5(J)*VCminR5(J)]  =e= alphaR5(I);
eqCMINR6(I)..  VCminR6(I)  - sum[J, -betaR6(J)*VCminR6(J)]  =e= alphaR6(I);
eqCMINR7(I)..  VCminR7(I)  - sum[J, -betaR7(J)*VCminR7(J)]  =e= alphaR7(I);
eqCMINR8(I)..  VCminR8(I)  - sum[J, -betaR8(J)*VCminR8(J)]  =e= alphaR8(I);
eqCMINR9(I)..  VCminR9(I)  - sum[J, -betaR9(J)*VCminR9(J)]  =e= alphaR9(I);
eqCMINR10(I).. VCminR10(I) - sum[J, -betaR10(J)*VCminR10(J)] =e= alphaR10(I);
eqCMINR11(I).. VCminR11(I) - sum[J, -betaR11(J)*VCminR11(J)] =e= alphaR11(I);
eqCMINR12(I).. VCminR12(I) - sum[J, -betaR12(J)*VCminR12(J)] =e= alphaR12(I);

option limrow = 10000   ;
OPTION NLP    = conopt4 ;

MODEL LESmodelRural     "Modele estimation equation LES" /eqCMINRural/;
MODEL LESmodelUrbain    "Modele estimation equation LES" /eqCMINUrbain/;
MODEL LESmodelMasculin  "Modele estimation equation LES" /eqCMINMasculin/;
MODEL LESmodelFeminin   "Modele estimation equation LES" /eqCMINFeminin/;

MODEL LESmodelR1  "Modele estimation equation LES" /eqCMINR1/;
MODEL LESmodelR2  "Modele estimation equation LES" /eqCMINR2/;
MODEL LESmodelR3  "Modele estimation equation LES" /eqCMINR3/;
MODEL LESmodelR4  "Modele estimation equation LES" /eqCMINR4/;
MODEL LESmodelR5  "Modele estimation equation LES" /eqCMINR5/;
MODEL LESmodelR6  "Modele estimation equation LES" /eqCMINR6/;
MODEL LESmodelR7  "Modele estimation equation LES" /eqCMINR7/;
MODEL LESmodelR8  "Modele estimation equation LES" /eqCMINR8/;
MODEL LESmodelR9  "Modele estimation equation LES" /eqCMINR9/;
MODEL LESmodelR10 "Modele estimation equation LES" /eqCMINR10/;
MODEL LESmodelR11 "Modele estimation equation LES" /eqCMINR11/;
MODEL LESmodelR12 "Modele estimation equation LES" /eqCMINR12/;

LESmodelRural.HOLDFIXED     = 1;
LESmodelUrbain.HOLDFIXED    = 1;
LESmodelMasculin.HOLDFIXED  = 1;
LESmodelFeminin.HOLDFIXED   = 1;

LESmodelR1.HOLDFIXED  = 1;
LESmodelR2.HOLDFIXED  = 1;
LESmodelR3.HOLDFIXED  = 1;
LESmodelR4.HOLDFIXED  = 1;
LESmodelR5.HOLDFIXED  = 1;
LESmodelR6.HOLDFIXED  = 1;
LESmodelR7.HOLDFIXED  = 1;
LESmodelR8.HOLDFIXED  = 1;
LESmodelR9.HOLDFIXED  = 1;
LESmodelR10.HOLDFIXED = 1;
LESmodelR11.HOLDFIXED = 1;
LESmodelR12.HOLDFIXED = 1;

SOLVE LESmodelRural     USING CNS;
SOLVE LESmodelUrbain    USING CNS;
SOLVE LESmodelMasculin  USING CNS;
SOLVE LESmodelFeminin   USING CNS;

SOLVE LESmodelR1  USING CNS;
SOLVE LESmodelR2  USING CNS;
SOLVE LESmodelR3  USING CNS;
SOLVE LESmodelR4  USING CNS;
SOLVE LESmodelR5  USING CNS;
SOLVE LESmodelR6  USING CNS;
SOLVE LESmodelR7  USING CNS;
SOLVE LESmodelR8  USING CNS;
SOLVE LESmodelR9  USING CNS;
SOLVE LESmodelR10 USING CNS;
SOLVE LESmodelR11 USING CNS;
SOLVE LESmodelR12 USING CNS;

display
VCminRural.L
VCminUrbain.L
VCminMasculin.L
VCminFeminin.L
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
VCminR12.L
;

execute_unload ".\LES-2014.gdx"
betaRural
betaUrbain
betaMasculin
betaFeminin
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
alphaRural
alphaUrbain
alphaMasculin
alphaFeminin
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
VCminRural.L
VCminUrbain.L
VCminMasculin.L
VCminFeminin.L
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
VCminR12.L
;

$setglobal outdir %USERPROFILE%\Downloads

$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminRural.L rng=Rural!A1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminUrbain.L rng=Urbain!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminMasculin.L rng=Masculin!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminFeminin.L rng=Feminin!A1 append=1

$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR1.L rng=R1!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR2.L rng=R2!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR3.L rng=R3!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR4.L rng=R4!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR5.L rng=R5!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR6.L rng=R6!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR7.L rng=R7!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR8.L rng=R8!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR9.L rng=R9!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR10.L rng=R10!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR11.L rng=R11!A1 append=1
$CALL GDXXRW.EXE results.gdx output="%outdir%\Results.xlsx" var=VCminR12.L rng=R12!A1 append=1


