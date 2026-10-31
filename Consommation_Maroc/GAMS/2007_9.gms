SET I Produits nomenclature 20 NCN
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

ALIAS(I,J);

parameter
betaRural(I)
betaUrbain(I)
betaMasculin(I)
betaFeminin(I)
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

alphaRural(I)
alphaUrbain(I)
alphaMasculin(I)
alphaFeminin(I)
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
;

PARAMETER
betadata(*,*);

$CALL GDXXRW.EXE "GAMS_2007.xlsx" par=betadata rng=Feuil1!A1:S10 Rdim=1 Cdim=1
$GDXIN GAMS_2007.gdx
$LOAD betadata
$GDXIN

betaRural(I) = betadata(I, "Rural") ;
betaUrbain(I) = betadata(I, "Urbain") ; 
betaMasculin(I) = betadata(I, "Masculin") ;
betaFeminin(I) = betadata(I, "Feminin") ;
betaSud(I) = betadata(I, "Sud") ;
betaR4(I)  = betadata(I, "R4") ;
betaR5(I)  = betadata(I, "R5") ;
betaR6(I)  = betadata(I, "R6") ;
betaR7(I)  = betadata(I, "R7") ;
betaR8(I)  = betadata(I, "R8") ;
betaR9(I)  = betadata(I, "R9") ;
betaR10(I) = betadata(I, "R10") ;
betaR11(I) = betadata(I, "R11") ;
betaR12(I) = betadata(I, "R12") ;
betaR13(I) = betadata(I, "R13") ;
betaR14(I) = betadata(I, "R14") ;
betaR15(I) = betadata(I, "R15") ;
betaR16(I) = betadata(I, "R16") ;

PARAMETER
alphadata(*,*);

$CALL GDXXRW.EXE "GAMS_2007.xlsx" par=alphadata rng=Feuil1!A13:S22 Rdim=1 Cdim=1
$GDXIN GAMS_2007.gdx
$LOAD alphadata
$GDXIN

alphaRural(I) = alphadata(I, "Rural");
alphaUrbain(I) = alphadata(I, "Urbain");
alphaMasculin(I) = alphadata(I, "Masculin");
alphaFeminin(I) = alphadata(I, "Feminin");
alphaSud(I) = alphadata(I, "Sud");
alphaR4(I)  = alphadata(I, "R4");
alphaR5(I)  = alphadata(I, "R5");
alphaR6(I)  = alphadata(I, "R6");
alphaR7(I)  = alphadata(I, "R7");
alphaR8(I)  = alphadata(I, "R8");
alphaR9(I)  = alphadata(I, "R9");
alphaR10(I) = alphadata(I, "R10");
alphaR11(I) = alphadata(I, "R11");
alphaR12(I) = alphadata(I, "R12");
alphaR13(I) = alphadata(I, "R13");
alphaR14(I) = alphadata(I, "R14");
alphaR15(I) = alphadata(I, "R15");
alphaR16(I) = alphadata(I, "R16");

variables
VCminRural(I)
VCminUrbain(I)
VCminMasculin(I)
VCminFeminin(I)
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
eqCMINMasculin
eqCMINFeminin
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

eqCMINRural(I)..    VCminRural(I)   - sum[J, -betaRural(J)*VCminRural(J)]   =e= alphaRural(I);
eqCMINUrbain(I)..   VCminUrbain(I)  - sum[J, -betaUrbain(J)*VCminUrbain(J)] =e= alphaUrbain(I);
eqCMINMasculin(I).. VCminMasculin(I)- sum[J, -betaMasculin(J)*VCminMasculin(J)] =e= alphaMasculin(I);
eqCMINFeminin(I)..  VCminFeminin(I) - sum[J, -betaFeminin(J)*VCminFeminin(J)] =e= alphaFeminin(I);
eqCMINSud(I)..      VCminSud(I)     - sum[J, -betaSud(J)*VCminSud(J)]         =e= alphaSud(I);

eqCMINR4(I)..  VCminR4(I)  - sum[J, -betaR4(J)*VCminR4(J)]  =e= alphaR4(I);
eqCMINR5(I)..  VCminR5(I)  - sum[J, -betaR5(J)*VCminR5(J)]  =e= alphaR5(I);
eqCMINR6(I)..  VCminR6(I)  - sum[J, -betaR6(J)*VCminR6(J)]  =e= alphaR6(I);
eqCMINR7(I)..  VCminR7(I)  - sum[J, -betaR7(J)*VCminR7(J)]  =e= alphaR7(I);
eqCMINR8(I)..  VCminR8(I)  - sum[J, -betaR8(J)*VCminR8(J)]  =e= alphaR8(I);
eqCMINR9(I)..  VCminR9(I)  - sum[J, -betaR9(J)*VCminR9(J)]  =e= alphaR9(I);
eqCMINR10(I).. VCminR10(I) - sum[J, -betaR10(J)*VCminR10(J)] =e= alphaR10(I);
eqCMINR11(I).. VCminR11(I) - sum[J, -betaR11(J)*VCminR11(J)] =e= alphaR11(I);
eqCMINR12(I).. VCminR12(I) - sum[J, -betaR12(J)*VCminR12(J)] =e= alphaR12(I);
eqCMINR13(I).. VCminR13(I) - sum[J, -betaR13(J)*VCminR13(J)] =e= alphaR13(I);
eqCMINR14(I).. VCminR14(I) - sum[J, -betaR14(J)*VCminR14(J)] =e= alphaR14(I);
eqCMINR15(I).. VCminR15(I) - sum[J, -betaR15(J)*VCminR15(J)] =e= alphaR15(I);
eqCMINR16(I).. VCminR16(I) - sum[J, -betaR16(J)*VCminR16(J)] =e= alphaR16(I);

option limrow = 10000   ;
OPTION NLP    = conopt4 ;

MODEL LESmodelRural     /eqCMINRural/;
MODEL LESmodelUrbain    /eqCMINUrbain/;
MODEL LESmodelMasculin  /eqCMINMasculin/;
MODEL LESmodelFeminin   /eqCMINFeminin/;
MODEL LESmodelSud       /eqCMINSud/;

MODEL LESmodelR4  /eqCMINR4/;
MODEL LESmodelR5  /eqCMINR5/;
MODEL LESmodelR6  /eqCMINR6/;
MODEL LESmodelR7  /eqCMINR7/;
MODEL LESmodelR8  /eqCMINR8/;
MODEL LESmodelR9  /eqCMINR9/;
MODEL LESmodelR10 /eqCMINR10/;
MODEL LESmodelR11 /eqCMINR11/;
MODEL LESmodelR12 /eqCMINR12/;
MODEL LESmodelR13 /eqCMINR13/;
MODEL LESmodelR14 /eqCMINR14/;
MODEL LESmodelR15 /eqCMINR15/;
MODEL LESmodelR16 /eqCMINR16/;


LESmodelRural.HOLDFIXED     = 1;
LESmodelUrbain.HOLDFIXED    = 1;
LESmodelMasculin.HOLDFIXED  = 1;
LESmodelFeminin.HOLDFIXED   = 1;
LESmodelSud.HOLDFIXED       = 1;

LESmodelR4.HOLDFIXED  = 1;
LESmodelR5.HOLDFIXED  = 1;
LESmodelR6.HOLDFIXED  = 1;
LESmodelR7.HOLDFIXED  = 1;
LESmodelR8.HOLDFIXED  = 1;
LESmodelR9.HOLDFIXED  = 1;
LESmodelR10.HOLDFIXED = 1;
LESmodelR11.HOLDFIXED = 1;
LESmodelR12.HOLDFIXED = 1;
LESmodelR13.HOLDFIXED = 1;
LESmodelR14.HOLDFIXED = 1;
LESmodelR15.HOLDFIXED = 1;
LESmodelR16.HOLDFIXED = 1;

*========================
* SOLVE
*========================

SOLVE LESmodelRural     USING CNS;
SOLVE LESmodelUrbain    USING CNS;
SOLVE LESmodelMasculin  USING CNS;
SOLVE LESmodelFeminin   USING CNS;
SOLVE LESmodelSud       USING CNS;

SOLVE LESmodelR4  USING CNS;
SOLVE LESmodelR5  USING CNS;
SOLVE LESmodelR6  USING CNS;
SOLVE LESmodelR7  USING CNS;
SOLVE LESmodelR8  USING CNS;
SOLVE LESmodelR9  USING CNS;
SOLVE LESmodelR10 USING CNS;
SOLVE LESmodelR11 USING CNS;
SOLVE LESmodelR12 USING CNS;
SOLVE LESmodelR13 USING CNS;
SOLVE LESmodelR14 USING CNS;
SOLVE LESmodelR15 USING CNS;
SOLVE LESmodelR16 USING CNS;

*========================
* DISPLAY
*========================

DISPLAY
VCminRural.L
VCminUrbain.L
VCminMasculin.L
VCminFeminin.L
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
VCminR16.L
;

*========================
* EXPORT GDX
*========================

execute_unload ".\LES-2007.gdx"
betaRural
betaUrbain
betaMasculin
betaFeminin
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

alphaRural
alphaUrbain
alphaMasculin
alphaFeminin
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

VCminRural.L
VCminUrbain.L
VCminMasculin.L
VCminFeminin.L
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
VCminR16.L
;